from flask import Flask, render_template, request, redirect, url_for, session
from util import *
import time

app = Flask(__name__)
app.secret_key = 'some_secure_random_key'  # For sessions

MAX_DIFF_TIME = 500
# Define Global variable to track threat IDs.
threat_ids = {
    "sample@gmail.com" : time.time()
}
# Define the route to serve the input form
@app.route('/')
def input_form():
    return render_template('index.html')

# Process form submission and store data in session
@app.route('/monitor', methods=['POST'])
def process_form():
    if not session.get('ignore_requests', False):
        session['ignore_requests'] = True
        print("Ignoring requests for the next 5 minutes.")
        time.sleep(2)  # 300 seconds = 5 minutes
        session.pop('ignore_requests', None)
        print("Now accepting requests.")

        data = request.form
        session['user_data'] = data  # Store in session
        return redirect(url_for('monitor_page'))
    else:
        return "Requests are currently being ignored. Please try again later.", 403

# # Serve the monitor.html template
# @app.route('/monitor')
# def monitor():
#     user_data = session.get('user_data')
#     if user_data:
#         print("User: ", user_data)
#         return render_template('monitor.html', user_data=user_data)
#     else:
#         return redirect(url_for('input_form')) 

# Serve the monitor.html template (renamed route)
@app.route('/monitor_page')
def monitor_page():
    user_data = session.get('user_data')
    if user_data:
        print("User: ", user_data)
        return render_template('monitor.html', user_data=user_data)
    else:
        return redirect(url_for('input_form')) 

# Handle threat detection and send email alerts
@app.route('/threat', methods=['POST'])
def handle_threat():
    print("Threat detected!")  
    user_data = session.get('user_data')
    if user_data:
        # Extract emergency contacts
        emergency_contact = user_data.get('emgEmail1', '')
        
        if emergency_contact and emergency_contact in threat_ids:
            time_diff = time.time() - threat_ids[emergency_contact]
            if   time_diff < MAX_DIFF_TIME:
                # check if current time gap is more than max diff.
                # Do not send any request for now.
                # time.sleep()
                return "Threat was send already", 200
        if emergency_contact:
            threat_ids[emergency_contact] = time.time()
            # Build email message
            subject = "Accident Alert!"
            body = generate_email_body(user_data=user_data, emergency_contact=emergency_contact)

            # Send the email
            recipients = [emergency_contact]
            try:
                send_email_alert(recipients, subject, body)
                return "Alert received", 200
            except Exception as e:
                print("Error sending email:", e)
                return "Error processing request", 500
        else:
            return "No Emergency contact", 500
    else:
        return "No user data found", 404

if __name__ == '__main__':
    app.run(debug=False)
