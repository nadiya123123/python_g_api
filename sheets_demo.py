# python code to read a google sheet file using Gspread library
import gspread

from oauth2client.service_account import ServiceAccountCredentials

myscope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
mycred = ServiceAccountCredentials.from_json_keyfile_name('credentials.json',myscope)

client =gspread.authorize(mycred)

#open the file

mysheet = client.open("countries").sheet1

list_of_row = mysheet.get_all_records()
row1 = mysheet.row_values(1)
print("List of countries:")
print(list_of_row)
print("The first country:")
print(row1)