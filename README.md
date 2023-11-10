# Python Runner

An API for running python code.

## Example

Provide code and tests (pytest is used):

```json
{
  "code":"def add(a: int, b: int):\n  result = a+b\n  return result\n",
  "sample_tests":"assert add(2,3) == 5",
  "extra_tests":"assert add(1,2) == 3",
  "performance_tests":"add(1,2)"
}
```

And get:

```json
{
    "time_secs":2.1300220396369695e-07,
    "peak_mem_bytes":0,
    "final_mem_bytes":0,
    "sample_tests_pass":true,
    "extra_tests_pass":true
}
```