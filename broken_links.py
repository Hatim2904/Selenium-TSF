import requests
from selenium import webdriver
driver=webdriver.Chrome(r"C:\Users\Hatim\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe")
driver.get('https://www.google.com/')
links = driver.find_elements_by_css_selector("a")
for link in links:
    r = requests.head(link.get_attribute('href'))
    if r.status_code>400:
        print(link.get_attribute('href'),":brokenLink:",r.status_code)
print("All Links are checked.")

