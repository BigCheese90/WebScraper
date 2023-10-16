import pandas as pd
import requests
from bs4 import BeautifulSoup
from Geschäftszweig import Extract_Company_Data


def Download_daily_data(Date):

  url = 'https://www.unternehmen24.info/Firmenbuch/%C3%96sterreich/Neueintragungen/' + Date
  Date2 = Date.replace("-","")
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  DF = pd.DataFrame()
  links= soup.find_all("a", href=True)
  for link in links:
    link2 = link.get("href")
    if "/Firmenbuch/Österreich/Firmenbuchinformation" in link2:
      try:
        url = "https://www.unternehmen24.info/" + link2
        Company_Data = Extract_Company_Data(url)
        print(Company_Data[3])
        Company_Data = pd.DataFrame(Company_Data).T



      except Exception as error:
        print(error)
        continue
      DF = pd.concat([DF, Company_Data])
      #print("Link:", link.get("href"), "Text:", link.string, link.title)
  DF.columns = ["published_at", "trade_register_number","county_court", "company", "city", "postal_code", "street", "share_capital", "business_purpose", "primary_branch", "managing_directors", "short_info_file", "info_file", "short_info_url", "info_url"  ]
  #Filename = "jakob_at_" + Date2 + ".csv"
  #DF.to_csv(Filename,index=False, encoding="utf32")
  print("finished ", Date)
  return DF

from requests.auth import HTTPBasicAuth
import requests


#url = "https://mai.allnet.de/api/v1/add-company"
#headers = {'Accept': 'application/json', "api-key": "FjJy2hTZN1IuvGdSjJyI1jnRskWQOfF2" }
#auth = HTTPBasicAuth('api-key', 'FjJy2hTZN1IuvGdSjJyI1jnRskWQOfF2')
#files = {'file': open('filename', 'rb')}

#json = {"published_at":"2023-07-04","trade_register_number":"FN607631a","county_court":"HG Wien","company":"Alwine Sechs Beteiligungen AG ","city":"Wien","postal_code":" 1010","street":" GmbH Plankengasse 2 ","share_capital":"70000","business_purpose":"","primary_branch":"Beteiligungsverwaltung, Verwaltung des eigenen Verm\u00f6gens","managing_directors":"","short_info_file":"","info_file":"","short_info_url":"https:\/\/www.unternehmen24.info\/Firmenbuch\/%C3%96sterreich\/Firmenbuchinformation\/2659F709FA9E16","info_url":""}
#req = requests.post(url,headers=headers, json=json)

#Date = "2023-07-05"
#DF = Download_daily_data(Date)
#for i in range(len(DF)):
#  b = DF.iloc[i].to_dict()
#  req = requests.post(url, headers=headers, json=b)

