import openpyxl
try:
    # loading and opening the excel workbook,
    workbook = openpyxl.load_workbook('website/static/dictionary.xlsx')  # esnsure this script is in the same directory as your excel file

    workbook_sheetName=workbook['Sheet1']
    print(workbook_sheetName)
    for row in workbook_sheetName.iter_rows(min_row=4, max_row=30, values_only=True): # iterating through the rows available, assuming you have headers
        word, meaning= row[0], row[1]
        print(word, meaning)

    #  workbook_dictionary= workbook['Sheet1'] # the sheetname containing your data
except FileNotFoundError as error:
    print(f'{error} file not found, check the name or path of the file')
