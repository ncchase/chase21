import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from credentials import *
from datetime import datetime
import time
import RetrievePlayerInfo

# Creating variables
now = datetime.now()  # current date and time
date = now.strftime("%d")
month = now.strftime("%m")
day = now.strftime("%A")

# Getting values of user info(s)
print("Who do you want to punish?")
info = RetrievePlayerInfo.Retrieveinfo()

reason_input = int(input("Remove Reason?\n1. Breaking School Rules\n2. Cheating\n3. Custom Message\n"))
if reason_input == 1:
    reason = "Breaking School Rules"
elif reason_input == 2:
    reason = "Cheating"
elif reason_input == 3:
    reason = input("Input custom reason message:\n")

action_input = int(input("Action?\n1. Disqualification from game\n2. Disqualification from game & Form Class penalty\n3. Warning\n4. Custom Message\n"))
if action_input == 1:
    action = "Disqualification from game"
elif action_input == 2:
    action = "Disqualification from game & Form Class penalty"
elif action_input == 3:
    action = "Warning"
elif action_input == 4:
    action = input("Input custom action message\n")


# Setting Email Body
html_email = """
<h1><strong><span style="color: #ff0000;">Newlands College Chase21 Message</span></strong></h1>
<p>Dear {first_name} {last_name},</p>
<h3><span style="font-size: 16.38px;">You have been removed from the game for <span style="text-decoration: underline;">{reason}</span></span></h3>
<h3><span style="font-size: 14px;">Action taken:&nbsp;<span style="text-decoration: underline;">{action}</span></span></h3>
<p>Due to your actions, the above sanction has been put into place.</p>
<p>If you disagree or would like to appeal this, please reply to this email.</p>
<p style="font-size: 1.2em;">This email was sent automatically - for assistance, reply to this email or message us on Instagram <a href="https://www.instagram.com/newlands.college.chase/">@newlands.college.chase</a></p>
"""


message = MIMEMultipart("alternative")
message["Subject"] = "Chase21 Disciplinary Action -  " + day + " " + date + "/" + month
message["From"] = "Gamemaster <gamemaster@newlands.school.nz>"
message["To"] = "Player <NC-Chase21>"
# message["Reply-To"] = ""

context = ssl.create_default_context() # Create Context for server

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

    server.ehlo_or_helo_if_needed() # Greet the server
    # server.starttls() # Establish Secure Connection with server
    server.login(email_address, email_password)

    for person in range(len(info)):
        
        if person % 30 == 0 and person != 0:
            time.sleep(31)

        # List within info list in format [ID, FirstName, LastName, Email, FormClass, House]
        first_name = info[person][1]
        last_name = info[person][2]
        receiver_email = info[person][3]
        # receiver_email = "techcrew4@newlands.school.nz" #TESTING LINE

        part_html = MIMEText(html_email.format(first_name=first_name, last_name=last_name, action=action, reason=reason), "html")
        message.attach(part_html)
        server.sendmail(email_address, receiver_email, message.as_string())
        print("Email sent to " + receiver_email)

print(str(person + 1) + " emails sent")
