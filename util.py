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


def generate_email_body(user_data, emergency_contact):
    # Extract user information
    user_name = user_data.get('name', '')
    user_email = user_data.get('email', '')
    user_phone = user_data.get('phone', '')
    user_address = user_data.get('address', '')
    user_blood_group = user_data.get('bloodGroup', '')
    user_treating_doctor = user_data.get('treatingDoctor', '')

    # Extract emergency contact information
    emg_name = user_data.get('emgName1', '')
    emg_email = user_data.get('emgEmail1', '')
    emg_phone = user_data.get('emgPhone1', '')

    # Construct email body
    email_body = f"""Subject: Accident Alert!

        Dear Emergency Contact,

        This is to notify you that an accident may have occurred involving {user_name}.

        Details of the user:
        - Name: {user_name}
        - Email: {user_email}
        - Phone: {user_phone}
        - Address: {user_address}
        - Blood Group: {user_blood_group}
        - Treating Doctor: {user_treating_doctor}

        Emergency Contact Information:
        - Name: {emg_name}
        - Email: {emg_email}
        - Phone: {emg_phone}

        Please take necessary actions as per the situation.

        Thank you.

        Sincerely,
        [Your Organization's Name]"""

    return email_body
