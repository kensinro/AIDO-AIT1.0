# Reproduce the Minimal Public MVP

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

Expected result: 8 passing tests.

These tests verify the public reference lifecycle only. They do not replace the
historical 49-test evaluated-release evidence described in the manuscript.
