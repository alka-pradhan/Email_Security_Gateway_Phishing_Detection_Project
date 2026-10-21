import unittest
from detector import analyze_email, extract_urls

class DetectorTests(unittest.TestCase):
    def test_urgent_phishing_text_is_flagged(self):
        result = analyze_email(
            "security@example.com",
            "Urgent action required",
            "Your account suspended. Verify your account and login now."
        )
        self.assertIn(result["verdict"], {"SUSPICIOUS", "HIGH RISK"})
        self.assertGreaterEqual(result["score"], 2)

    def test_normal_text_has_no_high_risk_verdict(self):
        result = analyze_email(
            "teacher@example.edu",
            "Class notes",
            "Hello, the class notes are attached. See you tomorrow."
        )
        self.assertEqual(result["verdict"], "LOW RISK INDICATORS")

    def test_extract_urls(self):
        self.assertEqual(extract_urls("Visit https://example.com/test."), ["https://example.com/test"])

if __name__ == "__main__":
    unittest.main()
