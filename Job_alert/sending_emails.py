from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
import csv
import io
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
def extract_top_results(csv_content, n=5):
    """Extract top n rows from a CSV content string."""
    try:
        csv_file = io.StringIO(csv_content)
        csv_reader = csv.reader(csv_file)
        
        # Get headers and top n rows
        headers = next(csv_reader)
        top_rows = []
        for i, row in enumerate(csv_reader):
            if i < n:
                top_rows.append(row)
            else:
                break
                
        return headers, top_rows
    except Exception as e:
        print(f"Error extracting CSV data: {e}")
        return [], []

def format_csv_for_email(csv_name, headers, rows):
    """Format CSV data for plain text email."""
    text = f"\n\n--- TOP 5 RESULTS FROM {csv_name.upper()} ---\n\n"
    
    # Format headers
    text += " | ".join(headers) + "\n"
    text += "-" * 80 + "\n"
    
    # Format rows
    for row in rows:
        text += " | ".join(row) + "\n"
    
    return text

# def send_email_with_csv_summary(recipient_email, keyword, location, csv_data, email_user, app_password):
#     """Send an email using Gmail with App Password and include CSV summary."""
#     try:
#         # Create message
#         message = MIMEMultipart()
#         message["From"] = email_user
#         message["To"] = recipient_email
#         message["Subject"] = f"Job Search Results for {keyword} in {location}"
        
#         # Basic email body
#         body = f"""
# Hello,

# Here are the top results for your job search for "{keyword}" in {location}:
# """
        
#         # Add CSV summaries to body
#         for csv_name, csv_content in csv_data.items():
#             headers, top_rows = extract_top_results(csv_content)
#             if headers and top_rows:
#                 csv_summary = format_csv_for_email(csv_name, headers, top_rows)
#                 body += csv_summary
        
#         body += f"""

# Full results are attached as CSV files.

# Best regards,
# Your Application Team
# """
        
#         # Attach the text body
#         message.attach(MIMEText(body, "plain"))
        
#         # Attach CSV files
#         for csv_name, csv_content in csv_data.items():
#             attachment = MIMEApplication(csv_content.encode('utf-8'))
#             attachment['Content-Disposition'] = f'attachment; filename="{csv_name}.csv"'
#             message.attach(attachment)
        
#         # Gmail SMTP settings
#         email_host = "smtp.gmail.com"
#         email_port = 587
        
#         # Connect to email server and send
#         with smtplib.SMTP(email_host, email_port) as server:
#             server.starttls()
#             print("Attempting to log in to Gmail...")
#             server.login(email_user, app_password)
#             print("Login successful!")
#             server.send_message(message)
        
#         print("✅ Email with CSV summaries sent successfully!")
#         return True
#     except Exception as e:
#         print(f"❌ Error sending email: {e}")
#         if hasattr(e, 'smtp_code'):
#             print(f"SMTP Code: {e.smtp_code}")
#         if hasattr(e, 'smtp_error'):
#             print(f"SMTP Error: {e.smtp_error}")
#         return False

def send_email_with_csv_summary(recipient_email, keyword, location, csv_data, email_user, app_password):
    """Send an email using Gmail with top 5 job summaries only (no attachments)."""
    try:
        # Create message
        message = MIMEMultipart()
        message["From"] = email_user
        message["To"] = recipient_email
        message["Subject"] = f"Top Job Results for {keyword} in {location}"
        
        # Email body with top results
        body = f"""
Hello,

Here are the top results for your job search: "{keyword}" in {location}
"""
        for csv_name, csv_content in csv_data.items():
            headers, top_rows = extract_top_results(csv_content)
            if headers and top_rows:
                csv_summary = format_csv_for_email(csv_name, headers, top_rows)
                body += csv_summary

                body += "\nBest regards,\nYour Job Alert Team"

        # Attach the text body only
        message.attach(MIMEText(body, "plain"))
        
        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            print("Attempting to log in to Gmail...")
            server.login(email_user, app_password)
            print("Login successful!")
            server.send_message(message)

        print("✅ Summary email sent successfully!")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False
def send_email(recipient_email, keyword, location, email_user, app_password):
    """Send an email using Gmail with App Password."""
    try:
        # Create message
        message = MIMEMultipart()
        message["From"] = email_user
        message["To"] = recipient_email
        message["Subject"] = f"Subscription Confirmation for {keyword} in {location}"
        
        # Email body
        body = f"""
        Hello World!
        
        Thank you for subscribing to updates about "{keyword}" in {location}.
        We'll keep you informed about any new developments.
        
        Best regards,
        Your Application Team
        """
        
        message.attach(MIMEText(body, "plain"))
        
        # Gmail SMTP settings
        email_host = "smtp.gmail.com"
        email_port = 587
        
        # Connect to email server and send
        with smtplib.SMTP(email_host, email_port) as server:
            server.starttls()
            print("Attempting to log in to Gmail...")
            server.login(email_user, app_password)
            print("Login successful!")
            server.send_message(message)
        
        print("✅ Email sent successfully!")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        if hasattr(e, 'smtp_code'):
            print(f"SMTP Code: {e.smtp_code}")
        if hasattr(e, 'smtp_error'):
            print(f"SMTP Error: {e.smtp_error}")
        return False
