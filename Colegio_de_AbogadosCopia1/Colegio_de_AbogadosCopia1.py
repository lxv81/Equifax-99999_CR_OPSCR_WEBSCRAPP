
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
            tabla=self.driver.find_element_by_class_name("table")
            columns = tabla.find_element_by_tag_name("thead")
            th =columns.find_elements_by_tag_name("th")
            if len(th) > 0:
                column_info=[th[0].text,th[1].text,th[2].text,th[3].text,th[4].text,th[5].text,th[6].text,th[7].text,th[8].text]            
                return column_info
        except:
              print("An exception occurred get_Emcabezados")
    
    def get_rows(self):
        try:

            tabla=self.driver.find_element_by_class_name("table")
            tablee = tabla.find_element_by_tag_name("tbody")
            tr =tabla.find_elements_by_tag_name("tr")
            column_rows=[]
            for element in tr:                       
                d=element.find_elements_by_tag_name("td")
                if len(d) > 0:                    
                        column_rows=[d[0].text,d[1].text,d[2].text,d[3].text,d[4].text,d[5].text,d[6].text,d[7].text,d[8].text]                     
            return column_rows  

        except:
              print("An exception occurred get_rows")

  

    def SeleccionarCarnet(self):  
            try:
                 lista= driver.find_element_by_xpath('//*[@id="main"]/div/div/ul')
                 li= lista.find_elements_by_tag_name("li")
                 carnet=li[1]
                 carnet.click()
                 return 
        
            except:
                  print("An exception occurred SeleccionarCarnet") 
                  
                  
    def EscribirCarnet(self,carne):  
            try:
                 buscador = driver.find_elements_by_id("carne")
                 input =buscador[2]
                 input.clear()
                 input.send_keys(str(carne))
                 return
        
            except:
                  print("An exception occurred EscribirCarnet")
                  
    def BotonBuscar(self):  
            try:
                buton = driver.find_element_by_id("buscar1")
                buton.click()
                return
        
            except:
                  print("An exception occurred BotonBuscar")
   

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="https://www.abogados.or.cr/consultaagremiados/"
    driver.get(Url)
    table = Table(driver)

    table.SeleccionarCarnet()
    table.EscribirCarnet(12)
    table.BotonBuscar()
   
    Encabezados=table.get_Emcabezados()
    time.sleep(1)
    total_paginas = driver.find_element_by_xpath('//*[@id="main"]/div/p[1]')
    paginas=total_paginas.text
    listapaginas= paginas.split()

    for item in listapaginas:
        if(item.isnumeric()):
            numero_paginas=int(item)

    driver.execute_script("window.history.go(-1)")
    rows=[]
    numero_paginas=numero_paginas+1
    for i in range(27000,28000):  
           time.sleep(1)
           table.SeleccionarCarnet()
           table.EscribirCarnet(i)
           table.BotonBuscar()
           time.sleep(1)       
           data = table.get_rows()
           if data is not None:
                   if len(data) > 0:
                            rows.append(data)           
           driver.back()
          
         
    driver.close()
    if len(rows) > 0 and len(Encabezados) > 0:
        try:
            df = pd.DataFrame(rows, columns=Encabezados) 
            df.to_excel('C:\Pentaho\colegioAbb.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  

  
   