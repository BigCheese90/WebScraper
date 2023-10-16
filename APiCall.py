from requests.auth import HTTPBasicAuth
import requests


url = "https://mai.allnet.de/api/v1/add-company"

headers = {'Accept': 'application/json', "api-key": "FjJy2hTZN1IuvGdSjJyI1jnRskWQOfF2" }
auth = HTTPBasicAuth('api-key', 'FjJy2hTZN1IuvGdSjJyI1jnRskWQOfF2')
#files = {'file': open('filename', 'rb')}

json = {"published_at":"04.07.2023","trade_register_number":"FN 607611x ","county_court":"HG Wien","company":"BIENENKORB Immobilien GmbH  ","city":"Wien","postal_code":" 1010","street":" Bauernmarkt 10\/8 9 ","share_capital":"35000","business_purpose":"","primary_branch":"An- und Verkauf von Immobilien","managing_directors":"Mag. Alexander","short_info_file":"","info_file":"","short_info_url":"https:\/\/www.unternehmen24.info\/\/Firmenbuch\/\u00d6sterreich\/Firmenbuchinformation\/2659F709FB9519","info_url":""}

req = requests.post(url,headers=headers, json=json)