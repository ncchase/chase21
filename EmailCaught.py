import gspread
from credentials import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from credentials import *
from datetime import datetime
import time
import Logging

def EmailCaught():
    # Signing into service account & allowing access
        gc = gspread.service_account(filename=service_account_11_filepath)
        sh = gc.open_by_key(spreadsheet_key)
        # worksheet = sh.worksheet("YEAR9")

        # Creating variables for tiem and date (these go in the subject of the email)
        print("Creating variables...")
        now = datetime.now()  # current date and time
        date = now.strftime("%d")
        month = now.strftime("%m")
        day = now.strftime("%A")

        for year in range(9,13):
            
            # Retrieving sheet and putting it into an array
            sheet = sh.worksheet("YEAR" + str(year) + "_REMOVED")
            sheet_data = sheet.get_all_values()[1:]

            if len(sheet_data) != 0:

                # for student in sheet_data:

                html_email = """
                <h1><strong>Newlands College Chase 2021 <span style="color: #ff0000;">Caught Notice</span></strong></h1>
                <h4>Sadly, for you, the game is over... You have been caught by your Chaser...</h4>
                <p>You will no longer receive a runner, or have someone chasing you. However, you can still help your house, or participate in other Chase21 Events!</p>
                <p>If you disagree or have any questions, you can reach out by replying or messaging us on Instagram <a href="https://www.instagram.com/newlands.college.chase/" target="_blank" rel="noopener">@newlands.college.chase</a></p>
                <i>Your battle was a fierce one, one of deception, one of wit, one that sadly, <strong>you lost.</strong></i>
                <p style="font-size: 1.2em;">This email was sent automatically - for assistance, reply to this email or message us on Instagram <a href="https://www.instagram.com/newlands.college.chase/" target="_blank" rel="noopener">@newlands.college.chase</a></p>
                <h2><a href="https://bit.ly/NCChase" target="_blank" rel="noopener">Chase21 Website</a></h2>
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

                    # print(email_address, email_password, "email details")
                    server.login(email_address, email_password)
                    
                    # counter creation so that the script pauses for 30 seconds every 30 emails it sends.
                    counter = 0

                    for student in sheet_data:
                        
                        if counter % 30 == 0:
                            time.sleep(31)

                        # Retrieving email of recipient & that persons ID.
                        receiver_email = student[3]
                        player_id = student[0]

                        # Creating, attaching and sending the email
                        part_html = MIMEText(html_email.format(player_id=player_id), "html")
                        message.attach(part_html)
                        server.sendmail(email_address, receiver_email, message.as_string())

                        # Increasing counter by one
                        counter += 1

                # print(str(person + 1) + " emails sent")

                # Send logging message that an email has been sent.
                Logging.complete("EmailRunners.py", year, str(counter) + " email(s) sent")
            
            else:
                # Loggin message if there are no players removed
                Logging.complete("EmailRunners.py", year, "0 emails sent")

if __name__ == "__main__":

    EmailCaught()