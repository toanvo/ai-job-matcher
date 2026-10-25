import pytest
import json

from job_matcher.storage import load_jobs
from job_matcher.exceptions import InvalidJobError


def test_load_empty_jobs(tmp_path):
    file_path = tmp_path / "jobs.json"
    file_path.write_text("[]", encoding="utf-8")

    jobs = load_jobs(file_path)

    assert jobs == []


def test_load_valid_jobs(tmp_path):
    jobs = [
        {"title": "AI Engineer", "skills": ["Python", "LLM"]},
        {"title": "Backend Developer", "skills": ["C#", "Azure"]},
    ]

    file_path = tmp_path / "jobs.json"
    file_path.write_text(json.dumps(jobs), encoding="utf-8")

    result = load_jobs(file_path)

    assert result == jobs


def test_load_missing_file(tmp_path):
    file_path = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError):
        load_jobs(file_path)


def test_load_invalid_json(tmp_path):
    file_path = tmp_path / "jobs.json"
    file_path.write_text("{invalid json}", encoding="utf-8")


    with pytest.raises(json.JSONDecodeError):
        load_jobs(file_path)

def test_load_non_list_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{}", encoding="utf-8")

    with pytest.raises(ValueError):
        load_jobs(file_path)


def test_load_invalid_jobs(tmp_path):
    file_path = tmp_path / "invalid.json"

    jobs = [
        {
            "title": "AI Engineer",
            "skills": None
        }
    ]

    file_path.write_text(json.dumps(jobs), encoding="utf-8")

    with pytest.raises(InvalidJobError):
        load_jobs(file_path)