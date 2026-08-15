import smtplib
from email.message import EmailMessage

# -------------------------------------------------
# Function     : send_mail
# Description  : Sends email using Gmail SMTP server
# -------------------------------------------------

def send_mail(sender, app_password, receiver, subject, body):

    # Step 1 : Create Email object
    msg = EmailMessage()

    # Step 2 : Set mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Step 3 : Add mail body
    msg.set_content(body)

    # Step 4 : Create SMTP SSL connection
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Step 5 : Login using Gmail + App password
    smtp.login(sender, app_password)

    # Step 6 : Send the email
    smtp.send_message(msg)

    # Step 7 : Close connection
    smtp.quit()


# -------------------------------------------------
# Function : main
# Description : Driver code
# -------------------------------------------------

def main():

    sender_email = "bhosaleat11@gmail.com"
    app_password = "____-____-____-____"              # Enter the passsowrd from Google Account Security settings.
    receiver_email = "xyz@gmail.com"                  # You can Enter Targeted Mail ID

    subject = "Test Mail from Python Script"

    body = """Jay Ganesh,
    This is a test email sent using Marvellous Python.
    Regards,
    Atharv Bhosale"""

    send_mail(sender_email, app_password, receiver_email, subject, body)
    print("Mail Sent Successfully")


# -------------------------------------------------
# Program Entry Point
# -------------------------------------------------
if __name__ == "__main__" :
    main()
