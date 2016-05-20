# -*- coding: utf-8 -*-
"""
Created on Thu May 05 16:41:25 2016

@author: Alex
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from __future__ import division 

df = pd.read_csv('diabetic_data.csv')

EvFavo=df.encounter_id[(df.race == 'Caucasian')&(df.admission_source_id==8)].count()
EvPos=df.encounter_id[df.admission_source_id==8].count()
Probabilidad = str((EvFavo/EvPos)*100) + '%'
print(Probabilidad)

tabla = pd.crosstab(df.race, df.admission_source_id)
#Probabilidad por columna
probabilida = tabla/tabla.sum()
#Probabilidad general
probabilidaGeneral = tabla/tabla.sum().sum()

#Grafico 
plt.hist(probabilida[8])
plt.plot(probabilida[8])












"""
Que probabilidad tienen los pacientes, que presentan inestabilidad en niveles
de insulina que sean readmitidos después de 30 días.
"""
#Tabla
tabla = pd.crosstab(df.insulin, df.readmitted)
#Probabilidad por columna
probabilida = tabla/tabla.sum()
#Probabilidad general
probabilidaGeneral = tabla/tabla.sum().sum()

#Grafica
graf = pd.crosstab(index = df['insulin'], columns = df['readmitted']).plot(kind='bar')

#Funcion
def FuncIns(NivelInsulina,Time):
    EvFavo=df.encounter_id[(df.insulin == NivelInsulina)&(df.readmitted==Time)].count()
    EvPos=df.encounter_id[df.readmitted==Time].count()
    Probabilidad = EvFavo/EvPos
    print(Probabilidad)
    
#GroupBy
TablaGroup= df.groupby(['insulin','readmitted']).encounter_id.count()
TotalReadmitted = df.readmitted.groupby(df.readmitted).count()
Probabilidad = TablaGroup/TotalReadmitted






"""
que raza es mas probable a ser transferido de un lugasr x al del hospital
"""
tabla2 = pd.crosstab(df.race, df.admission_source_id)
#Probabilidad por columna
probabilidad = tabla2/tabla2.sum()
#Probabilidad general
#probabilidaGeneral = tabla2/tabla2.sum().sum()

#Grafica
graf = pd.crosstab(index = df['race'], columns = df['admission_source_id']).plot(kind='bar')


#Funcion
def FunProbabilidad( Race,Admision ): 
    EvFavo=df.encounter_id[(df.race == Race)&(df.admission_source_id==Admision)].count()
    EvPos=df.encounter_id[df.admission_source_id==Admision].count()
    Probabilida = str((EvFavo/EvPos)*100) + '%'
    print(Probabilida)
    
def LlamarProbabilidad(Admision):
    print probabilidad[Admision]

#GroupBy
TablaGroupAdmission= df.groupby(['race','admission_source_id']).encounter_id.count()
CountAdmi = df.admission_source_id.groupby(df.admission_source_id).count()
Probabilidad = TablaGroupAdmission/CountAdmi






"""
Cual es la probabilidad dependiendo del nivel   diabetes a que tenga n
cantidad de consultas
"""

tabla3 = pd.crosstab(df.number_outpatient, df.number_diagnoses)
#Probabilidad por columna
probabilidad = tabla3/tabla3.sum()
#Probabilidad general
#probabilidaGeneral = tabla2/tabla2.sum().sum()

#Grafica
graf = pd.crosstab(index = df['number_outpatient'], columns = df['number_diagnoses']).plot(kind='bar')
graficars = pd.crosstab(index=df['number_outpatient'],columns=df['number_diagnoses']).apply(lambda r: r/r.sum() *100, axis=1).plot(kind='bar')

#Funcion
def FunProba( NivelDiabete,CantiConsul ):
    EvFavo=df.encounter_id[(df.number_outpatient == NivelDiabete)&(df.number_diagnoses==CantiConsul)].count()
    EvPos=df.encounter_id[df.number_diagnoses==CantiConsul].count()
    Probabilida = str((EvFavo/EvPos)*100) + '%'
    print(Probabilida)
    
def LlamarProbabAdmi(Admision):
    a = probabilidad[Admision]
    return a

#GroupBy
TablaGroupAdmission= df.groupby(['number_diagnoses','number_outpatient']).encounter_id.count()
CountAdmi = df.admission_source_id.groupby(df.number_diagnoses).count()
Probabilidad = TablaGroupAdmission/CountAdmi









"""
Que edad, que raza y que genero es mas propensa a tener el cirto nivel de diabetes 
"""
#Tabla por edad 
TabGroupByAge = pd.crosstab(df.age, df.number_diagnoses)
Colum = TabGroupByAge[2]
print Colum.index[Colum==Colum.max()]

#Grafica
graf = pd.crosstab(index = df['age'], columns = df['number_diagnoses']).plot(kind='bar')


TabGroupByRace = pd.crosstab(df.race, df.number_diagnoses)
Colum1 = TabGroupByRace[2]
print Colum1.index[Colum1==Colum1.max()]

#grafica
graf = pd.crosstab(index = df['race'], columns = df['number_diagnoses']).plot(kind='bar')


TabGroupByGender = pd.crosstab(df.gender, df.number_diagnoses)
Colum2 = TabGroupByGender[2]
print Colum2.index[Colum2==Colum2.max()]

#grafica
graf = pd.crosstab(index = df['gender'], columns = df['number_diagnoses']).plot(kind='bar')


def Fun(tipo,a):
    if (tipo=='raza'):
        Colum1 = TabGroupByRace[a]
        print Colum1.index[Colum1==Colum1.max()]
    if (tipo=='genero'):
        Colum2 = TabGroupByGender[2]
        print Colum2.index[Colum2==Colum2.max()]
        
    if (tipo=='age'):
        Colum = TabGroupByAge[2]
        print Colum.index[Colum==Colum.max()]
