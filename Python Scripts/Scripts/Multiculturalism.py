
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json


# In[2]:


with open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Barrios.geojson') as json_data:
    d = json.load(json_data)
    json_data.close()


# In[19]:


tabla=pd.read_csv(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Tablas\Padrón\poblacion_estranjera.csv',sep=';',dtype={'Indice':float},engine="python", encoding="latin_1")


# In[20]:


aux=[]
for i in range(0,len(tabla.ix[:,0].str.split(" "))):
    cod=tabla.ix[:,0].str.split(" ")[i][0].replace('.','')
    if len(cod)==2:
        aux.append('0'+cod)
    else:
        aux.append(cod)


# In[21]:


tabla.insert(0,'coddistbar',aux)


# In[22]:


indice=list(tabla['Indice'])


# In[24]:


intervalos=np.linspace(0,max(indice)-0.001,6)


# In[25]:


intervalos


# In[26]:


for i in range(0,len(d['features'])):
    cod=d['features'][i]['properties']['coddistbar']
    num_votos=float(tabla[tabla['coddistbar']==cod]['Indice'])
    if intervalos[0]<=num_votos<intervalos[1]:
        d['features'][i]['properties']['raster']=0
    elif intervalos[1]<=num_votos<intervalos[2]:
        d['features'][i]['properties']['raster']=20
    elif intervalos[2]<=num_votos<intervalos[3]:
        d['features'][i]['properties']['raster']=40
    elif intervalos[3]<=num_votos<intervalos[4]:
        d['features'][i]['properties']['raster']=60
    elif intervalos[4]<=num_votos<intervalos[5]:
        d['features'][i]['properties']['raster']=80
    elif intervalos[5]<=num_votos:
        d['features'][i]['properties']['raster']=100


# In[29]:


archivo = open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\diversidad.geojson','w')
json.dump(d, archivo)
archivo.close()

