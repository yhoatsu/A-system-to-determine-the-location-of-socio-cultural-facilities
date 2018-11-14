
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json


# In[48]:


with open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Barrios.geojson') as json_data:
    d = json.load(json_data)
    json_data.close()


# In[31]:


tabla=pd.read_csv(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\Tablas\Padrón\poblacion_nivel_estudios.csv',sep=';',dtype={'Product':str},engine="python", encoding="latin_1")


# In[32]:


aux=[]
for i in range(0,len(tabla.ix[:,0].str.split(" "))):
    cod=tabla.ix[:,0].str.split(" ")[i][0].replace('.','')
    if len(cod)==2:
        aux.append('0'+cod)
    else:
        aux.append(cod)


# In[33]:


tabla.insert(0,'coddistbar',aux)


# In[35]:


p_no_lee_esc=[]
for i in range(0,len(tabla)):
    p_no_lee_esc.append((tabla.ix[i]['No sabe leer ni escribir']/tabla.ix[i]['Total']))


# In[36]:


tabla.insert(2,'p_no_lee_esc',p_no_lee_esc)


# In[37]:


p_inf_grad=[]
for i in range(0,len(tabla)):
    p_inf_grad.append((tabla.ix[i]['Titulación inferior a graduado escolar']/tabla.ix[i]['Total']))


# In[38]:


tabla.insert(3,'p_inf_grad',p_inf_grad)


# In[39]:


p_grad=[]
for i in range(0,len(tabla)):
    p_grad.append((tabla.ix[i]['Graduado escolar o equivalente']/tabla.ix[i]['Total']))


# In[40]:


tabla.insert(4,'p_grad',p_grad)


# In[41]:


p_bach=[]
for i in range(0,len(tabla)):
    p_bach.append((tabla.ix[i]['Bachiller, Formación Profesional de Segundo Grado o Títulos equivalentes o superiores']/tabla.ix[i]['Total']))


# In[42]:


tabla.insert(5,'p_bach',p_bach)


# In[49]:


for k in range(0,len(d['features'])):
    cod=d['features'][k]['properties']['coddistbar']
    d['features'][k]['properties']['raster']=int(tabla[tabla['coddistbar']==cod]['p_no_lee_esc']*25
                                                 + int(tabla[tabla['coddistbar']==cod]['p_inf_grad']*50)
                                                 + int(tabla[tabla['coddistbar']==cod]['p_grad']*75)
                                                 + int(tabla[tabla['coddistbar']==cod]['p_bach']*100))


# In[55]:


archivo = open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto en QGIS\raster_barrios_estudios.geojson','w')
json.dump(d, archivo)
archivo.close()

