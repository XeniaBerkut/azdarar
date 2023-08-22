import html
import logging
import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from helpers.test_data_helpers import get_test_data_from_json
from ui.entities.advertisement import Advertisement
import os

from ui.tests.conftest import logger
import smtplib


def create_directory_for_results(output_folder):
    logging.info('Check if directory for output exist and create if not')
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)


def write_ads_search_result_to_html(advertisement_list: list[Advertisement], file_name, output_folder):
    create_directory_for_results(output_folder)
    advertisement_list_html_file_path = output_folder + file_name + '.html'
    ads_html_file = open(advertisement_list_html_file_path, "w", encoding="utf-8")
    ad_number = 1
    html_text = """
    <html>
        <head>
            <title> Azdarar Smart Search </title>
        </head>
        <body>
        """
    for ad in advertisement_list:
        html_text += f"""
        <h1 style="background-color:#00b8e6;">{ad_number}. Search string <b>{ad.ad_search_string}</b>
        <br>
            <a href="{ad.ad_link}">{ad.ad_link}</a>
            <br>
        </h1>
        <br>
        <h2>{ad.ad_text}</h2>
        <br>
        """
        ad_number += 1
    html_text += """
        </body>
    </html>
    """
    ads_html_file.write(html_text)
    ads_html_file.close()


def create_email_body(email_body: list):
    html_table = "<table>\n"

    for dictionary in email_body:
        html_table += f"  <tr>"
        for key, value in dictionary.items():
            escaped_value = html.escape(str(value))
            html_table += f"<td>{escaped_value}</td>"
        html_table += f"</tr>\n"

    html_table += "</table>"
    return html_table


def send_email(data_folder_path: str, attachments_directory_path: str, email_body_data: list, search_date_depth: int):
    logger.info("Set up the email message")
    email_data = get_test_data_from_json(os.path.join(data_folder_path, "secrets.json"))
    message = MIMEMultipart("alternative")
    message["Subject"] = ("Azdarar Digest: " + start_searching_date(search_date_depth) +
                          " - " + datetime.datetime.now().strftime("%Y-%m-%d"))
    message["From"] = email_data["from_email"]
    message["To"] = email_data["to_email"]

    logger.info("Prepare and attach HTML content")
    email_body_html = MIMEText(create_email_body(email_body_data), "html")
    message.attach(email_body_html)

    logger.info("Attach files")
    for attachment_path in os.listdir(attachments_directory_path):
        full_path = os.path.join(attachments_directory_path, attachment_path)
        with open(full_path, "rb") as attachment:
            attachment_data = attachment.read()
            attachment_name = attachment_path.split("/")[-1]  # Extract the filename
            attachment_part = MIMEApplication(attachment_data)
            attachment_part.add_header("Content-Disposition", f"attachment; filename={attachment_name}")
            message.attach(attachment_part)

    logger.info("Send the email using Gmail's SMTP server")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = email_data["from_email"]
    smtp_password = email_data["token"]

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)


def start_searching_date(search_date_depth):
    current_date = datetime.datetime.now()
    days_before = datetime.timedelta(days=search_date_depth)
    date_10_days_ago = current_date - days_before
    return date_10_days_ago.strftime("%Y-%m-%d")
