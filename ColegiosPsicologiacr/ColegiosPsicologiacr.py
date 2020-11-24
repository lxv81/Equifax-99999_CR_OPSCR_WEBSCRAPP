


# -*- coding: utf-8 -*-
"""
Created on monday oct 26 2020

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


    def get_rows(self):
        try:
            time.sleep(3)
            soup = BeautifulSoup(driver.page_source, "lxml")
            gdp_table = soup.find_all("tr") 
            data = []
            for tr in gdp_table:
                tds = tr.find_all('td')
                if len(tds) > 0:  
                      if len(tds) == 10:
                         data.append([tds[0].text,tds[1].text,tds[2].text,tds[3].text,tds[4].text,tds[5].text,tds[6].text,tds[7].text,tds[8].text,tds[9].text])

            return data  

        except Exception as e:
              print("An exception occurred get_rows " + str(e))

    def Paginacion(self,i):  
            try:
                time.sleep(1)
                buton = driver.find_element_by_class_name("facetwp-pager")
                lista = buton.find_elements_by_tag_name('a')
                for item in lista:
                    if str(i) == item.text:
                         item.click()
                return
        
            except Exception as e:
                  print("Error en Paginacion " +str(e))
   

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="https://psicologiacr.com/directorio-de-profesionales/"
    driver.get(Url)
    table = Table(driver)
    ListaUrls =[]
    rows=[]

    #resp =table.get_rows()
    #if resp  is not None:
     #   if len(resp) > 0:
      #      for item in resp:
       #         rows.append(item)

    driver.forward()
    for i in range(2,1131):
                     #url = 'https://psicologiacr.com/directorio-de-profesionales/?fwp_paged='+ str(i)
                     #driver.get(url)
                     #table = Table(driver)   
                     data = table.get_rows()
                     if data is not None:
                         if len(data) > 0:
                             for elemento in data:
                                     rows.append(elemento)
                     table.Paginacion(i)

    driver.close()
    if len(rows) > 0:
        try:
            encabezados =['Codigo','Nombre','Provincia','Canton','Estado','Grado','Telefono','Correo','AreasTrabajo','ID',]
            df = pd.DataFrame(rows , columns=encabezados) 
            df.to_excel('C:\Pentaho\ColegioPsicologia.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  

  
   
