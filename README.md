# Calculator with unit tests (Python)

A small calculator module written to practise test-driven development. Pair
work with Amrita Ketireddy.

`calculator.py` implements one function per operation — add, subtract,
multiply, divide, logarithm, hypotenuse, and square root. `test_calculator.py`
covers them with 10 tests that include the failure paths, not just the happy
ones: division by zero, an invalid logarithm base, and an invalid logarithm
argument each get their own case.

## Run the tests

```bash
python -m pytest test_calculator.py
```
