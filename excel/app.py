import xlrd

# Give the location of the file
loc = ("Book1.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

print("0,0 content value: ", sheet.cell_value(0, 0))
print("Number of rows: ", sheet.nrows)
print("Number of cols: ", sheet.ncols)
print("Extracting all columns name")
for i in range(sheet.ncols):
    print(i, ": ", sheet.cell_value(0, i))
print("Extract first column")
for i in range(sheet.nrows):
    print(i, ": ", sheet.cell_value(i, 0))
print("Extract First column")
print(sheet.row_values(1))
