
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


tabla=pd.read_csv(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Tablas\Elecciones\elecciones.csv',sep=';',dtype={'Product':str},engine="python", encoding="latin_1")


# In[8]:


aux=[]
for i in range(0,len(tabla.ix[:,0].str.split(" "))):
    cod=tabla.ix[:,0].str.split(" ")[i][0].replace('.','')
    if len(cod)==2:
        aux.append('0'+cod)
    else:
        aux.append(cod)


# In[9]:


tabla.insert(0,'coddistbar',aux)


# In[11]:


participacion=[]
for i in range(0,len(tabla)):
    participacion.append((tabla.ix[i]['Número de votos total']/tabla.ix[i]['Censo Electoral']))


# In[12]:


tabla.insert(1,'participacion',participacion)


# In[86]:


intervalos=np.linspace(0,max(participacion)-0.0001,5)


# In[87]:


for i in range(0,len(d['features'])):
    cod=d['features'][i]['properties']['coddistbar']
    num_votos=float(tabla[tabla['coddistbar']==cod]['participacion'])
    if intervalos[0]<=num_votos<intervalos[1]:
        d['features'][i]['properties']['raster']=20
    elif intervalos[1]<=num_votos<intervalos[2]:
        d['features'][i]['properties']['raster']=40
    elif intervalos[2]<=num_votos<intervalos[3]:
        d['features'][i]['properties']['raster']=60
    elif intervalos[3]<=num_votos<intervalos[4]:
        d['features'][i]['properties']['raster']=80
    elif intervalos[4]<num_votos:
        d['features'][i]['properties']['raster']=100   


# In[62]:


intervalos


# In[88]:


raster=[]
for i in range(len(d['features'])):
    if d['features'][i]['properties']['coddistbar']!='175' and d['features'][i]['properties']['coddistbar']!='198':
        raster.append(d['features'][i]['properties']['raster'])


# In[89]:


media_raster=int(np.median(raster))


# In[90]:


for i in range(len(d['features'])):
    if d['features'][i]['properties']['coddistbar']=='175' or d['features'][i]['properties']['coddistbar']=='198':
        d['features'][i]['properties']['raster']=media_raster


# In[91]:


archivo = open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\votos_municipales.geojson','w')
json.dump(d, archivo)
archivo.close()

