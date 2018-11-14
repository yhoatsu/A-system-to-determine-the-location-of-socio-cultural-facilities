
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json


# In[2]:


with open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Barrios.geojson') as json_data:
    d = json.load(json_data)
    json_data.close()


# In[5]:


tabla=pd.read_csv(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Tablas\Cheques escolares\cheques.csv',sep=';',dtype={'Product':str},engine="python", encoding="latin_1")


# In[7]:


aux=[]
for i in range(0,len(tabla.ix[:,0].str.split(" "))):
    cod=tabla.ix[:,0].str.split(" ")[i][0].replace('.','')
    if len(cod)==2:
        aux.append('0'+cod)
    else:
        aux.append(cod)


# In[8]:


tabla.insert(0,'coddistbar',aux)


# In[10]:


solicitudes=[]
for i in range(0,len(tabla.ix[:,0])):
    solicitudes.append(tabla.ix[i]['Solicitantes'])


# In[12]:


intervalos=list(range(0,max(solicitudes),int(round(max(solicitudes)/5))))


# In[22]:


intervalos


# In[24]:


for i in range(0,len(d['features'])):
    cod=d['features'][i]['properties']['coddistbar']
    num_votos=int(tabla[tabla['coddistbar']==cod]['Solicitantes'])
    if intervalos[0]<=num_votos<intervalos[1]:
        d['features'][i]['properties']['raster']=100
    elif intervalos[1]<=num_votos<intervalos[2]:
        d['features'][i]['properties']['raster']=80
    elif intervalos[2]<=num_votos<intervalos[3]:
        d['features'][i]['properties']['raster']=60
    elif intervalos[3]<=num_votos<intervalos[4]:
        d['features'][i]['properties']['raster']=40
    elif intervalos[4]<=num_votos<intervalos[5]:
        d['features'][i]['properties']['raster']=20
    elif intervalos[5]<num_votos:
        d['features'][i]['properties']['raster']=0


# In[31]:


archivo = open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\cheques.geojson','w')
json.dump(d, archivo)
archivo.close()

