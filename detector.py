"""Rule-based phishing indicator scanner for educational demonstration.

This tool flags common warning signs. It is not an antivirus product and cannot
prove that an email is safe or malicious.
"""
import re
from urllib.parse import urlparse

URGENT_PHRASES = [
    "verify your account", "account suspended", "urgent action",
    "act immediately", "password expires", "confirm your password",
    "unusual activity", "claim your prize", "payment failed",
]
SUSPICIOUS_PHRASES = [
    "click here", "login now", "update your details", "send your password",
    "bank account", "gift card", "wire transfer",
]
URL_RE = re.compile(r"""https?://[^\s<>"']+|www\.[^\s<>"']+""", re.IGNORECASE)
IP_HOST_RE = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$")

def extract_urls(text):
    """Return URLs found in text, removing common trailing punctuation."""
    return [u.rstrip(".,!?;:)]}") for u in URL_RE.findall(text or "")]

def analyze_email(sender, subject, body):
    content = f"{sender}\n{subject}\n{body}".lower()
    score = 0
    findings = []

    for phrase in URGENT_PHRASES:
        if phrase in content:
            score += 2
            findings.append(f"Urgent or threatening language: “{phrase}”")

    for phrase in SUSPICIOUS_PHRASES:
        if phrase in content:
            score += 1
            findings.append(f"Potentially risky wording: “{phrase}”")

    urls = extract_urls(body)
    for raw_url in urls:
        candidate = raw_url if raw_url.lower().startswith(("http://", "https://")) else "http://" + raw_url
        host = (urlparse(candidate).hostname or "").lower()
        if candidate.lower().startswith("http://"):
            score += 1
            findings.append(f"Link uses unencrypted HTTP: {raw_url}")
        if host and (IP_HOST_RE.match(host) or host.startswith("xn--")):
            score += 2
            findings.append(f"Link uses an IP address or punycode hostname: {raw_url}")
        if "@" in urlparse(candidate).netloc:
            score += 2
            findings.append(f"Link contains an @ sign in its network location: {raw_url}")

    if sender and not re.search(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", sender):
        findings.append("Sender field is not in a typical email-address format.")
        score += 1

    if not findings:
        findings.append("No indicators from this simple rule set were found.")

    if score >= 4:
        verdict = "HIGH RISK"
        explanation = "Several warning signs were detected. Do not click links or provide sensitive information."
    elif score >= 2:
        verdict = "SUSPICIOUS"
        explanation = "Some warning signs were detected. Verify the sender through a separate trusted channel."
    else:
        verdict = "LOW RISK INDICATORS"
        explanation = "Few warning signs were detected by this demo. This does not guarantee the email is safe."

    return {
        "score": score,
        "verdict": verdict,
        "explanation": explanation,
        "findings": findings,
        "urls": urls,
    }
