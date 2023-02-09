import openpyxl

def open_file():
    book = openpyxl.open('goods.xlsx')
    sheet = book.active

    lst = []
    for row in sheet.iter_rows():
        for cell in row:
            if cell.value != None:
                lst.append(cell.value)
    return lst