import gspread
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from credentials import *
from datetime import datetime
import time

def EmailRunners(year):
    # Signing into service account & allowing access
    if year == 9:
        gc = gspread.service_account(filename=service_account_9_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        worksheet = sh.worksheet("YEAR9")
    elif year == 10:
        gc = gspread.service_account(filename=service_account_10_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        worksheet = sh.worksheet("YEAR10")
    elif year == 11:
        gc = gspread.service_account(filename=service_account_11_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        worksheet = sh.worksheet("YEAR11")
    elif year == 12:
        gc = gspread.service_account(filename=service_account_12_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        worksheet = sh.worksheet("YEAR12")
    elif year == 13:
        gc = gspread.service_account(filename=service_account_13_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        worksheet = sh.worksheet("YEAR13")  

    # Creating variables
    print("Creating variables...")
    now = datetime.now()  # current date and time
    date = now.strftime("%d")
    month = now.strftime("%m")
    day = now.strftime("%A")

    # Getting Values from Sheet. NOTE NUMBERS ARE 1 BASED.
    IDS = worksheet.col_values(1) 
    emails = worksheet.col_values(6)
    runner_first_names = worksheet.col_values(7)
    runner_last_names = worksheet.col_values(7)
    runner_forms = worksheet.col_values(9)

    # Delete headers from each column
    del IDS[0], emails[0], runner_first_names[0], runner_last_names[0], runner_forms[0]

    html_email = """
    <h2>Exec Newlands College Chase 2021!</h2>
    <h4>Pegs must be clipped onto the body or clothing, not bags.</h4>
    <p>To catch your runner, place a peg on them, then obtain their player ID.</p>
    <p><a href="https://sites.google.com/newlands.school.nz/nc-chase/home" target="_blank" rel="noopener">Detailed rules and more information at our website.</a></p>
    <p>Remember to keep your Player ID secret!<p>
    <p style="font-size: 1.5em;">Your Player ID is <span style="color: #ffffff; background-color: #3e3874;"><strong>{player_id}</strong></span></p>
    <p style="font-size: 1.5em;">Your Runner is <span style="color: #ffffff; background-color: #3e3874;"><strong>{runner_full_name}</strong></span>&nbsp;from&nbsp;<span style="color: #ffffff;background-color: #3e3874;"><strong>{runner_form}</strong></span></p>
    <p>When you catch your runner, get their Player ID then fill out <a href="https://forms.gle/ma3xJxzku99TfeiF8">our form.</a></p>
    <br>
    <p style="font-size:1.2em;">This email was sent automatically - for assistance, reply to this email or message us on Instagram 
    <a href="https://www.instagram.com/newlands.college.chase/">@newlands.college.chase</a></p>
    <h3>Telling a friend could be telling the enemy, so keep your lips sealed! Good luck.</h3>
    """


    message = MIMEMultipart("alternative")
    message["Subject"] = "NC Chase21 Exec -  " + day + " " + date + "/" + month
    message["From"] = "Gamemaster <gamemaster@newlands.school.nz>"
    message["To"] = "Players <NC-Chase21>"
    # message["Reply-To"] = ""


    print("Emails sending now...")

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
            runner_first_name = runner_first_names[person]
            runner_last_name = runner_last_names[person]
            runner_form = runner_forms[person]
            runner_full_name = runner_first_name + runner_last_name

            part_html = MIMEText(html_email.format(runner_form=runner_form, runner_full_name=runner_full_name,player_id=player_id), "html")

            message.attach(part_html)

            server.sendmail(email_address, receiver_email, message.as_string())

            print("Email sent to " + receiver_email)

    print(str(person + 1) + " emails sent")
