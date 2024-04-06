from email.mime.text import MIMEText
import smtplib

def send_email_alert(recipients, subject, body):
    # Replace with your actual SMTP settings
    smtp_server = 'smtp.gmail.com' 
    smtp_port = 587  
    username = 'psg.freel@gmail.com'  
    password = 'rtra xhlx disw yube'

    message = MIMEText(body, 'html')
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


def generate_email_body(user_data, audio_level=55):
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

    # Determine threat level and set background color
    if audio_level < 60:
        threat_message = "Minor threat detected."
        background_color = "yellowgreen"
    elif 60 <= audio_level < 75:
        threat_message = "Medium threat detected."
        background_color = "darkyellow"
    elif audio_level >= 75:
        threat_message = "Dangerous threat detected."
        background_color = "red"

    # Add threat message with background color to the email body
    # th_message = f"<div style='background-color: {background_color}; padding: 10px;'><b><font size='5'>{threat_message}</font></b></div>"

    # Construct email body
    email_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Accident Alert!</title>
        </head>
        <body>
            <h2>Accident Alert!</h2>

            <p>Dear Emergency Contact,</p>

            <p>This is to notify you that an accident may have occurred involving {user_name}.</p>

            <h3>Details of the user:</h3>
            <ul>
                <li>Name: {user_name}</li>
                <li>Email: {user_email}</li>
                <li>Phone: {user_phone}</li>
                <li>Address: {user_address}</li>
                <li>Blood Group: {user_blood_group}</li>
                <li>Treating Doctor: {user_treating_doctor}</li>
            </ul>

            <h3>Emergency Contact Information:</h3>
            <ul>
                <li>Name: {emg_name}</li>
                <li>Email: {emg_email}</li>
                <li>Phone: {emg_phone}</li>
            </ul>

            <div style='background-color: {background_color}; padding: 10px;'>
                <h3 style='font-size: 18px; font-weight: bold;'>{threat_message}</h3>
            </div>

            <p>Please take necessary actions as per the situation.</p>

            <p>Thank you.</p>

            <p>Sincerely,<br>
            Threat Detection Team</p>
        </body>
        </html>
        """
    return email_body
