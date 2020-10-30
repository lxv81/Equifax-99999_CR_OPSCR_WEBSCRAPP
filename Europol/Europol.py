

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

         
    def personas(self,item):
        try:     
            time.sleep(4)
            valor= False 
            data = driver.find_elements_by_class_name("wanted_teaser_quick_info")
            boton = data[item]
           # data.send_keys(Keys.ENTER)
            boton.click()  
            valor =True
                   
            return valor

        except Exception as e:
              print("An exception occurred get_rows" + str(e))

   

    def get_data(self,item):
        try:       
             time.sleep(5)   
             data =[]
             lista =[]
             info=driver.find_element_by_class_name("wanted_top_right")
             divs = info.find_elements_by_tag_name("div")
             nombre = driver.find_element_by_class_name("field-name-title-field")
             for item in divs:
                 lista.append(item.text.replace("\n",""))
             
             bandera = 0
             bandera2 = 0
             validacion = 0
             Delito =''
             sexo =''
             ojos =''
             nacimiento =''
             origen =''
             nacionalidad =''
             idioma =''
             estado =''
             for elemento in lista:
                 separar = elemento.split(":")

                 if separar[0] in ('DELITO','SEXO ','COLOR DE OJOS','FECHA DE NACIMIENTO','NACIONALIDAD','ORIGEN ÉTNICO','IDIOMAS HABLADOS','ESTADO DEL CASO'):
                      if separar[0] in ('DELITO'):
                          Delito =separar[1]
                          validacion = 1
                      if separar[0] in ('SEXO '):
                           sexo =separar[1]
                           validacion = 1
                      if separar[0] in ('COLOR DE OJOS'):
                          ojos =separar[1]
                          validacion = 1
                      if separar[0] in ('FECHA DE NACIMIENTO'):
                          if bandera  == 0:
                              bandera = 1
                              validacion = 1
                              nacimiento =separar[1]
                      if separar[0] in ('NACIONALIDAD'):
                          nacionalidad =separar[1]
                          validacion = 1
                      if separar[0] in ('ORIGEN ÉTNICO'):
                          origen =separar[1]
                          validacion = 1
                      if separar[0] in ('IDIOMAS HABLADOS'):
                          idioma =separar[1]
                          validacion = 1
                      if separar[0] in ('ESTADO DEL CASO'):
                          if bandera2  == 0:
                              bandera2 = 1
                              validacion = 1
                              estado =separar[1]

             if validacion == 1:
                    data=[nombre.text,Delito,sexo,ojos,nacimiento,nacionalidad,origen,idioma,estado]
             print(data)
             print(len(data))
             
             return data  

        except Exception as e:
              print("An exception occurred get_rows" + str(e))

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="https://eumostwanted.eu/es"
   
    driver.get(Url)
    table = Table(driver)
    rows=[]
    time.sleep(2)
    

    personas = driver.find_elements_by_class_name("wanted_teaser_quick_info")
    print(len(personas))
   
    column_rows=[]
    for item in range(0,42): 
                  valor = table.personas(item)
                  if valor == True:
                      data =table.get_data(item)
                      if data is not None:
                         if len(data) > 0:
                              rows.append(data)
                  
              #   driver.execute_script("window.history.go(-1)")
               #   Atras = driver.find_element_by_id("homeWantedTop") 
                 # Atras.click()
                              driver.forward()
                              driver.back()
    driver.close()
    if len(rows) > 0 :
        try:
            df = pd.DataFrame(rows,columns=['nombre','Delito','sexo','ojos','nacimiento','nacionalidad','origen','idioma','estado']) 
            df.to_excel('C:\Pentaho\Europol.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  
   



