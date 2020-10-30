



# -*- coding: utf-8 -*-
"""
Created on oct 06 11:50:40 2020

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
            th =columns.find_elements_by_tag_name("th")
            if len(th) > 0:
                column_info=[th[0].text,th[1].text,th[2].text,th[3].text,th[4].text,th[5].text,th[6].text]            
                return column_info
        except:
              print("An exception occurred get_Emcabezados")
    
    def get_rows(self,item):
        try:
              column_rows=[]
              d=item.find_elements_by_tag_name("td")
              if len(d) > 0:                    
                    column_rows=[d[0].text,d[1].text,d[2].text,d[3].text,d[4].text,d[5].text,d[6].text]                     
              return column_rows  

        except:
              print("An exception occurred get_rows")

    def Paginacion(self):  
        try:
              paginacion = self.driver.find_element_by_class_name("pdb-pagination")
              li= paginacion.find_elements_by_tag_name("li")
              data =li[-2]
              validacion =  data.get_attribute("class")      
              valor = False
              if validacion == 'disabled' :
                  valor = True

              else:
                   a =data.find_element_by_tag_name("a")
                   a.send_keys(Keys.ENTER)
                   time.sleep(3)
              return valor
        
        except:
              print("An exception occurred CalcularPaginacion")


if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="https://cpncampus.com/wp/colegiados/"
    driver.get(Url)
    table = Table(driver)
    time.sleep(1)
    Encabezados=table.get_Emcabezados()

    rows=[]
    while True:  
           time.sleep(2)
           tablee = driver.find_element_by_tag_name("tbody")
           tr =tablee.find_elements_by_tag_name("tr")
           for item in tr:
                 rows.append(table.get_rows(item))          
           
           validacion = table.Paginacion()
           if validacion:   
                        break
           
         
    
    if len(rows) > 0 and len(Encabezados) > 0:
        try:
            df = pd.DataFrame(rows, columns=Encabezados) 
            df.to_excel('C:\Pentaho\Lista-cpncr.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  

  
   