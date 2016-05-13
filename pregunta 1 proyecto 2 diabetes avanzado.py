# -*- coding: utf-8 -*-
"""
Created on Thu May 05 10:47:59 2016

@author: Gustavo
"""
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as pl
import seaborn as sns

from __future__ import division 

df = pd.read_csv('diabetic_data.csv')
df= pd.read_csv(r"C:\Users\Gustavo\diabetic_data.csv")
#PREGUNTA 1:
#¿Cual es el rango de edad n que presenta la mayor probabilidad de ser ingresado al hospital por k razon

print df
df.head()

df.info
df.readmitted.describe()
df.mode()
df.age.describe()

#groupby
df.groupby(['age','admission_type_id']).count()

#TABLA1

tabla1 = pd.crosstab(df.age, df.admission_type_id)
print tabla1

probabilidad = tabla1/tabla1.sum()
probabilidadGeneral = tabla1/tabla1.sum().sum()
print probabilidadGeneral
print probabilidad

#TABLA ALL
tablacont1 = pd.crosstab(index=df['age'],
            columns=df['admission_type_id'], margins=True)
print tablacont1

#FUNCION
def ageadmintype(age,admission_type_id):
   EvFavo=df.encounter_id[(df.age == age)&(df.admission_type_id==admission_type_id)].count()
   EvPos=df.encounter_id[df.admission_type_id==admission_type_id].count()
   Probabilidad = str((EvFavo/EvPos)*100) + '%'
   print(Probabilidad)
   
#####FUNCION que responde la edad que presenta la mayor probabilidad ingresando tipo de admin type   
def Fun(admision):
    Colum = probabilidad[admision]
    print Colum.index[Colum==Colum.max()]

#GRAFICA
graficareales = pd.crosstab(index=df['age'],
            columns=df['admission_type_id']).plot(kind='bar')

 
#PREGUNTA 2
 #CUAL ES L A PROBABILIDAD DE UNA PERSONA INGRESADA POR RAZON X TENGA N CANTIDAD DE PROCEDIMIENTOS QUIRUIRRGICOS
 
#groupby
df.groupby(['admission_type_id', 'num_procedures']).encounter_id.count()

#TABLA1
 

tabla2 = pd.crosstab(df.admission_type_id, df.num_procedures)
print tabla2
 
#TABLA ALL
tablacont2 = pd.crosstab(index=df['admission_type_id'],
            columns=df['num_procedures'], margins=True)
print tablacont2

#probabilidad general entre todos los datos
probabilidad2 = tabla2/tabla2.sum()
probabilidadGeneral2 = tabla2/tabla2.sum().sum()
print probabilidadGeneral2
print probabilidad2

 
#FUNCION
 

 
def adminproced(admission_type_id, num_procedures):
   EvFavo=df.encounter_id[(df.admission_type_id == admission_type_id)&(df.num_procedures==num_procedures)].count()
   EvPos=df.encounter_id[df.num_procedures==num_procedures].count()
   Probabilidad = str((EvFavo/EvPos)*100) + '%'
   print(Probabilidad)
   

 
#GRAFICA
graficareales = pd.crosstab(index=df['admission_type_id'],
            columns=df['num_procedures']).plot(kind='bar')

#pregunta 3  
#Que probabilidad tiene la raza raza n y a recibir TIPOS DE PROCEDIMIENTOS DE LABORATORI?

df.num_lab_procedures.unique()

#TABLA
tabla3 = pd.crosstab(df.race, df.num_lab_procedures)
print tabla3

probabilidad3 = tabla3/tabla3.sum()
probabilidaGeneral3 = tabla3/tabla3.sum().sum()
print probabilidad3
print probabilidadGeneral3

#FUNCION RESPONDA PROBABILIDAD raza raza n y a recibir k cantidad de procedimientos?
def raceproce(race, num_lab_procedures):
   EvFavo=df.encounter_id[(df.race == race)&(df.num_lab_procedures==num_lab_procedures)].count()
   EvPos=df.encounter_id[df.num_lab_procedures==num_lab_procedures].count()
   Probabilidad = str((EvFavo/EvPos)*100) + '%'
   print(Probabilidad)

#GROUPBY
df.groupby(['race', 'num_lab_procedures']).encounter_id.count()

#TABLA ALL
tablacont3 = pd.crosstab(index=df['race'],
            columns=df['num_lab_procedures'], margins=True)
print tablacont3

#GRAFICA3 
#cambie mis ejes para que la grafica se entendiera un poco mas
graficareales = pd.crosstab(index=df['num_lab_procedures'],
            columns=df['race']).plot(kind='bar')
            




 