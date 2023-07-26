import xlsxwriter
from ui.entities.advertisement import Advertisement
import os


def create_directory_for_results(output_folder, parent_folder):
    if not os.path.isdir(parent_folder):
        os.mkdir(parent_folder)
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)


def convert_ads_to_list_of_lists(advertisement_list):
    list_of_lists = []
    for ad in advertisement_list:
        temp = [ad.ad_date, ad.ad_link, ad.ad_text]
        list_of_lists.append(temp)
    return list_of_lists


def write_ads_search_result_to_excel(advertisement_list: list[Advertisement],
                                     file_name, output_folder):
    output_folder_excel = output_folder + 'excel/'
    create_directory_for_results(output_folder_excel, output_folder)
    advertisement_list_xlsx_file_path = output_folder_excel + file_name + '.xlsx'
    with xlsxwriter.Workbook(advertisement_list_xlsx_file_path) as workbook:
        worksheet = workbook.add_worksheet()
    converted_ads_list = convert_ads_to_list_of_lists(advertisement_list)
    for row_num, data in enumerate(converted_ads_list):
        worksheet.write_row(row_num, 0, data)
    workbook.close()


def write_ads_search_result_to_html(advertisement_list: list[Advertisement], file_name, output_folder):
    output_folder_html = output_folder + 'html/'
    create_directory_for_results(output_folder_html, output_folder)
    advertisement_list_html_file_path = output_folder_html + file_name + '.html'
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
