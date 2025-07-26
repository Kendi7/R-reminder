import os
import smtplib
import datetime
import calendar
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# Get today's date and last day of the month
today = datetime.date.today()
last_day = calendar.monthrange(today.year, today.month)[1]
reminder_day = last_day - 7

# --- FOR TESTING: Force send regardless of the date ---
force_send = True  # Set to False in production

if not force_send and today.day != reminder_day:
    print(f"📅 Not the reminder day ({today}). Will run again tomorrow.")
    sys.exit()
else:
    print(f"📨 Forcing send... (Today's date: {today})")

# Prepare email content
subject = "🏠 Rent Reminder [Test Mode]"
body = f"""Hello,

This is a friendly reminder that your rent is due in 7 days — on {today.replace(day=last_day).strftime('%B %d')}.

Please make sure to pay your rent on time.

Thanks!
- Your Python Script 🤖
"""

# Build and send email
msg = MIMEMultipart()
msg["From"] = EMAIL_ADDRESS
msg["To"] = TO_EMAIL
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, TO_EMAIL.split(","), msg.as_string())
    server.quit()
    print("✅ Rent reminder sent successfully (Test Mode).")
except Exception as e:
    print(f"❌ Error sending email: {e}")
