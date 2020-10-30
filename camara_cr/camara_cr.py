
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:50:40 2020

@author: luis
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
from self import self

class Table:
    def __init__(self,driver):
        self.driver=driver


    def get_rows(self,item):
        try:
           i = item.find_element_by_tag_name("i")
           i.click()   
           time.sleep(3)
           informacion= self.driver.find_element_by_class_name("agent-contact-form")  
           nombre=informacion.find_element_by_tag_name("h3")
           asociado=informacion.find_element_by_tag_name("p")
           listaInfo=informacion.find_elements_by_tag_name("li")
           column_rows=[]
           column_rows.append(nombre.text)
           for item in listaInfo:
                 column_rows.append(item.text)  
           return column_rows

        except Exception as e:
              print("An exception occurred get_rows "+str(e))

    def CalcularPaginacion(self):  
        try:           
             pages =self.driver.find_elements_by_class_name("page-numbers")
             return len(pages)
        
        except Exception as e:
              print("An exception occurred CalcularPaginacion" +str(e))

   
                  
                  
  
   

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="https://camara.cr/agents/"
    driver.get(Url)
    table = Table(driver)

   # table.get_rows()
    number_pages =table.CalcularPaginacion()
    number_pages= number_pages;
    rows=[]
    data=[]
    for i in range(1,number_pages):   
           xpah='//*[@id="main"]/div/div/div/div[1]/div[2]/ul/nav/div/a['+str(i)+']'
           driver.find_element_by_xpath(xpah).click()
           time.sleep(1)
           for i in range(0,9):
                     lista= driver.find_elements_by_class_name("blog-image")
                     data.append(table.get_rows(lista[i]))                   
                     if data[0] is not None :
                                if len(data[0]) > 0 :
                                        rows.append(data[0]) 
                    
                     driver.execute_script("window.history.go(-1)")
                     time.sleep(2)

        
    print(rows)


    if len(rows) > 0:
            try:
                df = pd.DataFrame(data=rows) 
                df.to_excel('C:\Pentaho\Camara.xlsx',index=False)

            except:
                    print("Error en escribir en el excel")
    else:
          print('ocurrio un error')    
   
    

  

  
   
