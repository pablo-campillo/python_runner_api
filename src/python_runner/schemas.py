from pydantic import BaseModel, ConfigDict


class CKSBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class Message(CKSBase):
    message: str


class CodeKataSubmissionResult(CKSBase):
    time_secs: float
    peak_mem_bytes: int
    final_mem_bytes: int
    sample_tests_pass: bool
    extra_tests_pass: bool


class CodeKataSubmission(CKSBase):
    code: str
    sample_tests: str
    extra_tests: str
    performance_tests: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "code": "def add(a: int, b: int):\n  result = a+b\n  return result\n",
                    "sample_tests": "assert add(2,3) == 5",
                    "extra_tests": "assert add(1,2) == 3",
                    "performance_tests": "add(1,2)",
                }
            ]
        }
    }

