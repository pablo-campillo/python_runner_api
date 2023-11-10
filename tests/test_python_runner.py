from python_runner.python_runner import PythonRunner
from python_runner.schemas import CodeKataSubmission, CodeKataSubmissionResult


def test_python_runner():
    runner = PythonRunner()

    code_kata_submission = CodeKataSubmission(
        code="def add(a: int, b: int):\n  result = a+b\n  return result\n",
        sample_tests="assert add(2,3) == 5",
        extra_tests="assert add(1,2) == 3",
        performance_tests="add(1,2)",
    )

    result: CodeKataSubmissionResult = runner.submit(code_kata_submission)

    assert result.time_secs > 0
    assert result.peak_mem_bytes >= 0
    assert result.final_mem_bytes >= 0
    assert result.sample_tests_pass
    assert result.extra_tests_pass
