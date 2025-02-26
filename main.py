# from flask import Flask, request, jsonify
# import pandas as pd
# import smtplib
# from email.message import EmailMessage
# import subprocess
# from flask_cors import CORS
# import mimetypes
# import os

# app = Flask(__name__)
# CORS(app)

# # Load CSV file
# def load_recruiters(csv_file):
#     try:
#         df = pd.read_csv(csv_file)

#         # Ensure expected columns exist
#         expected_columns = ["Name", "Email", "Company"]
#         for col in expected_columns:
#             if col not in df.columns:
#                 raise KeyError(f"Missing column: {col}. Ensure CSV has 'Name', 'Email', 'Company'.")

#         return df[expected_columns].dropna()
    
#     except Exception as e:
#         print(f"Error loading CSV: {e}")
#         return None

# # Generate Email using Local DeepSeek/Llama
# def generate_email(name, company):
#     prompt = f"""Generate a professional cold email body for job applications with NO introduction, explanation, or commentary. I need ONLY the email content from greeting to signature.

# Use these exact details about me:
# - Name: Vihaan Phal
# - Education: Computer Science degree from Arizona State University (3.86 GPA)
# - Technical skills: ReactJS, Node.js, Python, C#, Swift, AWS, PyTorch, scikit-learn, full-stack development, AI, distributed systems

# My notable projects demonstrate problem-solving abilities:
# 1. StockLearn: After losing money in the stock market due to insufficient research, I built an interactive platform using ReactJS, MongoDB, and Firebase that allows users to simulate investments with dummy money to learn market behavior before risking real capital.

# 2. ConvoCoach: While job hunting, I needed mock interview practice but friends weren't always available. I created an AI-driven platform using Next.js, Flask, and Meta Llama 3.1 that provides interview simulations with AI-powered avatars. This evolved into my company, ConvoCoach.com, offering personalized interview preparation with real-time feedback.

# The email should:
# - Be addressed to {name} at {company}
# - Portray me as extremely confident but not arrogant
# - Emphasize my problem-solving mindset and ability to identify real-world needs
# - Highlight how my technical skills and innovative approaches will specifically benefit {company}
# - Include a clear call-to-action requesting a meeting
# - Be concise (max 250 words) yet impactful
# - Use a professional but warm tone
# - NOT include any subject line or pre/post commentary

# Provide ONLY the email body text, starting with "Dear {name}," and ending with my signature.
#     """
    
#     try:
#         result = subprocess.run(
#             ["ollama", "run", "llama2:13b", prompt],
#             capture_output=True,
#             text=True,
#             timeout=30  # Set timeout to prevent hanging
#         )
#         return result.stdout.strip()
#     except Exception as e:
#         print(f"Error generating email: {e}")
#         return "Error generating email. Please check the AI model setup."

# # Send email function
# def send_email_with_attachment(to_email, subject, body, sender_email, sender_password, attachment_path):
#     try:
#         msg = EmailMessage()
#         msg.set_content(body)
#         msg["Subject"] = subject
#         msg["From"] = sender_email
#         msg["To"] = to_email

#         # Attach a file (Resume)
#         if os.path.exists(attachment_path):
#             with open(attachment_path, "rb") as file:
#                 file_data = file.read()
#                 file_type, _ = mimetypes.guess_type(attachment_path)
#                 file_type = file_type or "application/octet-stream"
                
#                 msg.add_attachment(
#                     file_data,
#                     maintype=file_type.split("/")[0],
#                     subtype=file_type.split("/")[1],
#                     filename=os.path.basename(attachment_path)
#                 )
#         else:
#             print(f"Warning: Attachment not found at {attachment_path}")

#         # Send email
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#             server.login(sender_email, sender_password)
#             server.send_message(msg)
#         print(f"Email successfully sent to {to_email}")

#     except Exception as e:
#         print(f"Error sending email: {e}")

# # Flask Route to Process and Send Emails
# @app.route('/send-emails', methods=['POST'])
# def process_emails():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400
    
#     file = request.files['file']
    
#     if file.filename == '':
#         return jsonify({"error": "No file selected"}), 400

#     recruiters = load_recruiters(file)
    
#     if recruiters is None:
#         return jsonify({"error": "Failed to process CSV file"}), 400

#     sender_email = "phal.vihaan@gmail.com"
#     sender_password = "dddz kekv hwda ztmk"  # Store in environment variables
#     attachment_path = "VihaanPhal_Fulltime copy.pdf"

#     for _, row in recruiters.iterrows():
#         name, email, company = row["Name"], row["Email"], row["Company"]
#         email_body = generate_email(name, company)

#         print(f"\nEmail to {name} ({email}):\n{email_body}")
#         confirm = input("Send this email? (y/n): ")

#         if confirm.lower() == 'y':
#             send_email_with_attachment(
#                 to_email=email,
#                 subject="Bit of a read but absolutely worth it!",
#                 body=email_body,
#                 sender_email=sender_email,
#                 sender_password=sender_password,
#                 attachment_path=attachment_path
#             )
#         else:
#             print("Skipped.")

#     return jsonify({"message": "Emails processed."})

# if __name__ == "__main__":
#     app.run(debug=True)
