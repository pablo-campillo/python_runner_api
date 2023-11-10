from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from python_runner.schemas import CodeKataSubmission, CodeKataSubmissionResult


class PythonRunner:
    """Abstract class that provides methods for managing code katas"""

    def submit(
            self, code_kata_submission: CodeKataSubmission
    ) -> CodeKataSubmissionResult:
        timeit_number = 10
        with TemporaryDirectory() as tmpdirname:
            with (Path(tmpdirname) / "main.py").open("w") as f:
                f.write(code_kata_submission.code)
            with (Path(tmpdirname) / "test_sample.py").open("w") as f:
                f.write("from main import *\n\n")
                f.write("def test_sample():\n")
                f.writelines(f"  {l}\n" for l in code_kata_submission.sample_tests.split('\n'))
            with (Path(tmpdirname) / "test_extra.py").open("w") as f:
                f.write("from main import *\n\n")
                f.write("def test_extra():\n")
                f.writelines(f"  {l}\n" for l in code_kata_submission.extra_tests.split('\n'))
            with (Path(tmpdirname) / "test_performance.py").open("w") as f:
                f.write("import tracemalloc\n\n")
                f.write(code_kata_submission.code+"\n")
                f.write("tracemalloc.start()\n")
                f.writelines(f"{l}\n" for l in code_kata_submission.performance_tests.split('\n'))
                f.write("print(tracemalloc.get_traced_memory())\n")
                f.write("tracemalloc.stop()\n")

            import timeit
            time_secs = timeit.timeit(
                code_kata_submission.performance_tests, setup=code_kata_submission.code, number=timeit_number)
            time_secs /= timeit_number

            import subprocess
            out = subprocess.check_output(['python3', str(Path(tmpdirname) / "test_performance.py")])
            final_mem_bytes, peak_mem_bytes = eval(out)

            result1 = pytest.main([f"{tmpdirname}/test_sample.py"])
            sample_tests_pass = result1 == 0
            extra_tests_pass = pytest.main([f"{tmpdirname}/test_extra.py"]) == 0
        return CodeKataSubmissionResult(
            time_secs=time_secs,
            peak_mem_bytes=peak_mem_bytes,
            final_mem_bytes=final_mem_bytes,
            sample_tests_pass=sample_tests_pass,
            extra_tests_pass=extra_tests_pass,
        )