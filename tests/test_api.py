from fastapi.testclient import TestClient

from python_runner.main import app

client = TestClient(app)


def test_simple_run():
    data = {
        "code": "def add(a: int, b: int):\n  result = a+b\n  return result\n",
        "sample_tests": "assert add(2,3) == 5",
        "extra_tests": "assert add(1,2) == 3",
        "performance_tests": "add(1,2)"
    }
    response = client.post("/", json=data)
    response_dict = response.json()
    assert response.status_code == 200
    assert response_dict['time_secs'] > 0
    assert response_dict['peak_mem_bytes'] >= 0
    assert response_dict['final_mem_bytes'] >= 0
    assert response_dict['sample_tests_pass']
    assert response_dict['extra_tests_pass']


def test_bad_code_python():
    data = {
        "code": "def add(a: int, b: int):\n  result = a+\n  return result\n",
        "sample_tests": "assert add(2,3) == 5",
        "extra_tests": "assert add(1,2) == 3",
        "performance_tests": "add(1,2)"
    }
    response = client.post("/", json=data)
    response_dict = response.json()
    assert response.status_code == 452
    assert response_dict['message'] == "Oops! Invalid Syntax in your code!"
