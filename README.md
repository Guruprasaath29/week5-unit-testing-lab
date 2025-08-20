# Week 5 Lab: Unit Testing & Automation (Pytest + GitHub Actions)

## How to run locally
```bash
# Optional: create venv
# python -m venv .venv && source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate                           # Windows PowerShell

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Run tests
pytest -q
```

## Files
- `example1.py` / `test_1.py` – is_even()
- `example2.py` / `test_2.py` – reverse_string()
- `.github/workflows/python-app.yml` – CI workflow
