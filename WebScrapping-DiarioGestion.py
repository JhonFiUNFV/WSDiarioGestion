# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# WEB SCRAPPING

#EJEMPLO 1: Importar una página en bruto
#Ej. Diario Gestión


%reset -f
from bs4 import BeautifulSoup
import requests
import urllib.request

#url
web = 'https://gestion.pe/'
codigo = requests.get(web)
codigo 
raw = BeautifulSoup(codigo.content)
raw #usualmente se le llama soup
raw = BeautifulSoup(codigo.text, "html.parser")
raw

import webbrowser
webbrowser.open(web)

#ahora a inspeccionar CONTROL +SHIFT + I

web = 'https://gestion.pe/ultimas-noticias/'
codigo = requests.get(web)
codigo 
raw = BeautifulSoup(codigo.content)
raw #usualmente se le llama soup
raw = BeautifulSoup(codigo.text, "html.parser")
raw 
print(raw.prettify())

###identificando objetos
time.sleep(l)
raw.findAll()
raw.findAll('p')
raw.findAll('a')
raw.findAll('h2')
raw.findAll('h3')
raw.findAll('h4')
raw.findAll('picture')
raw.findAll('img')
raw.findAll('div')
raw.findAll('td')
raw.findAll('table')

parrafo_raw = raw.findAll('p')[5]
parrafo_raw
type(parrafo_raw)
parrafo_str = str(parrafo_raw)
type(parrafo_str)
parrafo = parrafo_str[122:]
parrafo
#nota, en este caso vale para impares

#bucle

noticias = []
for x in range (1,50):
    parrafo_raw = raw.findAll('p')[x]
    parrafo_raw
    type(parrafo_raw)
    parrafo_str = str(parrafo_raw)
    type(parrafo_str)
    parrafo= parrafo_str[122:-4]
    
    noticias.append(parrafo)
    
noticias

del noticias[1::2]

from pandas import DataFrame
df = DataFrame (noticias, columns=['Titulares'])
print(df)

import datetime
now = datetime.datetime.now()
df = DataFrame (noticias, columns=['Titulares del diario Gestión al' + now.strftime("%Y-%m-%d %H:%M:%S")])
print(df)
df

#### Extracción del link

link36 = raw.findAll('a')[36]
link36
link = link36['href']
link
link = 'https://gestion.pe/' + link36['href']
link
type(link)
import webbrowser
webbrowser.open(link)

### Extracción 
raw.findAll('img')
imagen36 = raw.findAll('img')[10]
imagen36
imagen = imagen36['src']
type(imagen)
import webbrowser
webbrowser.open(imagen)







