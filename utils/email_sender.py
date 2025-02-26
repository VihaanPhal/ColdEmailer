import smtplib
from email.message import EmailMessage
import mimetypes
import os

def send_email_with_attachment(to_email, subject, body, sender_email, sender_password, attachment_path):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = to_email

        if os.path.exists(attachment_path):
            with open(attachment_path, "rb") as file:
                file_data = file.read()
                file_type, _ = mimetypes.guess_type(attachment_path)
                file_type = file_type or "application/octet-stream"
                
                msg.add_attachment(
                    file_data,
                    maintype=file_type.split("/")[0],
                    subtype=file_type.split("/")[1],
                    filename=os.path.basename(attachment_path)
                )
        else:
            print(f"Warning: Attachment not found at {attachment_path}")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"Email successfully sent to {to_email}")

    except Exception as e:
        print(f"Error sending email: {e}")
