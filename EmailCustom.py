import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from credentials import *
from datetime import datetime
import sys

# Creating variables
now = datetime.now()  # current date and time
date = now.strftime("%d")
month = now.strftime("%m")
day = now.strftime("%A")

# SETTING CUSTOM VARIABLES
receiver_email = "techcrew4@newlands.school.nz"
first_name = "FirstName"
last_name = "Last-Name"
reason = "Example big reason"
action = "action im gonna punish you"


# Confirming Custom Email Send
confirmation_message = "Please confirm sending custom punishment email to {receiver_email} - {first_name} {last_name}, with reason '{reason}' and action '{action}'\nY or N\n\n"
if input(confirmation_message.format(receiver_email=receiver_email,first_name=first_name,last_name=last_name,reason=reason,action=action)) != "Y":
    sys.exit()


# Setting Email Body
html_email = """
<h1><strong><span style="color: #ff0000;">Newlands College Chase 2021 Message</span></strong></h1>
<p>Dear {first_name} {last_name},</p>
<h3><span style="font-size: 16.38px;">You have been removed from the game for <span style="text-decoration: underline;">{reason}</span></span></h3>
<h3><span style="font-size: 14px;">Action taken:&nbsp;<span style="text-decoration: underline;">{action}</span></span></h3>
<p>Due to your actions, the above sanction has been put into place.</p>
<p>If you disagree or would like to appeal this, you can reach out by replying or messaging us on Instagram <a href="https://www.instagram.com/newlands.college.chase/" target="_blank" rel="noopener">@newlands.college.chase</a></p>
<p style="font-size: 1.2em;">This email was sent automatically - for assistance, reply to this email or message us on Instagram <a href="https://www.instagram.com/newlands.college.chase/" target="_blank" rel="noopener">@newlands.college.chase</a></p>

<h2><a href="https://bit.ly/NCChase" target="_blank" rel="noopener">Chase21 Website</a></h2>
"""


message = MIMEMultipart("alternative")
message["Subject"] = "Chase21 Disciplinary Action -  " + day + " " + date + "/" + month
message["From"] = "Gamemaster <gamemaster@newlands.school.nz>"
message["To"] = "Player <NC-Chase21>"

context = ssl.create_default_context() # Create Context for server

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

    server.ehlo_or_helo_if_needed() # Greet the server
    # server.starttls() # Establish Secure Connection with server
    server.login(email_address, email_password)

    part_html = MIMEText(html_email.format(first_name=first_name, last_name=last_name, action=action, reason=reason), "html")
    message.attach(part_html)
    server.sendmail(email_address, receiver_email, message.as_string())
    print("Email sent to " + receiver_email)