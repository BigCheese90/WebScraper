import pandas as pd
import requests
from bs4 import BeautifulSoup
from Firmeninformationen_neu import extract_company_info
from random import randint
from random import random
from time import sleep
from Openvpn import change_vpn
import os

def get_daily_Data(date):
    url = "https://www.unternehmen24.info/Firmenbuch/%C3%96sterreich/Neueintragungen/"+ date
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    links= soup.find_all("a", href=True)

    file_path = "Company Data\\" + date + ".csv"
    if os.path.exists(file_path):
        DF = pd.read_csv(file_path, sep=";")

    else:
        DF = pd.DataFrame()

    for link in links:
        link2 = link.get("href")
        if "/Firmeninformationen/Österreich/Firma" in link2:
            if random()<=0.1:
                change_vpn()
            try:
                Company_Data = extract_company_info(link2)
                print(Company_Data[3])
                Company_Data = pd.DataFrame(Company_Data).T
                DF = pd.concat([DF, Company_Data])
            except Exception as error:
                print("ERROR!!! An exception occured: ", error)
            sleep(randint(5, 25))

    DF.columns = ["published_at", "trade_register_number","county_court", "company", "city", "postal_code", "street", "share_capital", "business_purpose", "primary_branch", "managing_directors", "short_info_file", "info_file", "short_info_url", "info_url"]
    DF.to_csv(file_path, sep=";", index=False)
    return DF

