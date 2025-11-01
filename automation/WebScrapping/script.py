import os
import requests  # http requests
import smtplib  # email sending
import datetime  # date and time
from bs4 import BeautifulSoup  # web scraping
from email.mime.multipart import MIMEMultipart  # email structure
from email.mime.text import MIMEText  # email content

now = datetime.datetime.now()

# email content placeholder
content = ""


# extracting news stories
def extract_news(url):
    print("Extracting News Stories...")
    cnt = ""
    cnt += "<b>HN Top Stories:</b>\n" + "<br>" + "-" * 50 + "<br>"

    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    for i, tag in enumerate(
        soup.find_all("td", attrs={"class": "title", "valign": ""})
    ):
        cnt += (
            (str(i + 1) + " :: " + tag.text + "\n" + "<br>")
            if tag.text != "More"
            else ""
        )
    return cnt


cnt = extract_news("https://news.ycombinator.com/")
content += cnt
content += "<br>------------------------------------<br>"
content += "<br><br>End of Message"


# email configuration
print("Composing Email...")

# Load environment variables from a .env file if available. This uses python-dotenv
# when installed, otherwise falls back to a simple .env parser.
try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    # simple .env fallback: set environment vars if .env exists next to this script
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    k, v = line.split("=", 1)
                    # only set if not already present
                    os.environ.setdefault(k.strip(), v.strip())

# Email configuration (loaded from environment)
SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")  # SMTP server
PORT = int(os.getenv("SMTP_PORT", 587))  # SMTP port
FROM = os.getenv("EMAIL_FROM")
TO = os.getenv("EMAIL_TO")
PASSWORD = os.getenv("EMAIL_PASSWORD")  # app password

if not all([FROM, TO, PASSWORD]):
    raise RuntimeError(
        "Missing email configuration: ensure EMAIL_FROM, EMAIL_TO and EMAIL_PASSWORD are set in environment or in a .env file"
    )

msg = MIMEMultipart()

msg["From"] = FROM
msg["To"] = TO
msg["Subject"] = (
    "Top News Stories HN [Automated Email] "
    + str(now.day)
    + "-"
    + str(now.month)
    + "-"
    + str(now.year)
)

msg.attach(MIMEText(content, "html"))

print("Initializing Server...")

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()

server.login(FROM, PASSWORD)
server.sendmail(FROM, TO, msg.as_string())

print("Email sent successfully!")

server.quit()

# sending the email
print("Sending Email...")
