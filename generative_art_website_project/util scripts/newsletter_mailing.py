import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "New exciting stuff we wanted you to know about The Gallery of Computation"
sender_email = "raunitxgenerativeart@gmail.com"
receiver_email = "raunit88@gmail.com"
password = input("Type your password and press enter:")

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
html = """\
<html>
  <head></head>
  <body>
    <div style="width: 80%; justify-content: center; align-text: center;">
    <img src="https://github.com/raunit-x/Generative-Art-Gallery/blob/master/images/ezgif.com-gif-maker.gif?raw=true"
             alt="A cool gif">
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
    <h6>You are seeing this message because you had subscribed to our newsletter.</h6>
    <h6>Want to unsubscribe? <a href="#">Click Here</a></h6>
    </div>
  </body>
</html>
"""
message.attach(MIMEText(html, "html"))

text = message.as_string()

# Log in to server using secure context and send email

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
