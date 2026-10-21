from flask import Flask, render_template, request
from detector import analyze_email

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    email_text = ""
    sender = ""
    subject = ""
    if request.method == "POST":
        sender = request.form.get("sender", "").strip()
        subject = request.form.get("subject", "").strip()
        email_text = request.form.get("email_text", "").strip()
        result = analyze_email(sender, subject, email_text)
    return render_template(
        "index.html",
        result=result,
        sender=sender,
        subject=subject,
        email_text=email_text,
    )

if __name__ == "__main__":
    # Local demo only. Do not expose this development server to the public internet.
    app.run(debug=True)
