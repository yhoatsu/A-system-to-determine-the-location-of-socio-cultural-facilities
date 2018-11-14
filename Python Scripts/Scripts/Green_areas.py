
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json


# In[2]:


with open(r'D:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\barrio_parques.geojson') as json_data:
    d = json.load(json_data)
    json_data.close()


# In[4]:


parques=[]
for i in range(0,len(d['features'])):
    parques.append(d['features'][i]['properties']['barrios_parques'])


# In[6]:


intervalos=list(range(0,max(parques),round(max(parques)/5)))


# In[7]:


intervalos


# In[14]:


for i in range(0,len(d['features'])):
    if intervalos[0]<=d['features'][i]['properties']['barrios_parques']<intervalos[1]:
        d['features'][i]['properties']['raster']=20
    elif intervalos[1]<=d['features'][i]['properties']['barrios_parques']<intervalos[2]:
        d['features'][i]['properties']['raster']=40
    elif intervalos[2]<=d['features'][i]['properties']['barrios_parques']<intervalos[3]:
        d['features'][i]['properties']['raster']=60
    elif intervalos[3]<=d['features'][i]['properties']['barrios_parques']<intervalos[4]:
        d['features'][i]['properties']['raster']=80
    elif intervalos[4]<d['features'][i]['properties']['barrios_parques']:
        d['features'][i]['properties']['raster']=100  


# In[16]:


archivo = open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\raster_barrios_parques.geojson','w')
json.dump(d, archivo)
archivo.close()

