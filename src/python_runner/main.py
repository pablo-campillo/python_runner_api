from fastapi import FastAPI
from starlette.responses import JSONResponse

from python_runner.python_runner import PythonRunner
from python_runner.schemas import CodeKataSubmission, CodeKataSubmissionResult, Message

app = FastAPI()
runner = PythonRunner()


@app.exception_handler(SyntaxError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=452,
        content={"message": "Oops! Invalid Syntax in your code!"},
    )


@app.post(
    "/",
    response_model=CodeKataSubmissionResult,
    responses={
        452: {"model": Message, "description": "Python code syntax is not valid."},
    }
)
async def run_python(submission: CodeKataSubmission):
    return runner.submit(submission)
