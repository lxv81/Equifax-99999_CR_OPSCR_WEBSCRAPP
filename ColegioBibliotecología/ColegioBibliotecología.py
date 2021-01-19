


# -*- coding: utf-8 -*-
"""
Created on monday january 12 2021

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
            soup = BeautifulSoup(driver.page_source, "lxml")
            gdp_table = soup.find("table", attrs={"id": "footable_8084"})
            gdp_table_data = gdp_table.tbody.find_all("tr")  # contains 2 rows      
            lista = []
            apellido1 = ''
            apellido2 = ''
            nombre = ''
            carnet =''
            cedula =''
            condicion =''
            for tr in gdp_table_data:
                tds = tr.find_all('td')
                if len(tds) > 0: 
                        apellido1 = tds[0].text.strip()
                        apellido2 = tds[1].text.strip()
                        nombre = tds[2].text.strip()
                        carnet = tds[3].text.strip()
                        cedula = tds[4].text.strip()
                        condicion = tds[5].text.strip()
                        data=[apellido1,apellido2,nombre,carnet,cedula,condicion]
                        lista.append(data)   
                   
            return lista  

        except Exception as e:
              print("Error obtener filas :" + str(e))


    def TotalPaginas(self):
         try:
             ul = self.driver.find_element_by_xpath('//*[@id="footable_8084"]/tfoot/tr/td/div/ul')
             li = ul.find_elements_by_tag_name("li")
             total = 0
             if len(li) > 0:
                ultima = li[-1].find_element_by_tag_name("a")
                ultima.click()
                total = int(li[-4].text)
                primera = li[0].find_element_by_tag_name("a")
                primera = primera.click()
             return  total
         except Exception as e:
                  print("Error TotalPaginas :" + str(e))

    def Siguiente(self):
         try:
             ul = self.driver.find_element_by_xpath('//*[@id="footable_8084"]/tfoot/tr/td/div/ul')
             li = ul.find_elements_by_tag_name("li")
             if len(li) > 0:
                siguiente = li[-2].find_element_by_tag_name("a")
                siguiente.click()
             return  
         except Exception as e:
                  print("Error siguiente :" + str(e))
   

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="https://coprobi.co.cr/colegiados/directorio/"
    driver.get(Url)
    table = Table(driver)

    time.sleep(7)
    total= table.TotalPaginas()
    rows=[]
    time.sleep(1)
    for x in range(total):
       data = table.get_rows()
       if data is not None:
          if len(data) > 0:
             for item in data:
                 rows.append(item)
             table.Siguiente()

          
         
    driver.close()
    if len(rows) > 0:
        try:
            encabezados =['Apellido1','Apellido2','Nombre','Carnet', 'Cedula', 'Condicion']
            df = pd.DataFrame(rows , columns=encabezados) 
            df.to_excel('C:\Pentaho\Bibliotecnologia.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  

  
   