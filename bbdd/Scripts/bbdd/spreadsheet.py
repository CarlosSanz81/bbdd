import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Copia de **BBDD**").sheet1
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)

final = sheet.row_count #Cuenta la ultima fila

sheet.delete_row(final-2) #borrar la fila indicada