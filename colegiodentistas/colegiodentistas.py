

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
            column_info=["Codigo","Nombre","Especialidad","Estado"]            
            return column_info
        except:
              print("An exception occurred get_Emcabezados")
    
    def get_rows(self,element,tipo):
        try:       
              d=element.find_elements_by_tag_name("td")
              if len(d) > 0:                    
                    if tipo == 1:
                         data=[d[0].text,d[1].text," ",d[3].text]
                    else:
                         data=[d[0].text,d[1].text,d[3].text," "] 
                           
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
    Url="http://www.colegiodentistas.org/sitCol/miembros-activos/"
   
    driver.get(Url)
    table = Table(driver)
    rows=[]
    Especialistas=[]
    Suspendidos=[]
    Pencionados=[]
    time.sleep(2)
    Encabezados=table.get_Emcabezados()
    tr =table.get_filaCompleta()
    # colegios de cirujanos activos mandar 1 cuando es estado
    for element in tr:
          data =table.get_rows(element,1)
          if data is not None:
             if len(data) > 0:
                 rows.append(data)



    # colegios de cirujanos suspendidos mandar 1 cuando es estado
    Url="http://www.colegiodentistas.org/sitCol/suspendidos/"  
    driver.get(Url)
    table = Table(driver)

    tr =table.get_filaCompleta()
    # colegios de cirujanos activos
    for element in tr:
          data =table.get_rows(element,1)
          if data is not None:
             if len(data) > 0:
                 rows.append(data)


    # colegios de cirujanos pensionados mandar 1 cuando es estado
    Url="http://www.colegiodentistas.org/sitCol/miembros-pensionados/"  
    driver.get(Url)
    table = Table(driver)

    tr =table.get_filaCompleta()
    # colegios de cirujanos activos
    for element in tr:
          data =table.get_rows(element,1)
          if data is not None:
             if len(data) > 0:
                 rows.append(data)


     # colegios de cirujanos  mandar 0 cuando es especialidad
    Url="http://www.colegiodentistas.org/sitCol/especialistas/"  
    driver.get(Url)
    table = Table(driver)

    tr =table.get_filaCompleta()
    # colegios de cirujanos activos
    for element in tr:
          data =table.get_rows(element,0)
          if data is not None:
             if len(data) > 0:
                 rows.append(data)



    if len(rows) > 0 and len(Encabezados) > 0:
        try:
            df = pd.DataFrame(rows, columns=Encabezados) 
            df.to_excel('C:\Pentaho\colegiodentistas.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')


  
   
