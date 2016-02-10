from openpyxl import load_workbook
wb = load_workbook('test.xlsx')
print wb.get_sheet_names()
sheet_ranges = wb['CONF SEEDING']
print (sheet_ranges['A2'].value)