
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json


# In[2]:


with open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Barrios_bus.geojson') as json_data:
    d = json.load(json_data)
    json_data.close()


# In[8]:


paradas=[]
for i in range(0,len(d['features'])):
    paradas.append(d['features'][i]['properties']['paradas_bus'])


# In[15]:


intervalos=list(range(0,max(paradas),9))


# In[17]:


for i in range(0,len(d['features'])):
    if intervalos[0]<=d['features'][i]['properties']['paradas_bus']<intervalos[1]:
        d['features'][i]['properties']['raster']=20
    elif intervalos[1]<=d['features'][i]['properties']['paradas_bus']<intervalos[2]:
        d['features'][i]['properties']['raster']=40
    elif intervalos[2]<=d['features'][i]['properties']['paradas_bus']<intervalos[3]:
        d['features'][i]['properties']['raster']=60
    elif intervalos[3]<=d['features'][i]['properties']['paradas_bus']<intervalos[4]:
        d['features'][i]['properties']['raster']=80
    elif intervalos[4]<d['features'][i]['properties']['paradas_bus']:
        d['features'][i]['properties']['raster']=100        


# In[23]:


archivo = open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\raster_barrios_bus.geojson','w')
json.dump(d, archivo)
archivo.close()

