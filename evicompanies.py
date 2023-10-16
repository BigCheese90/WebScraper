import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set the path to your ChromeDriver executable
chromedriver_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'  # Replace with your path

# URL of the website you want to interact with
url = 'https://allnet.at'  # Replace with your target website

# Create a Chrome WebDriver with Selenium
chrome_service = ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=chrome_service)


# Navigate to the website
driver.get(url)

 # Execute JavaScript in the console


script = """console.log(csvContent);

"""
result = driver.execute_script(script)

# Create a DataFrame with the result
df = pd.DataFrame({'Result': [result]})

 # Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)


# Close the browser
driver.quit()