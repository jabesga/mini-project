import sys
import ctypes # An included library with Python install.
import xlrd
import csv
import os

FILE_TO_CONVERT = ''
NAME_OF_CSV_FILE = ''
SKIP_FIRST_ROW = True
FOR_TYNKER = True

FIRST_NAME_COLUMN_NUMBER = 6 # START WITH 0 # FIRST_NAME
LAST_NAME_COLUMN_NUMBER = 7

def main():
    if len(sys.argv) < 2:
        ctypes.windll.user32.MessageBoxA(0, "You must drop a file into the executable", "XLS to CSV converter", 0x10 | 0x0)
        sys.exit(0)
    else:
        global FILE_TO_CONVERT
        global NAME_OF_CSV_FILE
        FILE_TO_CONVERT = sys.argv[1]
        NAME_OF_CSV_FILE = sys.argv[1] + '_CSV.csv'
    
    wb = xlrd.open_workbook(FILE_TO_CONVERT)
    sheet = wb.sheet_by_index(0) # first sheet

    destination_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), NAME_OF_CSV_FILE)
    csv_file = open(destination_path, 'wb')

    #######################################################

    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    if SKIP_FIRST_ROW:
        if FOR_TYNKER:
            wr.writerow(['first', 'last', 'login', 'password'])

    for row in xrange(SKIP_FIRST_ROW, sheet.nrows):
        if FOR_TYNKER:

            # Login is the firstname+lastname
            # Password is the firstname
            row_info = sheet.row_values(row)
            first_name = row_info[FIRST_NAME_COLUMN_NUMBER].encode('utf-8')
            last_name = row_info[LAST_NAME_COLUMN_NUMBER].encode('utf-8')
            student_data = [
                            first_name,
                            last_name,
                            first_name+last_name,
                            first_name
                            ]

            wr.writerow(student_data)
        else:
            wr.writerow(sheet.row_values(row))

    #######################################################

    csv_file.close()

    ctypes.windll.user32.MessageBoxA(0, "File converted successfully", "XLS TO CSV Converter", 0x40 | 0x0)


if __name__ == '__main__':
    main()