from job_matcher.results import Result


def test_success_result():    
    result = Result(data = 100.0)
    assert result.data == 100.0
    assert result.is_success is True

def test_failure_result():    
    result = Result(error="Invalid Job")    
    assert result.is_success is False
    assert result.error == "Invalid Job"

def test_generic_result_with_list(): 
    result = Result(data = ["Python", "Azure"])    
    assert len(result.data) == 2 