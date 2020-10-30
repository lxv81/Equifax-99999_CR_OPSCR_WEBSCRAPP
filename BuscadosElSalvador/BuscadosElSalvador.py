

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

         
    def Paginacion(self):
        try:     
            time.sleep(3)
            valor= False 
            listaPaginacion = driver.find_element_by_class_name("custom-pagination")
            a= listaPaginacion.find_elements_by_tag_name("a")
            for item in a:
                if item.text == 'Siguiente »':
                         item.click()  
                         valor =True
                   
            return valor

        except Exception as e:
              print("An exception occurred get_rows" + str(e))

   

    def get_data(self,item):
        try:       
             time.sleep(1)   
             data =[]
             div =item.find_element_by_tag_name("div")  
             nombre = div.get_attribute('data-firstname') 
             apellidos = div.get_attribute('data-lastname')    
             direccion = div.get_attribute('data-address')    
             delito = div.get_attribute('data-crime')    
             detalle = div.get_attribute('data-details')   
             data =[nombre,apellidos,direccion,delito,detalle]
             return data  

        except Exception as e:
              print("An exception occurred get_rows" + str(e))

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="https://www.tupista.info/mas-buscados/personas/"
   
    driver.get(Url)
    table = Table(driver)
    rows=[]
    time.sleep(2)
    

    listaPaginacion = driver.find_element_by_class_name("custom-pagination")
    a= listaPaginacion.find_elements_by_tag_name("a")  
    numero_paginas=a[-2].text
    numero_paginas = int(numero_paginas)   
    numero_paginas =numero_paginas + 1
    column_rows=[]
    for element in range(0,numero_paginas):
           
            data =  driver.find_element_by_class_name("most-wanted")
            lista = data.find_elements_by_class_name("most-wanted__box")
            for item in lista:               
                  data =table.get_data(item)
                  if data is not None:
                     if len(data) > 0:
                          rows.append(data)

          
            validacion = table.Paginacion()
            if validacion == False:
                break
   
   
    driver.close()
    if len(rows) > 0 :
        try:
            df = pd.DataFrame(rows,columns=['Nombre','Apellidos','Direccion','Delito','Detalle']) 
            df.to_excel('C:\Pentaho\BuscadosELSalvador.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  
   


