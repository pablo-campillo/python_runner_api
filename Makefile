start_fast_api_server:
	uvicorn src.python_runner.main:app --reload

start_sam_server:
	sam local start-api

request_local_api:
	curl -X POST http://127.0.0.1:3000/ -H 'Content-Type: application/json' -d @body.json