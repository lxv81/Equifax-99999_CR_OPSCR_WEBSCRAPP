

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

    def get_rows(self):
        try:
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source, "lxml")
            table = soup.findAll('table')
            column_rows=[]
            if len(table) > 0:
                tr = table[0].tbody.findAll('tr')              
                contador = 0 
                for element in tr: 
                        if contador == 1:
                            d=element.findAll('td')
                            if len(d) > 0:                    
                                    column_rows=[d[0].text,d[1].text,d[2].text,d[3].text,d[4].text,d[5].text]    
                        contador += 1
            return column_rows  

        except Exception as e:
              print("Error en get_rows" + str(e))

  

    def SeleccionarCarnet(self):  
            try:
                 lista =self.driver.find_elements_by_class_name("col-sm-4")
                 carnet = lista[0]
                 h3 = carnet.find_element_by_class_name("panel-title")
                 h3 = carnet.find_element_by_class_name("panel-title")
                 a = h3.find_element_by_tag_name("a")
                 a.click()
                
                 return 
        
            except:
                  print("An exception occurred SeleccionarCarnet") 
                  
                  
    def EscribirCarnet(self,carne):  
            try:
                 input = driver.find_element_by_id("MainContent_txtcarne")              
                 input.clear()
                 input.send_keys(str(carne))
                 return
        
            except:
                  print("An exception occurred EscribirCarnet")
                  
    def BotonBuscar(self):  
            try:
                buton = driver.find_element_by_id("MainContent_Btncarne")
                buton.click()
                return
        
            except:
                  print("An exception occurred BotonBuscar")
   

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="http://consultas.contador.co.cr/"
    driver.get(Url)
    table = Table(driver)
    rows = []
    for i in range(1,36875):  
           table.SeleccionarCarnet()
           table.EscribirCarnet(i)
           table.BotonBuscar() 
           data = table.get_rows()
           if data is not None:
                   if len(data) > 0:
                            rows.append(data)           

    driver.close()
    if len(rows) > 0 :
        try:
            Encabezados = ['Carne','Nombre','Cedula','Estado','SubEstado','ConsejoRegional']
            df = pd.DataFrame(rows, columns=Encabezados) 
            df.to_excel('C:\Pentaho\Lista-CCPCR.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  

  
   