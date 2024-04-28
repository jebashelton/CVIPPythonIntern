import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Setup SMTP connection
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)

        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach body to message
        msg.attach(MIMEText(body, 'plain'))

        # Send email
        smtp_server.send_message(msg)

        # Quit SMTP connection
        smtp_server.quit()
        print(f"Email sent to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {str(e)}")

def main():
    # Sender's email credentials
    sender_email = 'your_email@gmail.com'  # Change to your email
    sender_password = 'your_password'  # Change to your password

    # Email details
    subject = 'Personalized Email'
    body_template = '''
    Dear {name},
    
    We hope this email finds you well. We are excited to inform you about our latest offerings.
    
    Regards,
    Your Name
    '''

    # Read recipient details from CSV file
    with open('recipients.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['Email']
            name = row['Name']
            
            # Personalize email body
            body = body_template.format(name=name)

            # Send email
            send_email(sender_email, sender_password, recipient_email, subject, body)

if __name__ == "__main__":
    main()
