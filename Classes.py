from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import pandas as pd
from time import sleep
from random import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



class UrlGrabber:
    def __init__(self):
        chromedriver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'  # Replace with your path
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        chrome_service = ChromeService(executable_path=chromedriver_path)
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


    def connect(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def move_Mouse(self):
        button = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Alle")
        ActionChains(self.driver) \
            .move_to_element(button) \
            .perform()

    jscript = """const results = [    ['Url', 'Anchor Text', 'External'] ];
var urls = document.getElementsByTagName('a');
for (urlIndex in urls) {
    const url = urls[urlIndex]
    const externalLink = url.host !== window.location.host
    if(url.href && url.href.indexOf('://')!==-1) results.push([url.href, url.text, externalLink]) // url.rel
}
const csvContent = results.map((line)=>{
    return line.map((cell)=>{
        if(typeof(cell)==='boolean') return cell ? 'TRUE': 'FALSE'
        if(!cell) return ''
        let value = cell.replace(/[\\f\\n\\v]*\\n\s*/g, "\\n").replace(/[\\t\\f ]+/g, ' ');
        value = value.replace(/\\t/g, ' ').trim();
        return `"${value}"`
    }).join('\\t')
}).join("\\n");
return csvContent"""


    def graburl(self):
        result = self.driver.execute_script(self.jscript)
        return result


class DataHandler:
    def __init__(self, data):
        self.data = data

    def reformat(self, condition):
        result = []
        a = self.data.split("\n")
        for i in a:
            if condition in i:
                result.append(i.split("\t"))
        df = pd.DataFrame(result, columns = ["url", "description", "external"])
        df["url"] = df["url"].apply(lambda x: x[1:-1])
        df["description"] = df["description"].apply(lambda x: x[1:-1])
        return df

df = pd.DataFrame()
Scraper = UrlGrabber()

for i in range(1, 211):

    Scraper.connect("https://www.evi.gv.at/s?suche=neueintragung&page="+str(i))
    sleep(random()*5+1)
    Scraper.move_Mouse()
    #Test.connect("https://httpbin.org/headers")
    data = Scraper.graburl()
    sleep(random()*20+1)
    dataclean = DataHandler(data).reformat("https://www.evi.gv.at/b/")
    print(dataclean)
    df = pd.concat([df, dataclean])
    sleep(random() * 20 + 1)
    sleep(5)
    print(i)

df.to_csv("CompanyData", sep=";", index=False)