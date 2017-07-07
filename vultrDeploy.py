import requests
from bs4 import BeautifulSoup



api_token = input('Enter your API token:')
location = input('Enter where you want your proxies located[Miami, Dallas, Seattle, Atlanta, Chicago, LA, NY, Silicon Valley, Germany, France, UK, Amsterdam, Tokyo, Sydney]:')
numOfProxies = input('Enter number of proxies you want to deploy:')
scriptID = input('Enter your startup Script ID:')


headers = {
    'API-Key':api_token,
    }
main_url = 'https://api.vultr.com/v1/'


if location == 'Miami':
        locale = '39'
elif location == 'Dallas':
        locale = '3'	
elif location == 'Seattle':
        locale = '4'
elif location == 'Atlanta':
        locale = '6'
elif location == 'Chicago':
        locale = '2'
elif location == 'LA':
        locale = '5'
elif location == 'NY':
        locale = '1'
elif location == 'Silicon Valley':
        locale = '12'
elif location == 'Germany':
        locale = '9'
elif location == 'France':
        locale = '24'
elif location == 'UK':
        locale = '8'
elif location == 'Amsterdam':
        locale = '7'
elif location == 'Singapore':
        locale = '40'
elif location == 'Tokyo':
        locale = '25'
elif location == 'Sydney':
        locale = '19'

def serverCreate():
    data = [
      ('DCID',locale),
      ('VPSPLANID',"201"),
      ('OSID',"160"),
      ('SCRIPTID', scriptID),
      ('SUBID', "test")
    ]
    for i in range(int(numOfProxies)):
        r = requests.post(main_url + 'server/create', headers=headers, data=data)
        print(r.content + b' was just create!')


serverCreate()
