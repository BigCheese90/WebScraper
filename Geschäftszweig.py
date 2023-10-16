import requests, re
from bs4 import BeautifulSoup


def Extract_Company_Data(url):


    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #for td in soup.find_all("span",string="Firmenbuchsache:"):
        #print(td.find_next_sibling("p"))

    td = soup.find("span",string="Firmenbuchsache:")
    Find_Name = td.find_next_sibling("p")
    Extract_Name = Find_Name.get_text(separator=";")


    Find_Business = soup.find_all(string=re.compile(r"GESCHÄFTSZWEIG"))[0]
    Business = Find_Business.split(": ")[1][:-1]

    Firmendaten = Extract_Name.split(";")
    if len(Firmendaten) == 3:
        Firmendaten.insert(1, "")
    if len(Firmendaten) == 5:
        del Firmendaten[2]
    Plz = Firmendaten[3][0:5]
    Ort = Firmendaten[3][6:]
    Street = Firmendaten[2]
    Name = " ".join(Firmendaten[0:2])
    Find_Kapital = soup.find_all(string=re.compile(r"KAPITAL"))
    if not Find_Kapital:
        Kapital = ""
    else:
        Kapital = Find_Kapital[0].split(": ")[1][:-1]
        Kapital = Kapital[4:]
        Kapital = Kapital.replace(".", "")
        Kapital = Kapital.split(" ")
        Kapital = Kapital[0]

    Find_Boss = soup.find_all(string=re.compile(r"GESCHÄFTSFÜHRER"))
    if not Find_Boss:
        Boss = ""
    else:
        Boss = Find_Boss[0].split()[3:5]
        Boss = " ".join(Boss)

    Find_FBn = soup.find_all(string=re.compile(r"Firmenbuchnummer:"))
    FBn = Find_FBn[0].find_next_sibling().get_text()

    Find_Gericht = soup.find_all("span", string="Gericht:")[0].find_next_sibling("p").get_text()
    Find_Gericht = Find_Gericht.split(" eingetragen am ")
    Gericht = Find_Gericht[0]
    Datum = Find_Gericht[1]
    Datum = Datum[6:] + "-" + Datum[3:5] + "-" + Datum[0:2]



    return [Datum, FBn, Gericht, Name , Ort, Plz, Street, Kapital, Business,"", Boss, "", "", url, ""]

#print(Extract_Company_Data("https://www.unternehmen24.info/Firmenbuch/%C3%96sterreich/Firmenbuchinformation/2758FB0FF89017"))