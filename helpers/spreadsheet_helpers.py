import xlsxwriter
from ui.entities.advertisement import Advertisement


def write_ads_search_result_to_excel(advertisement_list: list[Advertisement], file_name):
    with xlsxwriter.Workbook(f'./azdarar_search_results/{file_name}.xlsx') as workbook:
        worksheet = workbook.add_worksheet()

        for row_num in enumerate(advertisement_list):
            for ad in advertisement_list:
                worksheet.write_row(row_num, 1, ad.ad_date)
                worksheet.write_row(row_num, 2, ad.ad_link)
                worksheet.write_row(row_num, 3, ad.ad_text)

    workbook.close()
