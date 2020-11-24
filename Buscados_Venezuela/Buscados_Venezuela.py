


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


    def get_rows(self,link):
        try:
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source, "lxml")
            gdp_table = soup.find_all("tr") 
            data = []
            nombre = ''
            cedula = ''
            Fecha_Nac = ''
            Edad =''
            Alias =''
            Banda =''
            lugar =''
            delitos =''
            contador = 0
            for tr in gdp_table:
                tds = tr.find_all('td')
                if len(tds) > 0:  
                        texto =tds[0].text.replace("\n", "")
                        texto =texto.replace("\xa0", "")
                        texto =texto.replace(": ", ":")
                        if texto == 'Nombre y Apellido:':
                              nombre =tds[1].text.replace("\n", "")

                        if texto == 'Cédula de Identidad:':
                              cedula =tds[1].text.replace("\n", "")

                        if texto == 'Fecha de Nacimiento:':
                               Fecha_Nac =tds[1].text.replace("\n", "")

                        if texto == 'Edad:':
                                Edad =tds[1].text.replace("\n", "")

                        if texto == 'Alias:':
                                Alias =tds[1].text.replace("\n", "")

                        if texto == 'Banda que Integra:':
                                Banda =tds[1].text.replace("\n", "")

                        if texto== 'Lugar donde Opera:':
                                lugar =tds[1].text.replace("\n", "")

                        if texto == 'Delitos Vinculados:':
                                delitos =tds[1].text.replace("\n", "")
                                delitos =delitos.replace("//", ",")
                                delitos =delitos.replace("||", ",")

            data=[nombre,cedula,Fecha_Nac,Edad,Alias,Banda,lugar,delitos,link]

            return data  

        except:
              print("An exception occurred get_rows")

 
                  
    def GetAllUrl(self):  
            try:
                 time.sleep(2)
                 ListaUrl =[]
                 main = driver.find_element_by_id("main")
                 lista = main.find_elements_by_class_name("category-mas-buscados")
               
                 if len(lista) > 0:
                     for item in lista:
                         a = item.find_element_by_tag_name('a')
                         url =a.get_attribute('href')
                         ListaUrl.append(url)
                 
                 return ListaUrl
        
            except:
                  print("An exception occurred GetAllUrl")
                  
    def Paginacion(self):  
            try:
                buton = driver.find_element_by_class_name("next")
                buton.click()
                return
        
            except:
                  print("An exception occurred Paginacion")
   

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="http://masbuscados.mijp.gob.ve/index.php/category/mas-buscados/"
    driver.get(Url)
    table = Table(driver)
    ListaUrls =[]
    rows=[]
    for i in range(2):
          Urls=table.GetAllUrl()
          if Urls is not None:
              if len(Urls) > 0:
                  for element in Urls:
                      ListaUrls.append(element)
          table.Paginacion()
    
    driver.forward()
    if ListaUrls is not None:
            if len(ListaUrls) > 0:
                for url in ListaUrls:
                     print(url)
                     driver.get(url)
                     table = Table(driver)   
                     data = table.get_rows(url)
                     if data is not None:
                         if len(data) > 0:
                             rows.append(data)
          
         
    driver.close()
    if len(rows) > 0:
        try:
            encabezados =['Nombre','Cedula','Fecha_Nac','Edad','Alias','Banda','lugar','delitos','link']
            df = pd.DataFrame(rows , columns=encabezados) 
            df.to_excel('C:\Pentaho\BuscadosVenezuela.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  

  
   