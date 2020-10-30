

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
            listaPaginacion = self.driver.find_element_by_css_selector("#block-cog-dea-content > div > div > nav > ul")
            li= listaPaginacion.find_elements_by_tag_name("li")  
            for item in li:
                if item.text == 'Next page\n››':                        
                    a =item.find_element_by_tag_name("a") 
                    url = a.get_attribute('href')
                    driver.get(url)               
                    return   

        except Exception as e:
              print("An exception occurred Paginacion" + str(e))

    def get_filaCompleta(self,posicion):
            try:       
                data = self.driver.find_elements_by_class_name("views-row") 
             
                if posicion == -1:
                     return data  

                else:
                     return data[posicion]

            except Exception as e:
              print("An exception occurred get_filaCompleta" + str(e))
   

    def get_Estado(self,element):
        try:       
             time.sleep(1)
             a = element.find_element_by_tag_name('a')
             url = a.get_attribute('href')
             driver.get(url)
             time.sleep(1)
             nombre = driver.find_element_by_tag_name("h1")   
             info =driver.find_element_by_class_name("field--violations")
             delito =info.find_element_by_tag_name("div")   
             tabla=driver.find_element_by_tag_name("tbody")
             tr=tabla.find_elements_by_tag_name("tr")   
             lista=[nombre.text,delito.text]
             Emcabezados=['Nombre','Delito']
           
             for item in tr:
                     td=item.find_elements_by_tag_name("td")   
                     lista.append(td[1].text)
                     Emcabezados.append(td[0].text)

            
             driver.execute_script("window.history.go(-1)")
             return lista  

        except Exception as e:
              driver.execute_script("window.history.go(-1)")
              print("An exception occurred get_Estado" + str(e))

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="https://www.dea.gov/fugitives/all"
   
    driver.get(Url)
    table = Table(driver)
    rows=[]
    time.sleep(2)
    listaPaginacion = driver.find_element_by_css_selector("#block-cog-dea-content > div > div > nav > ul")
    li= listaPaginacion.find_elements_by_tag_name("li")  
    next= li[-1]
    a =next.find_element_by_tag_name("a") 
    url = a.get_attribute('href')
    driver.get(url)         
    column_rows=[]
    listaPaginacion2 = driver.find_element_by_css_selector("#block-cog-dea-content > div > div > nav > ul")
    li= listaPaginacion2.find_elements_by_tag_name("li")  
    next= li[-1]
    data= next.text.replace("\n",",")
    Lista = data.split(",")
    paginacion=0
    for item in Lista:
         x = item.isnumeric()
         if x:
             paginacion=int(item)
    driver.execute_script("window.history.go(-1)")
    d=table.get_filaCompleta(-1)
    size=len(d)
    for item in range(1,paginacion):
            for item in range(0,size):
                  elemento= table.get_filaCompleta(item)
                  data =table.get_Estado(elemento)
                  if data is not None:
                     if len(data) > 0:
                          rows.append(data)


            table.Paginacion()
   
   
    driver.close()
    if len(rows) > 0 :
        try:
            df = pd.DataFrame(data=rows) 
            df.to_excel('C:\Pentaho\DEA.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  
   

