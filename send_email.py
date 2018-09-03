import smtplib
import getpass

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')     # May differ if you use another email service (Yahoo, Hotmail, etc.)
        server.ehlo()                                   # Establishes a connection
        server.starttls()

        EMAIL_ADDRESS = raw_input("Enter your email: ")
        PASSWORD = getpass.getpass("Enter your password: ")     # getpass hides the password when written
        server.login(EMAIL_ADDRESS, PASSWORD)

        message = 'Subject: {}\n\n{}'.format(subject, msg)

        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")

subject = "Email from Python"
msg = "Hello from Python!"

send_email(subject, msg)
