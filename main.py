import pandas as pd
import random as rd
import numpy as np
import matplotlib.pyplot as plt
import ElFarol as EF

Num_agentes = 2
Num_iteraciones = 10
TIPO_RED = 0 # COMPLETA

agentes = crear_agentes_aleatorios(Num_agentes)

politicas = crear_politicas()

# CARLOS
red = crear_red(agentes)

# YA
agentes = juega_ronda(agentes)

# ESTEBAN
agentes = agentes_aprenden(agentes, red)

# # MARIA JOSE
# SIMULACION(Num_Iteraciones)
#     RONDA
#     APRENDIZAJE

data = crea_dataframe_agentes(agentes, Num_iteraciones)

guardar(data, 'agentes.csv')

# # EDGAR
# HISTOGRAMA_USO, GRAFICA_USO_VS_TIEMPO, GRAFICA_PUNTAJE = ANALISIS_ESTRATEGIAS(AGENTES)
#
# # ROJAS
# GRAFICA_ASISTENTES_BAR_VS_RONDA = ANALISIS_ASISTENCIA(AGENTES)
#
# # MIGUEL
# GRAFICA_PUNTAJE_VS_RONDA, GRAFICA_ESTRATEGIA_VS_RONDA = ANALISIS_AGENTES(AGENTES)
