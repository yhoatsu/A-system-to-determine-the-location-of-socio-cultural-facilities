
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json


# In[2]:


with open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Barrios.geojson') as json_data:
    d = json.load(json_data)
    json_data.close()


# In[6]:


tabla=pd.read_csv(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Tablas\Decidim\num_propuestas.csv',sep=';',dtype={'Product':str},engine="python", encoding="latin_1",header=None)


# In[15]:


propuestas=[]
for i in range(0,len(tabla.ix[:,0])):
    propuestas.append(tabla.ix[i][2])


# In[19]:


intervalos=list(range(0,max(propuestas),int(round(max(propuestas)/5))))


# In[20]:


intervalos


# In[37]:


for i in range(0,len(d['features'])):
    cod=int(d['features'][i]['properties']['coddistbar'])
    num_propuestas=int(tabla[tabla[0]==cod][2])
    if intervalos[0]<=num_propuestas<intervalos[1]:
        d['features'][i]['properties']['raster']=20
    elif intervalos[1]<=num_propuestas<intervalos[2]:
        d['features'][i]['properties']['raster']=40
    elif intervalos[2]<=num_propuestas<intervalos[3]:
        d['features'][i]['properties']['raster']=60
    elif intervalos[3]<=num_propuestas<intervalos[4]:
        d['features'][i]['properties']['raster']=80
    elif intervalos[4]<num_propuestas:
        d['features'][i]['properties']['raster']=100    


# In[40]:


archivo = open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\propuestas_decidim.geojson','w')
json.dump(d, archivo)
archivo.close()

