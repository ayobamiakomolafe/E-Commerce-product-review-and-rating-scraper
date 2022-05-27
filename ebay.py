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
for i in range(1,4):
    try:
        webpage='https://www.ebay.com/sch/i.html?_from=R40&_nkw=lenovo+laptops&_sacat=0&LH_TitleDesc=0&_pgn='+str(i)
        d.get(webpage)
        
        link=d.find_elements_by_xpath("//a[@_sp='p2351460.m4114.l8597']")
        for link_name in link:
           links.append(link_name.get_attribute('href'))
    except exceptions.StaleElementReferenceException as e:
        print(e)
        pass
print(len(links))


Details=[] 
for link in links:
        d.get(link)
        WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='product-title']")))
        product=d.find_element_by_xpath("//h1[@class='product-title']").text
        try:
            d.find_element_by_xpath("//a[@class='see--all--reviews-link']").click()
            End_Page=False
            while End_Page==False:
                reviews=d.find_elements_by_xpath("//h3[@class='review-item-title wrap-spaces']")
                stars=d.find_elements_by_xpath("//div[@itemprop='reviewRating']")
                for rev, sta in zip(reviews, stars):
                    reviewss=[]
                    reviewss.append(product)
                    reviewss.append( (rev.text, sta.get_attribute('title')) )
                    Details.append(reviewss)
                
                try:
                    d.find_element_by_xpath("//a[@rel='next']").click()
                    time.sleep(4)
                    
                except Exception as e:
                    print(e)
                    End_Page=True
        except Exception as e:
            print(e)
            reviews=d.find_elements_by_xpath("//h3[@class='review-item-title wrap-spaces']")
            stars=d.find_elements_by_xpath("//div[@itemprop='reviewRating']")
            for rev, sta in zip(reviews, stars):
                reviewss=[]
                reviewss.append(product)
                reviewss.append( (rev.text, sta.get_attribute('title')) )
                Details.append(reviewss)
            
            


import pandas as pd
df=pd.DataFrame(Details)
df.to_csv('Lenovo_Laptops1.csv')
