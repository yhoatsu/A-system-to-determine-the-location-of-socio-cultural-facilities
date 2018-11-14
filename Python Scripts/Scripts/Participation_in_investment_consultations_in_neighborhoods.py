
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json


# In[2]:


with open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Barrios.geojson') as json_data:
    d = json.load(json_data)
    json_data.close()


# In[3]:


tabla=pd.read_csv(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Tablas\Decidim\num_participación.csv',sep=';',dtype={'Product':str},engine="python", encoding="latin_1",header=None)


# In[5]:


participacion=[]
for i in range(0,len(tabla.ix[:,0])):
    participacion.append(tabla.ix[i][2])


# In[6]:


intervalos=list(range(0,max(participacion),int(round(max(participacion)/5))))


# In[7]:


intervalos


# In[8]:


for i in range(0,len(d['features'])):
    cod=int(d['features'][i]['properties']['coddistbar'])
    num_votos=int(tabla[tabla[0]==cod][2])
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


# In[11]:


archivo = open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\votos_decidim.geojson','w')
json.dump(d, archivo)
archivo.close()

