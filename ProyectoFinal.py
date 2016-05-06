# -*- coding: utf-8 -*-
"""
Created on Thu May 05 16:38:22 2016

@author: Lesly Garcia
"""

import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
from __future__ import division

df = pd.read_csv('diabetic_data.csv')

# ¿Cuál es la probabilidad de que una persona mayor o igual al rango de edad 
# 60-70 años pase más de 8 días en el hospital?

DataMay60 = df[(df.age == '[60-70)')|(df.age == '[70-80)')|(df.age == '[80-90)')]

#Eventos Favorables
DataDiasMayor8 = DataMay60.encounter_id[DataMay60.time_in_hospital >= 8].count()

#Eventos Posibles personas mayores a 60 años pero han estado n cantidad de días 
EvPosibles = DataMay60.encounter_id.count()

Probabilidad = str((DataDiasMayor8/EvPosibles)*100) + '%'




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

