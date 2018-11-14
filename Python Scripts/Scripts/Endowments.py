
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json


# In[2]:


with open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\barrios_equipamientos.geojson') as json_data:
    d = json.load(json_data)
    json_data.close()


# In[5]:


equipamientos=[]
for i in range(0,len(d['features'])):
    equipamientos.append(d['features'][i]['properties']['equipamientos'])


# In[8]:


intervalos=list(range(0,max(equipamientos),round(max(equipamientos)/5)))


# In[9]:


intervalos


# In[11]:


for i in range(0,len(d['features'])):
    if intervalos[0]<=d['features'][i]['properties']['equipamientos']<intervalos[1]:
        d['features'][i]['properties']['raster']=20
    elif intervalos[1]<=d['features'][i]['properties']['equipamientos']<intervalos[2]:
        d['features'][i]['properties']['raster']=40
    elif intervalos[2]<=d['features'][i]['properties']['equipamientos']<intervalos[3]:
        d['features'][i]['properties']['raster']=60
    elif intervalos[3]<=d['features'][i]['properties']['equipamientos']<intervalos[4]:
        d['features'][i]['properties']['raster']=80
    elif intervalos[4]<d['features'][i]['properties']['equipamientos']:
        d['features'][i]['properties']['raster']=100  


# In[13]:


archivo = open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\raster_barrios_equipamientos.geojson','w')
json.dump(d, archivo)
archivo.close()

