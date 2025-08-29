import smtplib
from email.mime.text import MIMEText

# Sender ane receiver email addresses
sender_email = "youremail@gmail.com"
receiver_email = "receiveremail@example.com"

# Email subject ane body
subject = "Test Mail from Python"
body = "Hello, aa email Python thi moklaya che!"

# Email object prepare karo
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

# SMTP server par connect karo
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()  # Secure connection
    # Login karo (tamaari Gmail ID ane password ya app password)
    server.login(sender_email, 'yourpassword')  
    
    # Email send karo
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("Email successfully sent!")
