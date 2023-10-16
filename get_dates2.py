import requests
from bs4 import BeautifulSoup
from get_companies import get_daily_Data
from requests.auth import HTTPBasicAuth
from Openvpn import close_vpn
from Openvpn import change_vpn
import os
import pandas as pd
url = 'https://www.unternehmen24.info/Firmenbuch/%C3%96sterreich/Neueintragungen/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
dates = soup.find_all("option")

apiurl = "https://mai.allnet.de/api/v1/add-company"
apiheaders = {'Accept': 'application/json', "api-key": "FjJy2hTZN1IuvGdSjJyI1jnRskWQOfF2" }
auth = HTTPBasicAuth('api-key', 'FjJy2hTZN1IuvGdSjJyI1jnRskWQOfF2')

Already_Downloaded_Dates = open("AlreadyDownloadedDates.txt", "r+")
datelist = Already_Downloaded_Dates.read().split()
datetracker = open("NewDates.txt", "r+")
k=0
for date in dates:

    date = date.get_text()
    date = date[6:] +"-" +date[3:5] + "-" +date[0:2]
    if date not in datelist:
        k = k + 1
        print(date)
        if k > 10:
            break
        change_vpn()
        DF = get_daily_Data(date)
        close_vpn()
        for i in range(len(DF)):
            b = DF.iloc[i].to_dict()
            req = requests.post(apiurl, headers=apiheaders, json=b)
        os.chdir('C:\\Users\\Jakob Wien\\PycharmProjects\\WEbScraper')
        datetracker.write("%s\n" % date)
        datelist.append(date)



for d in datelist:
    Already_Downloaded_Dates.write("%s\n" %d)


newlist =[]
for d in datelist:
    if d not in newlist:
        newlist.append(d)



Already_Downloaded_Dates.close()
datetracker.close()
print("Done")