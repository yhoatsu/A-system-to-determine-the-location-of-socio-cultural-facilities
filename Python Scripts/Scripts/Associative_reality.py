
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json


# In[2]:


with open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\raster_barrios_asociaciones.geojson') as json_data:
    d = json.load(json_data)
    json_data.close()


# In[3]:


d['features'][0]['properties']


# In[4]:


asociaciones=[]
for i in range(0,len(d['features'])):
    asociaciones.append(d['features'][i]['properties']['asociaciones'])


# In[5]:


intervalos=list(range(0,max(asociaciones),int(round(max(asociaciones)/5))))


# In[15]:


intervalos


# In[8]:


for i in range(0,len(d['features'])):
    if intervalos[0]<=d['features'][i]['properties']['asociaciones']<intervalos[1]:
        d['features'][i]['properties']['raster']=20
    elif intervalos[1]<=d['features'][i]['properties']['asociaciones']<intervalos[2]:
        d['features'][i]['properties']['raster']=40
    elif intervalos[2]<=d['features'][i]['properties']['asociaciones']<intervalos[3]:
        d['features'][i]['properties']['raster']=60
    elif intervalos[3]<=d['features'][i]['properties']['asociaciones']<intervalos[4]:
        d['features'][i]['properties']['raster']=80
    elif intervalos[4]<d['features'][i]['properties']['asociaciones']:
        d['features'][i]['properties']['raster']=100    


# In[14]:


d['features'][5]['properties']


# In[16]:


archivo = open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\barrios_asociaciones.geojson','w')
json.dump(d, archivo)
archivo.close()

