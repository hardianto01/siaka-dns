from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

print('                                                   made by: ')
print('\n\n')
print('                     ██╗  ██╗  █████╗  ██████╗  ██████╗  ██╗  █████╗  ███╗   ██╗ ████████╗  ██████╗')
print('                     ██║  ██║ ██╔══██╗ ██╔══██╗ ██╔══██╗ ██║ ██╔══██╗ ████╗  ██║ ╚══██╔══╝ ██╔═══██╗')
print('                     ███████║ ███████║ ██████╔╝ ██║  ██║ ██║ ███████║ ██╔██╗ ██║    ██║    ██║   ██║')
print('                     ██╔══██║ ██╔══██║ ██╔══██╗ ██║  ██║ ██║ ██╔══██║ ██║╚██╗██║    ██║    ██║   ██║')
print('                     ██║  ██║ ██║  ██║ ██║  ██║ ██████╔╝ ██║ ██║  ██║ ██║ ╚████║    ██║    ╚██████╔╝')
print('                     ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═════╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═══╝    ╚═╝     ╚═════╝')
print('\n\n')

print('Inspek Nilai Siaka Kalian Sekarang')
email = int(input('Masukan NIM: '))
pasw = input('Masukan password: ')

payLoad = {
        'email': email,
        'pasw': pasw,
        'juser': 'MHS'
    }

def getCookie():
    
    data = requests.post('https://siaka.undipa.ac.id/index.php?page=login&aksi=masuk', data=payLoad)
    return data.headers['Set-Cookie']

def getDns():
    headers = {
        'cookie': getCookie()
    }
    data = requests.get('https://siaka.undipa.ac.id/index.php?page=dns', headers=headers)
    soup = BeautifulSoup(data.content, 'html.parser')
    datas = []
    table = soup.find_all("table")[2]
    for row in table.find_all("tr"):
        row_data = [cell.get_text(strip=True).replace("\t", " ") for cell in row.find_all(["td"])]
        datas.append(row_data)
    for i in range(len(datas)):
        if (i == 4): continue
        if (i == 21): continue
        else: 
            print(' '.join(datas[i]))

getDns()