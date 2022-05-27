import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
d = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

links=[]
for i in range(1,2):
    webpage='https://www.amazon.com/s?k=sony+headphones&crid=29OUGQHGQKUHU&qid=1646325024&sprefix=sony+head%2Caps%2C601&ref=sr_pg_'+ str(i)
    d.get(webpage)
    link=d.find_elements_by_xpath("//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
    for link_name in link:
        links.append(link_name.get_attribute('href'))
      

Details=[]   
for link in links:
    
    try:
        d.get(link)
        WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//span[@id='productTitle']")))
        product=d.find_element_by_xpath("//span[@id='productTitle']").text
        
        WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//a[@data-hook='see-all-reviews-link-foot']")))
        d.find_element_by_xpath("//a[@data-hook='see-all-reviews-link-foot']").click()
        WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='a-section review aok-relative']")))

        End_Page=False
        while End_Page==False:
            
            review=d.find_elements_by_xpath("//a[@data-hook='review-title']")
            star=d.find_elements_by_xpath("//i[@data-hook='review-star-rating']")
            for rev, sta  in zip(review, star):
                reviews=[]
                reviews.append(product)
                reviews.append (  (rev.get_attribute('textContent').strip(), sta.get_attribute('textContent').strip()) )
                Details.append(reviews)
                
            try:
                d.find_element_by_xpath("//li[@class='a-last']").click()
                time.sleep(4)
                continue
            except:
                End_Page=True
        
      
    except:
        pass

import pandas as pd
df=pd.DataFrame(Details)
df.to_csv('Sony_Headphones.csv')
            

        

        


    


    
