
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
            Lista_labels = soup.find_all("p") 
            data = []
            Causa = ''
            Organismo_Requirente = ''
            Fecha_Busqueda = ''
            Hechos =''
            Calificación_Legal =''
            Genero =''
            Apellidos =''
            Nombres =''
            Alias = ''
            Fecha_Nacimiento = ''
            Lugar_Nacimiento = ''
            Edad_Presunta = ''
            Documento = ''
            parrafo1 =list(Lista_labels[1].text.split("\n")) 
            parrafo2 =list(Lista_labels[2].text.split("\n")) 
            print(len(parrafo1))
            print(len(parrafo2))
            Causa =parrafo1[2]
            Organismo_Requirente =parrafo1[5]
            Fecha_Busqueda =parrafo1[8]
            Hechos =parrafo1[11]
            Calificación_Legal =parrafo1[14]
            if len(parrafo2) == 24:
                Genero =parrafo2[2]
                Apellidos =parrafo2[5]
                Nombres =parrafo2[8]
                Alias =parrafo2[11]
                Documento =parrafo2[13]
                Fecha_Nacimiento =parrafo2[16]
                Lugar_Nacimiento =parrafo2[19]
                Edad_Presunta =parrafo2[22]

            if len(parrafo2) == 25:
                Genero =parrafo2[2]
                Apellidos =parrafo2[5]
                Nombres =parrafo2[8]
                Alias =parrafo2[11]
                Documento =parrafo2[14]
                Fecha_Nacimiento =parrafo2[17]
                Lugar_Nacimiento =parrafo2[20]
                Edad_Presunta =parrafo2[23]

            data=[Causa,Organismo_Requirente,Fecha_Busqueda,Hechos,Calificación_Legal,Genero,Apellidos,Nombres,Alias,Documento,Fecha_Nacimiento,Lugar_Nacimiento,Edad_Presunta,link]

            return data  

        except:
              print("An exception occurred get_rows")

 
                  
    def GetAllUrl(self):  
            try:
                 time.sleep(2)
                 ListaUrl =[]
                 lista = driver.find_elements_by_class_name("panel-footer")
                 print(len(lista))
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
    Url="http://www.dnrec.jus.gov.ar/masbuscados#"
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
            encabezados =['Causa','Organismo_Requirente','Fecha_Busqueda','Hechos','Calificación_Legal','Genero','Apellidos','Nombres','Alias','Documento','Fecha_Nacimiento','Lugar_Nacimiento','Edad_Presunta','link']
            df = pd.DataFrame(rows , columns=encabezados) 
            df.to_excel('C:\Pentaho\Buscados_NRN.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  

  
   