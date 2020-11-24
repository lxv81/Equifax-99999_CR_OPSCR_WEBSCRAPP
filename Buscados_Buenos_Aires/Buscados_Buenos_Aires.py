

# -*- coding: utf-8 -*-
"""
Created on monday nov 19 2020

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
            table = soup.find("table") 
            Lista_tr = table.find_all("tr") 
            data = []
            Nombre = ''
            Alias = ''
            DNI = ''
            Fecha_Nac = ''
            Lugar_Nac = ''
            Sexo = ''
            Nombre_Padre = ''
            Nombre_Madre = ''
            Domicilio = ''
            Delito = ''

            contador = 0 
            for item in Lista_tr:
                contador = contador + 1 
                tds= item.find_all("td")
                if contador == 3:
                    Nombre = tds[1].text.replace("\n","")
                    Nombre = tds[1].text.replace(","," ")
                    Nombre = Nombre.replace("\xa0","")
                    Nombre = Nombre.strip()
                    Alias = tds[3].text.replace("\n","")
                    Alias = Alias.replace("\xa0","")
                    Alias = Alias.strip()

                if contador == 4:
                    if len(tds) == 4:                   
                        DNI  = tds[1].text.replace("\n","")
                        DNI = DNI.replace("\xa0","")
                        DNI = DNI.strip()
                        Fecha_Nac = tds[3].text.replace("\n","")
                        Fecha_Nac = Fecha_Nac.replace("\xa0","")
                        Fecha_Nac = Fecha_Nac.strip()
                    else:
                        contador = 3
                      
                if contador == 5:
                    Lugar_Nac = tds[1].text.replace("\n","")
                    Lugar_Nac = Lugar_Nac.replace("\xa0","")
                    Lugar_Nac = Lugar_Nac.strip()
                    Sexo = tds[3].text.replace("\n","")
                    Sexo = Sexo.replace("\xa0","")
                    Sexo = Sexo.strip()

                if contador == 6:
                    Nombre_Padre = tds[3].text.replace("\n","")
                    Nombre_Padre = Nombre_Padre.replace("\xa0","")
                    Nombre_Padre = Nombre_Padre.strip()

                if contador == 7:
                    Nombre_Madre = tds[1].text.replace("\n","")
                    Nombre_Madre = Nombre_Madre.replace("\xa0","")
                    Nombre_Madre = Nombre_Madre.strip()

                if contador == 9:
                    Domicilio = tds[3].text.replace("\n","")
                    Domicilio = Domicilio.replace("\xa0","")
                    Domicilio = Domicilio.strip()

                if contador == 10:
                    Delito = tds[3].text.replace("\n","")
                    Delito = Delito.replace("\xa0","")
                    Delito = Delito.strip()
         
       

            data=[Nombre,Alias,DNI,Fecha_Nac,Lugar_Nac,Sexo,Domicilio,Delito,link]

            return data  

        except Exception as e:
              print("Error get_rows " + str(e))

 
                  
    def GetAllUrl(self):  
            try:
                 time.sleep(2)
                 ListaUrl =[]
                 lista = driver.find_elements_by_tag_name("tr")
                 print(len(lista))
                 if len(lista) > 0:
                     for item in lista:
                         td = item.find_element_by_tag_name('td')
                         a = td.find_element_by_tag_name('a')
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
    Url="https://profugos.mseg.gba.gov.ar/Profugos.aspx?idDelito=5&idTipoProfugo=1"
    driver.get(Url)
    table = Table(driver)
    ListaUrls =[]
    rows=[]
    ListaUrls=table.GetAllUrl()

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
            encabezados =['Nombre','Alias','DNI','Fecha_Nac','Lugar_Nac','Sexo','Domicilio','Delito','link']
            df = pd.DataFrame(rows , columns=encabezados) 
            df.to_excel('C:\Pentaho\Buscados_BuenoAires.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  

  
   