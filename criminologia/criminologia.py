
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

         
    def get_Emcabezados(self):
        try:
            column_info=[]           
            columns = self.driver.find_element_by_tag_name("thead")
            tr =columns.find_elements_by_tag_name("tr")
            lista1=tr[1]
            td=lista1.find_elements_by_tag_name("td")
            if len(td) > 0:
                column_info=[td[0].text,td[1].text,td[2].text,"Estado"]            
                return column_info
        except:
              print("An exception occurred get_Emcabezados")
    
    def get_rows(self,element,dato):
        try:       
              d=element.find_elements_by_tag_name("td")
              if len(d) > 0:                    
                     data=[d[0].text,d[1].text,d[2].text,dato]                    
              return data  

        except:
              print("An exception occurred get_rows")


    def get_filaCompleta(self):
        try:       
             tablee = driver.find_element_by_tag_name("tbody")
             tr =tablee.find_elements_by_tag_name("tr")              
             return tr  

        except:
              print("An exception occurred get_rows")


if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="https://criminologia.or.cr/colegiados/lista-de-colegiados-activos/"
   
   # Url="https://criminologia.or.cr/colegiados/lista-colegiados-retiro-temporal/"
    driver.get(Url)
    table = Table(driver)
    rows=[]
    time.sleep(2)
    Encabezados=table.get_Emcabezados()

    # colegios activos
    
    tr =table.get_filaCompleta()
    column_rows=[]
    for element in tr:
          data =table.get_rows(element,"Activos")
          if data is not None:
             if len(data) > 0:
                 rows.append(data)
   
    
   # colegios suspendidos
    Url="https://criminologia.or.cr/colegiados/lista-de-colegiados-suspendidos/"
    driver.get(Url)
    table = Table(driver)
  
 
    tr =table.get_filaCompleta()
    column_rows=[]
    for element in tr:
          data =table.get_rows(element,"Suspendidos")
          if data is not None:
             if len(data) > 0:
                 rows.append(data)

  
      # colegios retiro temporal         
    Url="https://criminologia.or.cr/colegiados/lista-colegiados-retiro-temporal/"
    driver.get(Url)
    table = Table(driver)
  
  
    tr =table.get_filaCompleta()
    column_rows=[]
    for element in tr:
          data =table.get_rows(element,"Retiro Temporal")
          if data is not None:
             if len(data) > 0:
                 rows.append(data)

 
    print(rows)
    driver.close()
    if len(rows) > 0 and len(Encabezados) > 0:
        try:
            df = pd.DataFrame(rows, columns=Encabezados) 
            df.to_excel('C:\Pentaho\criminologia.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  
   
