from mangum import Mangum

from python_runner.main import app

lambda_handler = Mangum(app, lifespan="off")
