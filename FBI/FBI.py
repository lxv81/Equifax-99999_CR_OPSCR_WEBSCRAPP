

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

    def get_rows(self,nombre,titulo,item):
         try:
             fecha_nacimiento =''
             cabello =''
             ojos =''
             Altura =''
             peso =''
             sexo =''
             nacionalidad =''
             if item == 0:
                titulo = self.driver.find_element_by_class_name("summary").text

             tabla = self.driver.find_element_by_tag_name("table")
             tr= tabla.find_elements_by_tag_name("tr")
             if len(tr) > 0 :
                 for items in tr: 
                      td=items.find_elements_by_tag_name("td")
                      if td[0].text == 'Date(s) of Birth Used':
                             fecha_nacimiento =td[1].text

                      if td[0].text == 'Hair':
                             cabello =td[1].text

                      if td[0].text == 'Eyes':
                                    ojos =td[1].text

                      if td[0].text == 'Height':
                                    Altura =td[1].text

                      if td[0].text == 'Weight':
                                    peso =td[1].text

                      if td[0].text == 'Sex':
                                    sexo =td[1].text

                      if td[0].text == 'Nationality':
                                    nacionalidad =td[1].text

                 return [titulo,nombre,fecha_nacimiento,cabello,ojos,Altura,peso,sexo,nacionalidad] 
         except Exception as error :
                print("Error busco tabla" + str(error))


    def get_Datos(self, item):
        try:
            titulo= ''
            nombre= ''
            link = ''
            li= self.driver.find_elements_by_class_name("portal-type-person")
            column_rows=[]
            print(len(li))
            total = len(li)
            resul = total 
            links = []
            for element in range(0,resul): 
                lista= self.driver.find_elements_by_class_name("portal-type-person")
                info = lista[element]
                title= info.find_element_by_class_name("title")
                titulo= title.text
                if item != 0: 
                    name= info.find_element_by_class_name("name")
                    nombre= name.text
                    a = name.find_element_by_tag_name("a")
                    link= a.get_attribute("href")
                    links.append([nombre,titulo,link])

                else:
                    a = title.find_element_by_tag_name("a")
                    link= a.get_attribute("href")
                    links.append([titulo,'',link])
              
            return links  

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
    #Url="https://www.fbi.gov/wanted/fugitives"
    #driver.get(Url)
    table = Table(driver)
    time.sleep(1)
   # for i in range(0,3):
    Url = ''
    i = 1
    if i == 1:
        Url="https://www.fbi.gov/wanted/bank-robbers"  
       # if i == 0:
        #        Url="https://www.fbi.gov/wanted/topten"  
       # if i == 1:
        #        Url="https://www.fbi.gov/wanted/terrorism"
 #   if i == 2:
  #          Url="https://www.fbi.gov/wanted/bank-robbers"
      #  if i == 3:
         #   Url="https://www.fbi.gov/wanted/vicap"
      # if i == 4:
       #     Url="https://www.fbi.gov/wanted/fugitives"
        
        driver.get(Url)
        table.scroll() 
        time.sleep(4)
        rows= []
        Data = table.get_Datos(i)
        if Data is not None:
               if len(Data) > 0:
                   for item in Data:
                        driver.get(item[2])
                        info = table.get_rows(item[0],item[1],i)
                        if info is not None:
                            if len(info) > 0:
                                rows.append(info)
                        else:
                            rows.append([item[1],item[0],'','','','','','',''])
                        driver.back()

    Encabezados=['titulo','nombre','fecha_nacimiento','cabello','ojos','Altura','peso','sexo','nacionalidad']
    if len(rows) > 0 and len(Encabezados) > 0:
        try:
            df = pd.DataFrame(rows, columns=Encabezados) 
            df.to_excel('C:\Pentaho\FBI.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  

  