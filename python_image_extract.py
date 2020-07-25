import time
import os
# selenium is library used for automation of web browser
from selenium import webdriver
# urllib is used used to fetch and perform operation on URL
import urllib.request
# These Keys are referring to keyboard keys 
# for example Keys.ENTER will refer to "enter" button on keyboard 
from selenium.webdriver.common.keys import Keys
# Used to download Chrome Driver
from webdriver_manager.chrome import ChromeDriverManager



# ChromeDriverManager will download and install chrome driver 
browser = webdriver.Chrome(ChromeDriverManager().install()) 	
# get() will open URL provided in Parentheis
browser.get("https://www.google.com/")


# q specifically point to the search box and find element whose name='q' 
search = browser.find_element_by_name('q')


# Given text is put in search box and enter key of keyboard is pressed
search.send_keys("women top and women dress",Keys.ENTER)



# link text will find "given text" within an anchor tag and return first matching element
elem = browser.find_element_by_link_text('Images')
# get href value within anchor tag and perform click
elem.get_attribute('href')
elem.click()

# scroll down the page for loading all images
value = 0
for i in range(20):
	browser.execute_script("scrollBy("+ str(value) +",+1000);")
	value += 1000
	time.sleep(3)


# google images contain in a div tag with is 'islmp'.It will get element by id having value 'islmp'. 
elem1 = browser.find_element_by_id('islmp')
# It will find all elements whose div tag contains img  
sub = elem1.find_elements_by_tag_name("img")


#It will create image directory to store all images
try:
	os.mkdir('images')
except FileExistsError:
	pass

# It will iterate all images stored in sub 
count = 0
for i in sub:
	# get source of current image
	src = i.get_attribute('src')
	# try catch block beacause some image url may be none
	try:
		if(src != None):
			src = str(src)
			print(src)
			count+=1
			# urllib.request.urlretrieve used to download images
			urllib.request.urlretrieve(src, os.path.join('images','image'+str(count)+'.jpg'))
			if(count==500):
				break
		else:
			raise TypeError
	except TypeError:
		print('fail')
			
