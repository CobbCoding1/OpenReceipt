from openpyxl import load_workbook

workbook = load_workbook('hello_world.xlsx')
sheet = workbook.active

num = 0

sheet['A2'] = 'test'
print(sheet['A'])
for row in sheet['A']:
    num += 1
sheet['A' + str(num+1)] = 'wasd'

def temp():
    workbook = Workbook()
    sheet = workbook.active

    sheet['A1'] = 'Date'
    sheet['B1'] = 'Total'
    sheet['C1'] = 'Store'

    workbook.save(filename='receipts.xlsx')
