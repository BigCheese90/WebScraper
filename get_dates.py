import requests
from bs4 import BeautifulSoup
from Firmenneugründungen import Download_daily_data
from requests.auth import HTTPBasicAuth
import pandas as pd
url = 'https://www.unternehmen24.info/Firmenbuch/%C3%96sterreich/Neueintragungen/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
dates = soup.find_all("option")

apiurl = "https://mai.allnet.de/api/v1/add-company"
headers = {'Accept': 'application/json', "api-key": "FjJy2hTZN1IuvGdSjJyI1jnRskWQOfF2" }
auth = HTTPBasicAuth('api-key', 'FjJy2hTZN1IuvGdSjJyI1jnRskWQOfF2')

Already_Downloaded_Dates = open("AlreadyDownloadedDates.txt", "r+")
datelist = Already_Downloaded_Dates.read().split()

k=0
for date in dates:

    date = date.get_text()
    date = date[6:] +"-" +date[3:5] + "-" +date[0:2]
    if date not in datelist:
        k = k + 1
        if k > 5:
            break
        print("Downloading: ",date)

        DF = Download_daily_data(date)
        for i in range(len(DF)):
            b = DF.iloc[i].to_dict()
            req = requests.post(apiurl, headers=headers, json=b)
        datelist.append(date)


for d in datelist:
    Already_Downloaded_Dates.write("%s\n" %d)

Already_Downloaded_Dates.close()
print("Done")