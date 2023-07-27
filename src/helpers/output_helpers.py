import logging
from ui.entities.advertisement import Advertisement
import os


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
