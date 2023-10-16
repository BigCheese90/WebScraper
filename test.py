from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import json

# Set the path to your ChromeDriver executable
chromedriver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'  # Replace with your path

# Set up Chrome options to enable logging
chrome_options = Options()
#chrome_options.add_argument('--headless')  # Optional: Run Chrome in headless mode
#chrome_options.add_argument('--disable-gpu')  # Optional: Disable GPU acceleration
#chrome_options.add_argument('--enable-logging')  # Enable console logging

# Create a Chrome WebDriver with Selenium
chrome_service = ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


# Navigate to the website you want to capture console logs from
driver.get('https://www.evi.gv.at/s?suche=neueintragung')  # Replace with your target website

script = """
const results = [    ['Url', 'Anchor Text', 'External'] ];
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
return csvContent
"""
result = driver.execute_script(script)





