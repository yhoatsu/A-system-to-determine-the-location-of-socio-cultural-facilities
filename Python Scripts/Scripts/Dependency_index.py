
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import json


# In[3]:


with open(r'D:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Barrios.geojson') as json_data:
    d = json.load(json_data)
    json_data.close()


# In[4]:


tabla=pd.read_csv(r'D:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Tablas\Padrón\poblacion_grupos.csv',sep=';',dtype={'Product':str},engine="python", encoding="latin_1")


# In[4]:


tabla.ix[:,0].str.split(" ")[0][0].replace('.','')


# In[6]:


aux=[]
for i in range(0,len(tabla.ix[:,0].str.split(" "))):
    cod=tabla.ix[:,0].str.split(" ")[i][0].replace('.','')
    if len(cod)==2:
        aux.append('0'+cod)
    else:
        aux.append(cod)


# In[8]:


tabla.insert(0,'coddistbar',aux)


# In[9]:


indice_dep=[]
for i in range(0,len(tabla.ix[:,0])):
    indice_dep.append((tabla.ix[i]['65 y más']+tabla.ix[i]['0-15'])/tabla.ix[i]['16-64'])


# In[10]:


tabla.insert(1,'Indice dependencia',indice_dep)


# In[31]:


for k in range(0,len(d['features'])):
    cod=d['features'][k]['properties']['coddistbar']
    d['features'][k]['properties']['inddep']=float(tabla[tabla['coddistbar']==cod]['Indice dependencia'])


# In[32]:


for i in range(0,len(d['features'])):
    if 0<=d['features'][i]['properties']['inddep']<0.25:
        d['features'][i]['properties']['raster']=100
    elif 0.25<=d['features'][i]['properties']['inddep']<0.5:
        d['features'][i]['properties']['raster']=80
    elif 0.5<=d['features'][i]['properties']['inddep']<0.75:
        d['features'][i]['properties']['raster']=60
    elif 0.75<=d['features'][i]['properties']['inddep']<1:
        d['features'][i]['properties']['raster']=40
    elif 1<=d['features'][i]['properties']['inddep']:
        d['features'][i]['properties']['raster']=20  


# In[43]:


archivo = open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\indice_dep.geojson','w')
json.dump(d, archivo)
archivo.close()

