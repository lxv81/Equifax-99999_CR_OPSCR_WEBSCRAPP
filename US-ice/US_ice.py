


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
             delito = self.driver.find_element_by_class_name("wanted-for").text

             tabla = self.driver.find_element_by_tag_name("table")
             tr= tabla.find_elements_by_tag_name("tr")
             if len(tr) > 0 :
                 for items in tr: 
                      td=items.find_elements_by_tag_name("td")
                      if td[0].text == 'Name':
                             nombre =td[1].text

                      if td[0].text == 'Hair':
                             cabello =td[1].text

                      if td[0].text == 'Eyes':
                                    ojos =td[1].text

                      if td[0].text == 'Height':
                                    Altura =td[1].text

                      if td[0].text == 'Weight':
                                    peso =td[1].text

                      if td[0].text == 'Gender':
                                    sexo = td[1].text

                      if td[0].text == 'Place of Birth':
                                    pais =td[1].text

                      if td[0].text == 'Alias':
                                    alias =td[1].text

                 return [nombre,delito,alias,cabello,ojos,Altura,peso,sexo,pais] 
         except Exception as error :
                print("Error busco tabla" + str(error))


    def get_Datos(self,item):
        try:
            titulo= ''
            nombre= ''
            link = ''
            if item == 0:
                lista = driver.find_element_by_xpath('//*[@id="node-page-31970"]/div/div/div[1]')
            if item == 1:
               lista = driver.find_element_by_xpath('//*[@id="node-page-31970"]/div/div/div[2]')

            if item == 2:
                lista = driver.find_element_by_xpath('//*[@id="node-page-31970"]/div/div/div[3]')

            if item == 3:
               lista = driver.find_element_by_xpath('//*[@id="node-page-31970"]/div/div/div[4]')

            li = lista.find_elements_by_tag_name("div")
            print(len(li))
            total = len(li)
            resul = total 
            links = []
            for element in li: 
                try:
                     p = element.find_elements_by_tag_name("p")
                     a = element.find_element_by_tag_name("a")
                     link= a.get_attribute("href")
                     print(link)
                     links.append(link)
                except Exception as e :
                   print("Error" +str(e))
               
              
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
    Url="https://www.ice.gov/most-wanted#wcm-survey-target-id"
    driver.get(Url)
    table = Table(driver)
    time.sleep(1)
    for i in range(3,4):
        ul=  driver.find_element_by_class_name("item-list")
        li = ul.find_elements_by_tag_name("li")
        if i == 1:
            ul=  driver.find_element_by_class_name("item-list")
            li = ul.find_elements_by_tag_name("li")
            a= li[1].find_element_by_tag_name("a")
            a.click()
            
        if i == 2:
            ul=  driver.find_element_by_class_name("item-list")
            li = ul.find_elements_by_tag_name("li")
            a= li[2].find_element_by_tag_name("a")
            a.click()
        if i == 3:
            ul=  driver.find_element_by_class_name("item-list")
            li = ul.find_elements_by_tag_name("li")
            a= li[3].find_element_by_tag_name("a")
            a.click()

        
        time.sleep(3)
        rows= []
        Data = table.get_Datos(i)
        if Data is not None:
               if len(Data) > 0:
                   for item in Data:
                        driver.get(item)
                        info = table.get_rows()
                        if info is not None:
                            if len(info) > 0:
                                rows.append(info)
                        else:
                            rows.append([item[1],item[0],'','','','','','',''])
                        driver.back()

        
    Encabezados=['nombre','delito','alias','cabello','ojos','Altura','peso','sexo','pais']
    if len(rows) > 0 and len(Encabezados) > 0:
        try:
            df = pd.DataFrame(rows, columns=Encabezados) 
            df.to_excel('C:\Pentaho\Ice.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')

  

  