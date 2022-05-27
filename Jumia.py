import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import exceptions
d = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

links=[]
for i in range(1,11):
    try:
        webpage='https://www.jumia.com.ng/catalog/?q=infinix+phones&page='+str(i)
        d.get(webpage)
        WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//a[@class='core']")))
        link=d.find_elements_by_xpath("//a[@class='core']")
        for link_name in link:
           links.append(link_name.get_attribute('href'))
    except exceptions.StaleElementReferenceException as e:
        print(e)
        pass
print(len(links))


        
        
        


Details=[] 
for link in links:
    try:
        d.get(link)
        WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='-fs20 -pts -pbxs']")))
        product=d.find_element_by_xpath("//h1[@class='-fs20 -pts -pbxs']").text
        
        WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//a[@class='btn _def _ti -mhs -fsh0']")))
        see_all=d.find_element_by_xpath("//a[@class='btn _def _ti -mhs -fsh0']").get_attribute('href')
        d.get(see_all)
        WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//article[@class='-pvs -hr _bet']")))
        reviews=d.find_elements_by_xpath("//div[@class='stars _m _al -mvs']")
        stars=d.find_elements_by_xpath("//h3[@class='-m -fs16 -pvs']")
        for review, star in zip(reviews, stars):
            reviewsss=[]
            reviewsss.append(product)
            rev=review.text
            sta=star.text
            reviewsss.append( (rev, sta) )
            Details.append(reviewsss)
    except:
        pass
        continue

import pandas as pd
df=pd.DataFrame(Details)
df.to_csv('Infinix_Phones.csv')


        
        
        




        

    

        
