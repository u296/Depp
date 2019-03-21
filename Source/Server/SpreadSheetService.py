import gspread
from oauth2client.service_account import ServiceAccountCredentials
mainWorkSheet = []
def gspreadInit:
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('yeet-da172c05274a.json', scope)

    googleCredentials = gspread.authorize(credentials)

    mainWorkSheet = googleCredentials.open('Automatic Mod Installer Project').sheet1

def getCell(row: int, collumn: int):
    try:
        return mainWorkSheet.cell(row, collumn)
    except Exception as e:
        return False

def findCell(query: str):
    try:
        return mainWorkSheet.find(query)
    except Exception as e:
        return False

def writeCell(row: int, collumn: int, content: str):
    try:
        mainWorkSheet.cell(row, collumn).value = content
        return True
    except Exception as e:
        return False

def writeFoundCell(query: str, content: str):
    try:
        mainWorkSheet.find(query).value = content
        return True
    except Exception as e:
        return False
