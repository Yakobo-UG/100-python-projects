import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import ADDRESS, PASSWORD

def send_msg(sender, to, subject, body):
    msg = MIMEMultipart()
    msg["From"] = sender,
    msg["To"] = to,
    msg["Subject"] = subject,
    msg.attach(MIMEText(body, "plain"))
    s.send_message(msg)

if __name__ == "__mail__":
    s = smtplib.SMTP(host="smtp.gmail.com", port=587)
    s.starttls()
    s.login(ADDRESS, PASSWORD)

    send_msg(ADDRESS,
            "themailyouwanttosendto@gmail.com", 
            "Testing one 2", 
            "This is the body yooo")
    s.quit()






