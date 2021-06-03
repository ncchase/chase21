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

        for years in range(9,13):

            sheet = sh.worksheet("YEAR" + str(years) + "_REMOVED")
            sheet_data = sheet.get_all_values()[1:]

            for student in sheet_data:

                html_email = """

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

                        part_html = MIMEText(html_email.format(runner_form=runner_form, runner_first_name=runner_first_name, runner_last_name=runner_last_name, player_id=player_id), "html")

                        message.attach(part_html)

                        server.sendmail(email_address, receiver_email, message.as_string())

                        # print("Email sent to " + receiver_email)
                # print(str(person + 1) + " emails sent")
                Logging.complete("EmailRunners.py", year, str(person+1) + " emails sent")


if __name__ == "__main__":

    EmailCaught()