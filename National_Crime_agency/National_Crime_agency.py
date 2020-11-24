



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


    def get_rows(self):
        try:
            time.sleep(2)
            nombre = ''
            Location = ''
            Crime = ''
            Sex = ''
            Height = ''
            Hair_Colour = ''
            contador = 0
            bandera1 = False
            bandera2 = False
            bandera3 = False
            bandera4 = False
            bandera5 = False

            soup = BeautifulSoup(driver.page_source, "lxml")
            mydivs = soup.findAll("div", {"class": "most-wanted-customfields"})
            nombre = soup.find("div", {"class": "page-header"}).text
            nombre = nombre.replace("\n","")
            nombre = nombre.replace("\t","")
            data = []

            if len(mydivs) > 0:
                for div in mydivs:
                    span = div.find_all('span')
                    if len(span) > 0:  
                       for element in span:
                            if bandera1:
                                 Location = element.text 
                                 bandera1 = False

                            if element.text == 'Location: ' and bandera1 == False:
                             bandera1 = True

                            if bandera2:
                                 Crime = element.text 
                                 bandera2 = False

                            if element.text == 'Crime: ' and bandera2 == False:
                             bandera2 = True

                            if bandera3:
                                 Sex = element.text 
                                 bandera3 = False

                            if element.text == 'Sex: ' and bandera3 == False:
                             bandera3 = True

                            if bandera4:
                                 Height = element.text.replace("'",' ') 
                                 bandera4 = False

                            if element.text == 'Height: ' and bandera4 == False:
                             bandera4 = True

                            if bandera5:
                                 Hair_Colour = element.text 
                                 bandera5 = False

                            if element.text == 'Hair Colour: ' and bandera5 == False:
                             bandera5 = True

                           
                          

            data=[nombre,Location,Crime,Sex,Height,Hair_Colour]

            return data  

        except:
              print("An exception occurred get_rows")

 
                  
    def GetAll(self):  
            try:
                 time.sleep(2)
                 LoadMore = self.driver.find_element_by_class_name("load-more")
                 LoadMore.click()
                 lista =[]
                 time.sleep(3)
                 lista = self.driver.find_elements_by_class_name("image-overlay")
                 return lista
        
            except Exception as e:
                  print("Error en GetAll " + str(e))
                  
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
    Url="https://www.nationalcrimeagency.gov.uk/most-wanted-search"
    driver.get(Url)
    table = Table(driver)
    Lista =[]
    rows=[]
    ##Lista=table.GetAll()
    #total = len(Lista)
    for i in range(22):
        elemento = table.GetAll()
        if elemento is not None:
           if len(elemento) > 0:
              elemento[i].click()
              data = table.get_rows()
              if data is not None:
                  if len(data) > 0:
                       rows.append(data)
              driver.back()
          
         
    driver.close()
    if len(rows) > 0:
        try:
            print(rows)
            encabezados = ['nombre','Location','Crime','Sex','Height','HairColour']
            df = pd.DataFrame(rows , columns=encabezados) 
            df.to_excel('C:\Pentaho\BuscadosVenezue.xlsx',index=False)

        except Exception as e:
                print("Error en escribir en el excel " + str(e))
    else:
        print('ocurrio un error')

  

  
   