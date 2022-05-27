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
for i in range(1,3):
    try:
        webpage='https://www.aliexpress.com/premium/lenovo-thinkpad-laptop.html?trafficChannel=ppc&d=y&CatId=0&SearchText=lenovo+thinkpad+laptop&ltype=premium&SortType=default&page='+str(i)
        d.get(webpage)
        WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//a[@class='_3t7zg _2f4Ho']")))
        link=d.find_elements_by_xpath("//a[@class='_3t7zg _2f4Ho']")
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
        WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//h1[@class='product-title-text']")))
        product=d.find_element_by_xpath("//h1[@class='product-title-text']").text
        
        d.find_element(By.CSS_SELECTOR, "span.product-reviewer-reviews").click()

        #navigate to parent element of iframe and scroll into view
        ifs = d.find_element(By.CSS_SELECTOR, ".tab-content > div:nth-child(2) > div")
        d.execute_script("arguments[0].scrollIntoView();", ifs)
        d.switch_to.frame('product-evaluation')

 
        End_Page=False
        while End_Page==False:
            reviews = d.find_elements(By.CSS_SELECTOR, "#transction-feedback dt.buyer-feedback > span:nth-child(1)")
            stars= d.find_elements_by_xpath("//span[@class='star-view']")
            for rev, sta in zip(reviews, stars):
                reviewss=[]
                star=sta.find_element_by_tag_name('span').get_attribute('style').split(':')[1]
                reviewss.append(product)
                reviewss.append((rev.text, star))
                Details.append(reviewss)
                    
            try:
                nx = d.find_element(By.CSS_SELECTOR, "a.ui-pagination-next")
                d.execute_script("arguments[0].click();", nx)
                time.sleep(3)
                continue
            except Exception as e:
                End_Page=True
    except:
        pass

import pandas as pd
df=pd.DataFrame(Details)
df.to_csv('Lenovo_Laptop.csv')
       

        


            
       

       
       
