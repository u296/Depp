import gspread
from oauth2client.service_account import ServiceAccountCredentials

def gspreadInit():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('GoogleCredentials.json', scope)

    googleCredentials = gspread.authorize(credentials)
    global mainWorkSheet
    mainWorkSheet = googleCredentials.open('Automatic Mod Installer Project').sheet1

def getCell(row: int, collumn: int):
    return mainWorkSheet.cell(row, collumn)

def findCell(query: str):
    return mainWorkSheet.find(query)

def findAllCells(query: str):
    return mainWorkSheet.findall(query)

def writeCell(row: int, collumn: int, content: str):
    mainWorkSheet.update_cell(row, collumn, content)

def writeFoundCell(query: str, content: str):
    cell = mainWorkSheet.find(query)
    mainWorkSheet.update_cell(cell.row, cell.col, content)

if __name__ == "__main__": 
    gspreadInit()
    findCell("ye")
