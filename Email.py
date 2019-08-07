import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Username
user = "javax0110@gmail.com"

# Password
pwd = "hackathon"
driverpath = r"C:\Users\Hatim\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\selenium\webdriver\chrome/chromedriver.exe" # put your path to chromedriver 
driver = webdriver.Chrome(driverpath)
driver.maximize_window()


driver.get("http://www.gmail.com")
time.sleep(2)


element = driver.find_element_by_id("identifierId")
element.send_keys(user)
element.click()
time.sleep(3)


next=driver.find_element_by_css_selector('span.CwaK9').click()
#next = driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
time.sleep(1)


element = driver.find_element_by_css_selector("input.whsOnd.zHQkBf")
element.send_keys(pwd)
time.sleep(1)

next=driver.find_element_by_css_selector('span.CwaK9').click()
#driver.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
time.sleep(4)

driver.find_element_by_css_selector('.T-I-KE').click()
time.sleep(3)
driver.find_element_by_css_selector(".oj div textarea").send_keys('hatimanandwala5253@gmail.com')
time.sleep(1)
driver.find_element_by_css_selector(".aoD.az6 input").send_keys('automated')
time.sleep(1)
driver.find_element_by_css_selector(".Ar.Au div").send_keys('This is done by using selenium')
time.sleep(2)
driver.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.T-I-atl.L3").click()
time.sleep(5)

