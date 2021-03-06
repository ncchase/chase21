import gspread
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from credentials import *
from datetime import datetime
import time

# Signing into service account & allowing access
gc = gspread.service_account(filename=service_account_9_filepath)
worksheet = gc.open_by_key("1-kFRYyEQ3QvRFi7JouYUiqkjHY6eQbivMfPFN7jPYm4")
# worksheet = gc.open_by_key(spreaadsheet_key)

# Fetching sheet
student_sheet = worksheet.worksheet("EXEC")

# Sender information & password
sender_email = email_address
sender_password = email_password

# Creating variables
print("Creating variables...")
now = datetime.now()  # current date and time
date = now.strftime("%d")
month = now.strftime("%m")
day = now.strftime("%A")
# Getting Values from Sheet. NOTE NUMBERS ARE 1 BASED.
IDS = student_sheet.col_values(1) 
emails = student_sheet.col_values(6)
runner_names = student_sheet.col_values(7)
runner_forms = student_sheet.col_values(9)

del IDS[0], emails[0], runner_names[0], runner_forms[0] # Removes headers

html_email = """
<h2>Exec Newlands College Chase 2021!</h2>
<h4>Pegs must be clipped onto the body or clothing, not bags.</h4>
<p>To catch your runner, place a peg on them, then obtain their player ID.</p>
<p><a href="https://sites.google.com/newlands.school.nz/nc-chase/home" target="_blank" rel="noopener">Detailed rules
    and more information at our website.</a></p><p>Remember to keep your Player ID secret!<p><p style="font-size: 1.5em;">Your Player ID is <span style="color: #ffffff;"><span style="background-color: #3e3874;"><strong>{player_id}</strong></span></span></p>
<p style="font-size: 1.5em;">Your Runner is <span style="color: #ffffff; background-color: #3e3874;"><strong>{runner_name}</strong></span>&nbsp;from&nbsp;<span style="color: #ffffff;background-color: #3e3874;"><strong>{runner_form}</strong></span></p>
<p>When you catch your runner, get their Player ID then fill out <a href="https://forms.gle/ma3xJxzku99TfeiF8">our 
form.</a></p>
<br>
<p style="font-size:1.2em;">This email was sent automatically - for assistance, reply to this email or message us on Instagram 
<a href="https://www.instagram.com/newlands.college.chase/">@newlands.college.chase</a></p>
<h3>Telling a friend could be telling the enemy, so keep your lips sealed! Good luck.</h3>
"""

message = MIMEMultipart("alternative")
# message["Subject"] = "NC Chase21 Exec -  " + day + " " + date + "/" + month
message["Subject"] = "NC Chase21 Exec - Friday 12/03"
message["From"] = "Gamemaster <gamemaster@newlands.school.nz>"
message["To"] = "Players <NC-Chase21>"
# message["Reply-To"] = "Anomaly Support <different-address@anomaly.net.au>"


print("Emails sending now...")

context = ssl.create_default_context() # Create Context for server.
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.ehlo_or_helo_if_needed() # Greet the server.
    # server.starttls() # Establish Secure Connection with server
    server.login(sender_email, sender_password)
    for person in range(len(emails)):
        
        if person % 30 == 0:
            time.sleep(35)

        receiver_email = emails[person]
        player_id = IDS[person]
        runner_name = runner_names[person]
        runner_form = runner_forms[person]
        part_html = MIMEText(html_email.format(runner_form=runner_form, runner_name=runner_name,player_id=player_id), "html")
        # part_plain = MIMEText(plain_email.format(runner_form=runner_form, runner_name=runner_name,player_id=player_id), "plain")
        message.attach(part_html)
        # message.attach(part_plain)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
        print("Email sent to " + receiver_email)

print(str(person + 1) + " emails sent")
