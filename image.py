from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import json
from urllib.request import *
import sys
import time
download_path = r"C:\Users\Hatim\/"
def main():
	searchtext =input("Enter:")
	num_requested = 10
	if not os.path.exists(download_path + searchtext.replace(" ", "_")):
		os.makedirs(download_path + searchtext.replace(" ", "_"))

	url = "https://www.google.co.in/search?q="+searchtext+"&source=lnms&tbm=isch"
	driver = webdriver.Chrome(r"C:\Users\Hatim\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\selenium\webdriver\chrome/chromedriver.exe")
	driver.get(url)
	driver.maximize_window()

	headers = {}
	headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
	extensions = {"jpg", "jpeg", "png", "gif"}
	img_count = 0
	downloaded_img_count = 0
	imges = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
	
	for img in imges:
		img_count += 1
		img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
		img_type = json.loads(img.get_attribute('innerHTML'))["ity"]
		print ("Downloading image {}:{}".format(img_count,img_url))
		try:
			if img_type not in extensions:
				img_type = "jpg"
			req = Request(img_url, headers=headers)
			raw_img = urlopen(req).read()
			f = open(download_path+searchtext.replace(" ", "_")+"/"+str(downloaded_img_count)+"."+img_type, "wb")
			f.write(raw_img)
			f.close
			downloaded_img_count += 1
		except Exception as e:
			print ("Download failed: {}".format(e))
		
		if downloaded_img_count >= num_requested:
			break

	print ("Total downloaded: {}/{}".format(downloaded_img_count,img_count))
	

if __name__ == "__main__":
	main()
