import requests, re
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.unternehmen24.info/Firmenbuch/%C3%96sterreich/Firmenbuchinformation/2659F709FA9E16"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

for td in soup.find_all("span",string="Firmenbuchsache:"):
    print(td.find_next_sibling("p"))


Find_Name = td.find_next_sibling("p")
Extract_Name = Find_Name.get_text(separator=";")

Firmendaten = Extract_Name.split(";")
if len(Firmendaten) == 3:
    Firmendaten.insert(1, "")
if len(Firmendaten) == 5:
    del Firmendaten[2]
Plz = Firmendaten[3][0:5]
Ort = Firmendaten[3][6:]
Street = Firmendaten[2]
Name = Firmendaten[0:2]
Find_Business = soup.find_all(string=re.compile(r"GESCHÄFTSZWEIG"))[0]
Business = Find_Business.split(": ")[1][:-1]

Find_Kapital = soup.find_all(string=re.compile(r"KAPITAL"))
if not Find_Kapital:
    Kapital = ""
else:
    Kapital = Find_Kapital[0].split(": ")[1][:-1]
    Kapital = Kapital[4:]
    Kapital = Kapital.replace(".","")
Find_Boss = soup.find_all(string=re.compile(r"GESCHÄFTSFÜHRER"))
if not Find_Boss:
    Boss = ""
else:
    Boss = Find_Boss[0].split()[3:5]
    Boss = " ".join(Boss)
Find_FBn = soup.find_all(string=re.compile(r"Firmenbuchnummer:"))
FBn = Find_FBn[0].find_next_sibling().get_text()
FBn = FBn.replace(" ","")
Find_Gericht = soup.find_all("span", string = "Gericht:")[0].find_next_sibling("p").get_text()
Gericht = Find_Gericht.split(" eingetragen am ")
Datum = Gericht[1]
Gericht = Gericht[0]
Datum = Datum[6:] +"-" +Datum[3:5] + "-" +Datum[0:2]
Firmendaten = [Datum,FBn, Gericht, Name , Ort, Plz, Street, Kapital, "", Business, Boss, "", "",url,""  ]
DF = pd.DataFrame(Firmendaten)
DF = DF.T
DF.columns = ["published_at", "trade_register_number","county_court", "company", "city", "postal_code", "street", "share_capital", "business_purpose", "primary_branch", "managing_directors", "short_info_file", "info_file", "short_info_url", "info_url"  ]
test = DF.to_json(orient="records")


test = test[1:-1]
