# IBD Nutrition & Symptom Tracker

A beginner-friendly **Python + Streamlit + SQLite** application for logging meals, estimated calories, protein, and self-reported symptoms, with simple daily charts. Portfolio demonstration, **not a medical device**.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Features: meal and symptom entry, local SQLite storage, dashboard charts, CSV export, basic validation, and unit tests.

**Privacy:** `tracker.db` is excluded by `.gitignore`. Never upload real patient data to GitHub. If hosted remotely, data are saved on the server: do not deploy for real health information without suitable authentication, security, and privacy review.

No diagnoses, dietary recommendations, or claims that specific foods cause symptoms. Run tests: `python -m unittest discover -s tests`.
