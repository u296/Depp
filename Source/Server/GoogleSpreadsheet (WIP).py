import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('yeet-da172c05274a.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('Automatic Mod Installer Project').sheet1


#vv this prints the existing spreadsheet information into python
#print(wks.get_all_records())


#vv this gives the spreadsheet information
#while True:
#    wks.append_row([input()])
    
#vv this prints existing spreadsheet information in chosen cell into python
result = wks.cell(input('Row: '),input('Column: ')).value

print(result)
