
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json


# In[2]:


with open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\barrio_area.geojson') as json_data:
    d = json.load(json_data)
    json_data.close()


# In[3]:


tabla=pd.read_csv(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Tablas\Padrón\poblacion_grupos.csv',sep=';',dtype={'Product':str},engine="python", encoding="latin_1")


# In[4]:


aux=[]
for i in range(0,len(tabla.ix[:,0].str.split(" "))):
    cod=tabla.ix[:,0].str.split(" ")[i][0].replace('.','')
    if len(cod)==2:
        aux.append('0'+cod)
    else:
        aux.append(cod)


# In[5]:


tabla.insert(0,'coddistbar',aux)


# In[10]:


for k in range(0,len(d['features'])):
    cod=d['features'][k]['properties']['coddistbar']
    d['features'][k]['properties']['hacinamiento']=float(tabla[tabla['coddistbar']==cod]['Total']/d['features'][k]['properties']['area'])


# In[15]:


hacinamiento=[]
for k in range(0,len(d['features'])):
    hacinamiento.append(d['features'][k]['properties']['hacinamiento'])


# In[28]:


intervalos=list(np.linspace(0,max(hacinamiento)-0.001,5))


# In[29]:


intervalos


# In[30]:


for i in range(0,len(d['features'])):
    if intervalos[0]<=d['features'][i]['properties']['hacinamiento']<intervalos[1]:
        d['features'][i]['properties']['raster']=100
    elif intervalos[1]<=d['features'][i]['properties']['hacinamiento']<intervalos[2]:
        d['features'][i]['properties']['raster']=80
    elif intervalos[2]<=d['features'][i]['properties']['hacinamiento']<intervalos[3]:
        d['features'][i]['properties']['raster']=60
    elif intervalos[3]<=d['features'][i]['properties']['hacinamiento']<intervalos[4]:
        d['features'][i]['properties']['raster']=40
    elif intervalos[4]<d['features'][i]['properties']['hacinamiento']:
        d['features'][i]['properties']['raster']=20  


# In[35]:


archivo = open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\hacinamiento.geojson','w')
json.dump(d, archivo)
archivo.close()

