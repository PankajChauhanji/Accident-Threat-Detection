from email.mime.text import MIMEText
import smtplib

def send_email_alert(recipients, subject, body):
    # Replace with your actual SMTP settings
    smtp_server = 'smtp.gmail.com' 
    smtp_port = 587  
    username = 'psg.freel@gmail.com'  
    password = 'rtra xhlx disw yube'

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = username
    message['To'] = ', '.join(recipients) 

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls() 
            server.login(username, password)
            server.sendmail(username, recipients, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)