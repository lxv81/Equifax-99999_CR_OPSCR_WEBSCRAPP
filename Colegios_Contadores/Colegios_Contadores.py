



# -*- coding: utf-8 -*-
"""
Created on oct 06 10:50:40 2020

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
              time.sleep(1)
              soup = BeautifulSoup(driver.page_source, "lxml")
              tr = soup.find('table').tbody.findAll('tr')
              column_rows=[]
              if len(tr) > 0:
                  for item in tr:
                      td = item.findAll('td')
                      th = item.find('th')
                      if len(td) > 0:
                         data =[th.text,td[0].text,td[1].text,td[2].text]
                         column_rows.append(data)
              
              
              return column_rows  

        except Exception as e:
              print("Error en get_rows " +str(e))

  

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    totalPaginas = input("Ingrese el total de paginas:")
    totalPaginas = int(totalPaginas) + 1
    rows=[]
    
    for i in range(1,totalPaginas):
        Url="https://www.ccpa.or.cr/buscar-ccpa/?_pagi_pg=" +str(i)
        driver.get(Url)
        table = Table(driver)
        data= table.get_rows()
        if data is not None:
            if len(data) > 0:
                for item in data:
                    rows.append(item)
        driver.forward()
         
    print(len(rows))
    if len(rows) > 0 :
        try:
            Encabezados =['Carnet','Cedula','Nombre','Estado']
            df = pd.DataFrame(rows, columns=Encabezados) 
            df.to_excel('C:\Pentaho\Lista-CCPA.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  

  
   