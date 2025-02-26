from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.file_processor import load_recruiters
from utils.email_generator import generate_email
from utils.email_sender import send_email_with_attachment
import os

app = Flask(__name__)
CORS(app)

# Flask Route to Process and Send Emails
@app.route('/send-emails', methods=['POST'])
def process_emails():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    recruiters = load_recruiters(file)
    
    if recruiters is None:
        return jsonify({"error": "Failed to process CSV file"}), 400

    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    attachment_path = "static/VihaanPhal_Fulltime.pdf"

    for _, row in recruiters.iterrows():
        name, email, company = row["Name"], row["Email"], row["Company"]
        email_body = generate_email(name, company)

        print(f"\nEmail to {name} ({email}):\n{email_body}")
        confirm = input("Send this email? (y/n): ")

        if confirm.lower() == 'y':
            send_email_with_attachment(
                to_email=email,
                subject="Bit of a read but absolutely worth it!",
                body=email_body,
                sender_email=sender_email,
                sender_password=sender_password,
                attachment_path=attachment_path
            )
        else:
            print("Skipped.")

    return jsonify({"message": "Emails processed."})

if __name__ == "__main__":
    app.run(debug=True)
