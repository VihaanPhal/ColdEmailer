from flask import Flask
from flask_cors import CORS
from routes.send_emails import process_email

app = Flask(__name__)
CORS(app)

# Flask Route to Process and Send Emails
@app.route('/send-emails', methods=['POST'])
def process_emails():
    return process_email()

if __name__ == "__main__":
    app.run(debug=True)