import xlsxwriter

def write_to_excel(list):
    with xlsxwriter.Workbook('azdarar_search_results.xlsx') as workbook:
        worksheet = workbook.add_worksheet()

        for row_num, data in enumerate(list):
            worksheet.write_row(row_num, 0, data)
