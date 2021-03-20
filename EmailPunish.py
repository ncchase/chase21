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
info = RetrievePlayerInfo.Retrieveinfo()
# TODO do something with info variable to get variables for sending.
# NOTE See line 40 in EmailRunners.py



# Setting Email Body
html_email = """
example email. Your name is {first_name} {last_name} and your ID is {player_id}
"""


message = MIMEMultipart("alternative")
message["Subject"] = "Chase21 TESTING -  " + day + " " + date + "/" + month
message["From"] = "Gamemaster <gamemaster@newlands.school.nz>"
message["To"] = "Players <NC-Chase21>"
# message["Reply-To"] = ""

context = ssl.create_default_context() # Create Context for server

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

    server.ehlo_or_helo_if_needed() # Greet the server
    # server.starttls() # Establish Secure Connection with server
    server.login(email_address, email_password)

    for person in range(len(emails)):
        
        if person % 30 == 0:
            time.sleep(31)

        receiver_email = emails[person]
        player_id = IDS[person]
        first_name = first_names[person]
        last_name = last_names[person]

        part_html = MIMEText(html_email.format(player_id=player_id, first_name=first_name, last_name=last_name), "html")
        message.attach(part_html)
        server.sendmail(email_address, receiver_email, message.as_string())
        print("Email sent to " + receiver_email)