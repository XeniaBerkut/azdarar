import xlsxwriter
from ui.entities.advertisement import Advertisement


def write_ads_search_result_to_excel(advertisement_list: list[Advertisement], file_name):
    with xlsxwriter.Workbook(f'./azdarar_search_results/{file_name}.xlsx') as workbook:
        worksheet = workbook.add_worksheet()

        # for row_num, ad in enumerate(advertisement_list):
        #     worksheet.write_row(row_num, 1, ad.ad_date)
        #     worksheet.write_row(row_num, 2, ad.ad_link)
        #     worksheet.write_row(row_num, 3, ad.ad_text)
        row_num = 1
        for ad in advertisement_list:
            worksheet.write_row(row_num, 1, ad.ad_date)
            worksheet.write_row(row_num, 2, ad.ad_link)
            worksheet.write_row(row_num, 3, ad.ad_text)
            row_num += 1

    workbook.close()


def write_ads_search_result_to_html(advertisement_list: list[Advertisement], file_name):
    ads_html_file = open(f"./azdarar_search_results/{file_name}.html", "w", encoding="utf-8")
    ad_number = 1
    for ad in advertisement_list:
        ads_html_file.write(f'<html>\n<head>\n<title> \n \
               </title>\n</head> <body><h1 style="background-color:DodgerBlue;">{ad_number}. Search string for {ad.ad_type} TODO <br> <a href="{ad.ad_link}">{ad.ad_link}</a> <br></h1>\
               \n<h2> {ad.ad_text}</u> </h2> <br> \n</body></html>')
        ad_number += 1
    ads_html_file.close()
