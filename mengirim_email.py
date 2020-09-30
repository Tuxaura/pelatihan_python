from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib


message = MIMEMultipart()
message["from"] = "Beben Moch. Akbar P"
message["to"] = "bebenx@gmail.com"
message["subject"] = "Ini adalah isi pesan email"
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("python.jpg").read_bytes()))

# smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
# smtp.close()

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("bebenx@gmail.com", "")
    smtp.send_message(message)
    print("sent")
