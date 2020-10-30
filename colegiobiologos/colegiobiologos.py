
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
            tabla=self.driver.find_element_by_id("dresultado")
            columns = tabla.find_element_by_tag_name("thead")
            th =columns.find_elements_by_tag_name("th")
            if len(th) > 0:
                column_info=[th[1].text,th[2].text,th[3].text]            
                return column_info
        except:
              print("An exception occurred en get_Emcabezados")
    
    def get_rows(self):
        try:
            time.sleep(2)
            tabla=self.driver.find_element_by_id("dresultado")
            tablee = tabla.find_element_by_tag_name("tbody")
            tr =tabla.find_elements_by_tag_name("tr")
            column_rows=[]
            for element in tr:
                d=element.find_elements_by_tag_name("td")
                if len(d) > 0:                    
                    column_rows=[d[1].text,d[2].text,d[3].text]                     
            return column_rows  

        except:
              print("An exception occurred en get_rows")
                    
                  
    def EscribirCarnet(self,carne):  
            try:
                 buscador = driver.find_element_by_id("ibuscar")
                 buscador.clear()
                 buscador.send_keys(str(carne))
                 return
        
            except:
                  print("An exception occurred  en EscribirCarnet")
                  
    def BotonBuscar(self):  
            try:
                buton = driver.find_element_by_xpath('//*[@id="post-136"]/div/div[2]/div[3]/button')
                buton.click()
                return
        
            except:
                  print("An exception occurred BotonBuscar")
   

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="http://www.colegiobiologos.com/agremiados/estado-del-agremiado/"
    driver.get(Url)
    table = Table(driver)
    contador=0
    rows=[]
    data=[]
    Emcabezados=[]
    for i in range(1,3000):           
           table.EscribirCarnet(i)
           table.BotonBuscar()
           data.append(table.get_rows())        
           if data[0] is not None:
               if len(data[0]) > 0:
                        rows.append(data[0])
                        if contador == 0:                                              
                               Emcabezados.append(table.get_Emcabezados())
                               contador = 1
           
   # print(rows)
   
    #print(Emcabezados)
    if len(rows) > 0 and len(Emcabezados) > 0:
        try:
            df = pd.DataFrame(rows, columns=Emcabezados[0]) 
            df.to_excel('C:\Pentaho\colegiobiologos.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  
   
