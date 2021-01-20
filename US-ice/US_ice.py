


# -*- coding: utf-8 -*-
"""
Created on Sat oct 23 20:50:40 2020

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
             nombre =''
             alias = ''
             cabello =''
             ojos =''
             Altura =''
             peso =''
             sexo =''
             pais =''
             wantedfor = self.driver.find_elements_by_class_name("field--name-field-wanted-for")
             if len(wantedfor) > 0:
                 delito =wantedfor[0].text

             name = self.driver.find_elements_by_class_name("field--name-field-most-wanted-name")
             if len(name) > 0 :
                 nombre =name[0].text
                 nombre = nombre.replace("NAME","")

             Gender = self.driver.find_elements_by_class_name("field--name-field-gender")
             if len(Gender) > 0 :
                 sexo =Gender[0].text
                 sexo = sexo.replace("GENDER","")

             aliass = self.driver.find_elements_by_class_name("field--name-field-most-wanted-alias")
             if len(aliass) > 0 :
                 alias =aliass[0].text
                 alias = alias.replace("ALIAS","")

             PlaceBirth = self.driver.find_elements_by_class_name("field--name-field-place-of-birth")
             if len(PlaceBirth) > 0 :
                 pais =PlaceBirth[0].text
                 pais = pais.replace("PLACE OF BIRTH","")

             height = self.driver.find_elements_by_class_name("field--name-field-height")
             if len(height) > 0 :
                 Altura =height[0].text
                 Altura = Altura.replace("HEIGHT","")

             weight = self.driver.find_elements_by_class_name("field--name-field-weight")
             if len(weight) > 0 :
                 peso =weight[0].text
                 peso = peso.replace("WEIGHT","")

             eyes = self.driver.find_elements_by_class_name("field--name-field-eyes")
             if len(eyes) > 0 :
                 ojos =eyes[0].text
                 ojos = ojos.replace("EYES","")

             hair = self.driver.find_elements_by_class_name("field--name-field-hair")
             if len(hair) > 0 :
                 cabello =hair[0].text
                 cabello = cabello.replace("HAIR","")
             return [nombre,delito,alias,cabello,ojos,Altura,peso,sexo,pais] 
         except Exception as error :
                print("Error busco tabla" + str(error))


    def get_Urls(self):
        try:
             ul=  driver.find_element_by_xpath('//*[@id="blazy-views-most-wanted-block-1-1"]')
             li = ul.find_elements_by_tag_name("li")
             ListaLinks =[]
             
             for item in li:
                a = item.find_element_by_tag_name("a")
                link= a.get_attribute("href")
                ListaLinks.append(link)
              
             return ListaLinks  

        except Exception as e:
              print("Error en get_Datos " +str(e))

    def scroll(self):
            SCROLL_PAUSE_TIME = 1
            last_height = self.driver.execute_script("return document.body.scrollHeight")

            while True:
    # Scroll down to bottom
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                   break
                last_height = new_height
   

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="https://www.ice.gov/most-wanted#wcm-survey-target-id"
    driver.get(Url)
    table = Table(driver) 
        
    time.sleep(3)
    rows= []
    Data = table.get_Urls()
    if Data is not None:
       if len(Data) > 0:
          for item in Data:
            driver.get(item)
            info = table.get_rows()
            if info is not None:
               if len(info) > 0:
                   rows.append(info)
            driver.forward()

    driver.close()   
    Encabezados=['nombre','delito','alias','cabello','ojos','Altura','peso','sexo','pais']
    if len(rows) > 0 and len(Encabezados) > 0:
        try:
            df = pd.DataFrame(rows, columns=Encabezados) 
            df.to_excel('C:\Pentaho\Ice.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  

  