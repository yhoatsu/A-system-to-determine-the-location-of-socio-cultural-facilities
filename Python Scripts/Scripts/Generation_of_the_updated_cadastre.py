
# coding: utf-8

# In[1]:


import json
import numpy


# In[15]:


with open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto Spatial\Pruebas\parcelas_actuales.json') as json_data:
    a = json.load(json_data)
    json_data.close()


# In[2]:


with open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto Spatial\Pruebas\geo.geojson') as json_data:
    d = json.load(json_data)
    json_data.close()


# In[3]:


with open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto Spatial\Pruebas\parcelas_non_sense.json') as json_data:
    c = json.load(json_data)
    json_data.close()


# In[4]:


with open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto Spatial\Pruebas\reetiquetado.json') as json_data:
    b = json.load(json_data)
    json_data.close()


# In[5]:


parcelas_dicc={}
for items in a:
    parcelas_dicc.update(items)


# In[6]:


etiquetado_dicc={}
for items in b:
    etiquetado_dicc.update(items)


# In[7]:


non_sense_dicc={}
for items in c:
    non_sense_dicc.update(items)


# In[10]:


parcelas_dicc.update(non_sense_dicc)


# In[11]:


dicc_reemplazado={}
for k,v in parcelas_dicc.items():
    dicc_aux={}
    for i,j in v.items():
        dicc_aux[etiquetado_dicc[i]]=j
    dicc_reemplazado[k]=dicc_aux


# In[12]:


categorias2=[]
for k,v in dicc_reemplazado.items():
    for i,j in v.items():
        categorias2.append(i)


# In[16]:


cat2=list(numpy.unique(categorias2))


# In[17]:


parcelas_categoria2={}
for elem in cat2:
    parcelas_categoria2[elem]=[]


# In[18]:


for k,v in dicc_reemplazado.items():
    for i,j in v.items():
        parcelas_categoria2[i].append(k)


# In[19]:


dicc_maximo={}
for k,v in dicc_reemplazado.items():
    dicc_aux={}
    for i,j in v.items():
        dicc_aux[i]=max(j)
    dicc_maximo[k]=dicc_aux


# In[44]:


for k in range(0,len(d['features'])):
    parcela=d['features'][k]['properties']['refparcela']
    if parcela in dicc_maximo.keys():
        d['features'][k]['properties'].update(dicc_maximo[parcela])
        del d['features'][k]['properties']['refpar']
        del d['features'][k]['properties']['refpla']
        del d['features'][k]['properties']['codvia']
        del d['features'][k]['properties']['dupli']
        del d['features'][k]['properties']['construcci']
        del d['features'][k]['properties']['antiguedad']
        del d['features'][k]['properties']['reforma']
        del d['features'][k]['properties']['tipo_refor']
        del d['features'][k]['properties']['ficha_es']
        del d['features'][k]['properties']['ficha_va']
        del d['features'][k]['properties']['pob_0_14']
        del d['features'][k]['properties']['pob_15_65']
        del d['features'][k]['properties']['pob_66_mas']
        del d['features'][k]['properties']['pob_total']
        d['features'][k]['properties']['url']=d['features'][k]['properties']['url'][35:-31]


# In[ ]:


del d['features'][k]['properties']['refpar']
del d['features'][k]['properties']['refpla']
del d['features'][k]['properties']['codvia']
del d['features'][k]['properties']['dupli']
del d['features'][k]['properties']['construcci']
del d['features'][k]['properties']['antiguedad']
del d['features'][k]['properties']['reforma']
del d['features'][k]['properties']['tipo_refor']
del d['features'][k]['properties']['ficha_es']
del d['features'][k]['properties']['ficha_va']
del d['features'][k]['properties']['pob_0_14']
del d['features'][k]['properties']['pob_15_65']
del d['features'][k]['properties']['pob_66_mas']
del d['features'][k]['properties']['pob_total']
d['features'][k]['properties']['url']=d['features'][k]['properties']['url'][35:-31]


# In[46]:


archivo = open(r'G:\GoogleDrive\Hacker Civics\Proyecto Spatial\Proyecto Spatial\Pruebas\cadastre.geojson','w')
json.dump(d, archivo)
archivo.close()

