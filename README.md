# Email Security Gateway with Phishing Detection

A beginner-friendly cybersecurity internship project that scans sample email text for common phishing indicators using transparent, rule-based checks.

## Features

- Checks for urgent or threatening phrases and suspicious wording.
- Extracts links from email body text.
- Flags HTTP links and some suspicious hostname patterns.
- Assigns a simple risk score and displays a verdict.
- Includes fictional sample emails and automated unit tests.
- Provides a small Flask web interface.

## Important limitation

This is an educational demonstration, not a production email gateway. It does not check domain reputation, SPF/DKIM/DMARC, attachments, redirects, or live threat-intelligence feeds. Attackers can evade simple phrase rules, and legitimate messages can trigger false positives. A low-risk result does not prove that an email is safe.

## Requirements

- Python 3.10 or newer
- pip

## Setup

### Windows (PowerShell)

```powershell
py -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open the local address shown in the terminal (normally `http://127.0.0.1:5000`).

Keep the app on your own computer. Do not expose Flask's development server to the public internet.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
email_security_gateway_phishing_detection/
├── app.py
├── detector.py
├── requirements.txt
├── sample_emails.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── tests/
    └── test_detector.py
```

## Example test

Try the fictional message in `sample_emails.txt` labelled **SUSPICIOUS**. The app should identify warning signs and assign a higher risk score. Then try the ordinary class-schedule example.

## Ethical use

Only analyze email content you are authorized to inspect. Use fictional or sanitized examples in screenshots and public repositories. Never commit credentials, private emails, personal data, or API keys.

## Future improvements

- Add safe domain reputation checks through a trusted API.
- Add SPF/DKIM/DMARC header analysis.
- Add a configurable allowlist/blocklist.
- Store anonymized scan results securely with user consent.
- Add more tests for false positives and false negatives.

## Author

Add your name, internship details, and completion date here before publishing.
