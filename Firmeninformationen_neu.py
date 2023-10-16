import requests,re
from bs4 import BeautifulSoup
import random

def extract_company_info(url):
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    ]

    user_agent =random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    Firmenname = soup.find(string="Name:").findNext('td').findNext("td").contents[0].text
    Adresse = soup.find(string="Adresse:").findNext('td').findNext("td").contents
    Strasse = Adresse[0]
    Plz = Adresse[2][0:4]
    Ort = Adresse[2][5:-3]
    Land = soup.find(string="Land").findNext('td').findNext("td").contents[0]
    FBn = soup.find(string="Firmenbuchnummer:").findNext('td').findNext("td").text
    print(FBn)
    Kapital = ""
    try:
        Kapital = soup.find(string="Kapital:").findNext('td').findNext("td").contents[0]
    except:
        print("Kapital not found")
    try:
        Firmenzweck = soup.find(string="Firmenzweck:").findNext('td').findNext("td").contents[0]
    except:
        Firmenzweck = soup.find(string="Tätigkeit:").findNext('td').findNext("td").contents[0]
    Datum = soup.find(string="Firmenbuch-Bekanntmachungen:").findNext("td").text
    Datum = Datum[-4:] +  "-" + Datum[-7:-5] + "-" +Datum[0:2]
    return (Datum, FBn, "", Firmenname, Ort, Plz, Strasse, Kapital, Firmenzweck, "", "", "", "", url, "")

#a=extract_company_info("https://www.unternehmen24.info/Firmeninformationen/%C3%96sterreich/Firma/77776100369")