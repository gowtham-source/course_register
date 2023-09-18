import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr
from pathlib import Path
from email.mime.application import MIMEApplication
# ... (your other code remains the same)
PORT = 587
# Adjust server address, if you are not using @outlook
EMAIL_SERVER = "smtp-mail.outlook.com"

# Load the environment variables
current_dir = Path(__file__).resolve(
).parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
# load_dotenv(envars)

# Read environment variables
sender_email = 'skillsforu@outlook.com'
password_email = 'Gowtham12345@'


def send_email(name, receiver_email):
    # Create the multipart message
    msg = MIMEMultipart()
    msg["Subject"] = "Thankyou for Registering a Powerbi Course!"
    msg["From"] = formataddr(("SkillsForU.com", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    # Load and attach the HTML template
    with open('index.html', 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
        # print(html_content)
        html_content = html_content.replace("{name}", name)
        html_part = MIMEText(html_content, 'html')
        msg.attach(html_part)

    # Attach images using Content-ID (CID) to reference them in the HTML
    # image_folder = 'images'
    # for image_file in os.listdir(image_folder):
    #     with open(os.path.join(image_folder, image_file), 'rb') as image:
    #         # Determine the MIME subtype based on the file extension
    #         file_extension = os.path.splitext(image_file)[1].lstrip('.')  # Get the file extension without the dot

    #         # Create the MIMEImage with the specified subtype
    #         image_data = MIMEImage(image.read(), _subtype=file_extension)
    #         # Use the same identifier in the Content-ID as in the HTML src attribute
    #         image_data.add_header('Content-ID', f'<{image_file}>')
    pdf_filename = '2-Day-Power-Training-brochure-1.pdf'
    with open(pdf_filename, 'rb') as pdf_file:
        pdf_data = MIMEApplication(pdf_file.read(), _subtype='pdf')
        pdf_data.add_header('Content-Disposition', f'attachment; filename="{pdf_filename}"')
        msg.attach(pdf_data)

    try:
        with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
            server.starttls()
            server.login(sender_email, password_email)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Email sending failed:", str(e))

# if __name__ == "__main__":
#     send_email(
#         name="Gowtham",
#         receiver_email="gowthammathi2507@gmail.com"
#     )
