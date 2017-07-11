import requests
import time

api_token = input('Enter your API token:')
headers = {
    'API-Key':api_token,
    }
main_url = 'https://api.vultr.com/v1/'

def serverCreate():
    location = input('Enter where you want your proxies located[Miami, Dallas, Seattle, Atlanta, Chicago, LA, NY, Silicon Valley, Germany, France, UK, Amsterdam, Tokyo, Sydney]:')
    numOfProxies = input('Enter number of proxies you want to deploy:')
    r = requests.get(main_url + 'startupscript/list', headers=headers)
    serverlist = []
    json = r.json()    
    for SUBID, server in json.items():
        serverlist.append(server)
        scriptData = SUBID
    
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
    data = [
      ('DCID',locale),
      ('VPSPLANID',"201"),
      ('OSID',"160"),
      ('SCRIPTID', scriptData),
      ('SUBID', "test")
    ]
    for i in range(int(numOfProxies)):
        r = requests.post(main_url + 'server/create', headers=headers, data=data)
        print(r.content)
        time.sleep(1)
def writeToFile():
    r = requests.get(main_url + 'server/list',headers=headers)
    serverlist = []
    json = r.json()
    ip = tuple(str(d['main_ip']) for d in json.values())
    lineBreak = '\n'.join('{}' + ':3128:dreamtm:1234asdf' for _ in range(len(ip))).format(*ip)
    print('\n' + 'Your proxies are: ' + '\n' + '\n' + lineBreak + '\n' + '\n' + 'Also wrote a text file, located within the vultrDeploy folder')
    file = open('vultr_proxies.txt','w')
    file.write(lineBreak)
    file.close()

def serverDestroy():
    r = requests.get(main_url + 'server/list', headers=headers)
    serverlist = []
    json = r.json()    
    for SUBID, server in json.items():
        serverlist.append(server)
        data = {
        'SUBID': SUBID,
        }
        deleted = requests.post ('https://api.vultr.com/v1/server/destroy', headers = headers, data = data)
        print ('Deleted: ' + SUBID)
        time.sleep(1)

def main():
    askMain = input('Do you want to create/destroy proxies (enter "C" or "D") or write current proxies to text file(enter "W")?')
    if askMain == 'C' or askMain == 'c':
        serverCreate()        
    elif askMain == 'D' or askMain== 'd':
        serverDestroy()
    elif askMain == 'W' or askMain =='w':
        writeToFile()
    else:
        print('You entered your something incorrectly, please enter as specified.')
        main()
    
        
if __name__ == "__main__":
    main()
