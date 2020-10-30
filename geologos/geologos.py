


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

         
    def get_Emcabezados(self):
        try:
            column_info=["Codigo","Nombre","Especialidad","Estado"]            
            return column_info
        except:
              print("An exception occurred get_Emcabezados")
    
    def get_MiembrosMeritos(self):
        try:       
             table = self.driver.find_element_by_id("tab-1-2-miembrosemeritos")    
             p = table.find_elements_by_tag_name('p')    
             lista1=p[1]
             data= lista1.text.replace("\n",",")
             Lista = data.split(",")
             return  Lista

        except:
              print("An exception occurred get_rows")


    def get_Especialidades(self):
        try:       
             table = self.driver.find_element_by_id("tab-1-3-especialidadesreconocidas")    
             h4 = table.find_elements_by_tag_name('h4')    
             p = table.find_elements_by_tag_name('p')  
             tr = table.find_elements_by_tag_name('tr')  
             listah4=[]
             listaP=[]
             listatd=[]
             ListaFin=[]
             for item in p:
                  data= item.text.replace("\n",",")
                  Lista = data.split(",")
                  listaP.append(Lista)

             for item in h4:
                 listah4.append(item.text)

             for item in tr:
                  td= item.find_elements_by_tag_name('td') 
                  for tds in td:
                       listatd.append(tds.text)
            
                      
             
             listah4.pop(0)
             for item in listah4:
                      if item == 'Hidrogeología':
                           for ite in listatd:   
                                 data=[ite,item]
                                 ListaFin.append(data)

                     
                      if item == 'Geología Estructural':
                               data=  p[0].text.replace("\n",",")
                               Lista = data.split(",")
                               for element in Lista:
                                    d=[element,item]
                                    ListaFin.append(d)

                      if item == 'Gestión del Riesgo':
                               data=  p[1].text.replace("\n",",")
                               Lista = data.split(",")
                               for element in Lista:
                                    d=[element,item]
                                    ListaFin.append(d)


                      if item == 'Neotectónica':
                                  data=  p[2].text.replace("\n",",")
                                  Lista = data.split(",")
                                  for element in Lista:
                                           d=[element,item]
                                           ListaFin.append(d)

                      if item == 'Geología del Cuaternario':
                                  data=  p[3].text.replace("\n",",")
                                  Lista = data.split(",")
                                  for element in Lista:
                                           d=[element,item]
                                           ListaFin.append(d)




                      if item == 'Geofísica':
                                  data=  p[4].text.replace("\n",",")
                                  Lista = data.split(",")
                                  for element in Lista:
                                           d=[element,item]
                                           ListaFin.append(d)


                      if item == 'Geotécnia':
                                  data=  p[5].text.replace("\n",",")
                                  Lista = data.split(",")
                                  for element in Lista:
                                           d=[element,item]
                                           ListaFin.append(d)


                      if item == 'Minería':
                                  data=  p[6].text.replace("\n",",")
                                  Lista = data.split(",")
                                  for element in Lista:
                                           d=[element,item]
                                           ListaFin.append(d)



                      if item == 'Sismología':
                                  data=  p[7].text.replace("\n",",")
                                  Lista = data.split(",")
                                  for element in Lista:
                                           d=[element,item]
                                           ListaFin.append(d)



                      if item == 'Vulcanología':
                                  data=  p[8].text.replace("\n",",")
                                  Lista = data.split(",")
                                  for element in Lista:
                                           d=[element,item]
                                           ListaFin.append(d)



                      if item == 'Paleontología de Vertebrados':
                                  data=  p[9].text.replace("\n",",")
                                  Lista = data.split(",")
                                  for element in Lista:
                                           d=[element,item]
                                           ListaFin.append(d)


                      if item == 'Historia de la Geología':
                                  data=  p[10].text.replace("\n",",")
                                  Lista = data.split(",")
                                  for element in Lista:
                                           d=[element,item]
                                           ListaFin.append(d)

                      if item == 'Contaminación Ambiental':
                                                      data=  p[11].text.replace("\n",",")
                                                      Lista = data.split(",")
                                                      for element in Lista:
                                                               d=[element,item]
                                                               ListaFin.append(d)



                      if item == 'Saneamiento del medio soportante con énfasis en diseño, ejecución y control de calidad, en el mejoramiento del medio soportante por medio de inyecciones de lechada':
                                        data=  p[12].text.replace("\n",",")
                                        Lista = data.split(",")
                                        for element in Lista:
                                              d=[element,item]
                                              ListaFin.append(d)

                      if item == 'Geotermia':
                                        data=  p[13].text.replace("\n",",")
                                        Lista = data.split(",")
                                        for element in Lista:
                                              d=[element,item]
                                              ListaFin.append(d)


                      if item == 'Historia de las Geociencias':
                               data=  p[14].text.replace("\n",",")
                               Lista = data.split(",")
                               for element in Lista:
                                      d=[element,item]
                                      ListaFin.append(d)


                      if item == 'Karstología':
                                   data=  p[15].text.replace("\n",",")
                                   Lista = data.split(",")
                                   for element in Lista:
                                            d=[element,item]
                                            ListaFin.append(d)


             return  ListaFin

        except Exception as e:
              print("An exception occurred get_Especialidades"+str(e))




            

    def get_GeologosActivos(self):
        try:       
             table = self.driver.find_element_by_id("tab-1-0-miembrosactivos")
             clase = table.find_element_by_class_name("row")
             div = clase.find_elements_by_tag_name("div")       
             lista=[]
             for item in div:
                    rows=item.find_elements_by_tag_name('p') 
                    for element in rows:
                        lista.append(element.text)
                   
             return lista 

        except:
              print("An exception occurred get_rows")

if "__main__" == __name__:
    PATH = "C:\Pentaho\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(2)
    Url="http://www.geologos.or.cr/agremiados-2/"
   
    driver.get(Url)
    table = Table(driver)
    rows=[]
    Especialistas=[]
    Suspendidos=[]
    Pencionados=[]
    time.sleep(5)
    # Miembros Activos
    listaActivos =table.get_GeologosActivos()
    
   # Miembros Emeritos
    driver.find_element_by_id("ui-id-3").click()
    time.sleep(4)
    ListaMeritos=table.get_MiembrosMeritos()

   # print(listaActivos)
    time.sleep(3)
    # Miembros Emeritos
    driver.find_element_by_id("ui-id-4").click()
    #time.sleep(4)
    ListaEspecialidades= table.get_Especialidades()
    time.sleep(3)
    ListaDefinitiva=[]
    Listas=[]
    for item in ListaMeritos:
           Listas.append([item,'Geologo(a)','Emeritos','Activo'])

    for item in ListaEspecialidades:
           Nombre=item[0]
           E=item[1]
           Listas.append([Nombre,'Geologo(a)',E,'Activo'])



    ListaNombres=[]
    for item in listaActivos:
        contador=0
        for ite in Listas:
            if item.upper() == ite[0].upper():
                contador=1
                ListaDefinitiva.append(ite)
                ListaNombres.append(item)
                break
           
        if contador == 0:
             ListaDefinitiva.append([item,'Geologo(a)','','Activo'])
             ListaNombres.append(item)
           
                


    for item in Listas:
        nombre=item[0]
        if nombre not in ListaNombres: 
                  ListaDefinitiva.append(item)
               
   
               
    print(ListaDefinitiva)
   
    if len(ListaDefinitiva) > 0 :
        try:
            df = pd.DataFrame(data=ListaDefinitiva) 
            df.to_excel('C:\Pentaho\listaGeologos.xlsx',index=False)

        except:
                print("Error en escribir en el excel")
    else:
        print('ocurrio un error')