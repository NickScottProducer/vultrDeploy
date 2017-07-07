import requests
from bs4 import BeautifulSoup
import installModules


api_token = input('Enter your API token:')

headers = {
    'API-Key':api_token,
    }
main_url = 'https://api.vultr.com/v1/'


f = open('startup.txt','r')
if f.mode == 'r':
    contents = f.read()
data = [
        ('name','script'),
        ('script',contents)
        ]
re = requests.post(main_url + 'startupscript/create',headers=headers,data=data)
soup = BeautifulSoup(re.content, 'html.parser')
print(soup)
print('Save this number somewhere for later use!')
print('You will not have to run this program again, unless you forget this number.')
print('If you do forget this number, simply run this program again and brand the number into your skin.')
print('Now run the vultrDeploy.py program')
