
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

         
    def get_rows(self,element):
        try:       
              d=element.find_elements_by_tag_name("td")
              if len(d) > 0:                    
                     data=[d[0].text]                    
              return data  

        except Exception as e:
              print("An exception occurred get_rows" + str(e))


    def get_filaCompleta(self,posicion):
        try:       
             tablee = driver.find_element_by_tag_name("tbody")
             tr =tablee.find_elements_by_tag_name("tr") 
             
             if posicion == 0:
                 return tr  

             else:
                 return tr[posicion]

        except Exception as e:
              print("An exception occurred get_rows" + str(e))

    def get_Estado(self,element):
        try:       
             a = element.find_element_by_tag_name('a')
             url = a.get_attribute('href')
             driver.get(url)
             estado = driver.find_element_by_class_name("tipo")   
             numId =driver.find_element_by_class_name("numId")
             nombre =driver.find_element_by_class_name("nom") 
             data=[numId.text,nombre.text,estado.text]
             driver.execute_script("window.history.go(-1)")
             return data  

        except Exception as e:
              print("An exception occurred get_rows" + str(e))

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="http://admin.colfar.com/index.php?option=com_consultas&view=colegiado&q=%&inicio=1"
   
    driver.get(Url)
    table = Table(driver)
    rows=[]
    time.sleep(2)
    
    tr =table.get_filaCompleta(0)
    tr.pop(0)
    size=len(tr)
    column_rows=[]
    for element in range(1,size):
          d=table.get_filaCompleta(element)
          data =table.get_Estado(d)
          if data is not None:
             if len(data) > 0:
                 rows.append(data)
   
    print(rows)
    driver.close()
    if len(rows) > 0 :
        try:
            df = pd.DataFrame(rows, columns=['NColegiado','Nombre','Estado']) 
            df.to_excel('C:\Pentaho\Farmaceutica.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  
   

