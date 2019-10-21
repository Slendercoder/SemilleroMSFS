import pandas as pd
import random as rd
import numpy as np
import matplotlib.pyplot as plt

class agente:
    def __init__(self, estados, scores, estrategias, vecinos):
        self.estado = estados # lista
        self.score = scores # lista
        self.estrategia = estrategias # lista
        self.vecinos = vecinos

def crear_agentes_aleatorios(Num_agentes):
    Agentes = []
    for i in range(Num_agentes):
        Agentes.append(agente([rd.randint(0,1)], [0], [rd.randint(0,7)], []))

    return Agentes

def crear_politicas():
    politicas = [
    {(0,0): 0, (1,1): 0, (1, -1): 0},
    {(0,0): 0, (1,1): 0, (1, -1): 1},
    {(0,0): 0, (1,1): 1, (1, -1): 0},
    {(0,0): 0, (1,1): 1, (1, -1): 1},
    {(0,0): 1, (1,1): 0, (1, -1): 0},
    {(0,0): 1, (1,1): 0, (1, -1): 1},
    {(0,0): 1, (1,1): 1, (1, -1): 0},
    {(0,0): 1, (1,1): 1, (1, -1): 1},
    ]
    return politicas

def crear_red(Agentes):
    for i in range(len(Agentes)):
        Agentes[i].vecinos = [x for x in range(len(Agentes)) if x!=i]

    return Agentes

def calcula_medio(agentes):
    a = [x.estado for x in agentes]
    return np.sum(a)/len(a)

def juega_ronda(Agentes, politicas):
    X = calcula_medio(Agentes)
    for a in Agentes:
        if a.estado[-1] == 1:
            if X > 0.5:
                a.score.append(-1)
            else:
                a.score.append(1)
        else:
            a.score.append(0)

        polit = politicas[a.estrategia[-1]]
        a.estado.append(polit[(a.estado[-1], a.score[-1])])
        a.estrategia.append(a.estrategia[-1])

    return Agentes

def agentes_aprenden(Agentes, Red):
    return Agentes

def crea_dataframe_agentes(Agentes, Num_iteraciones):
    print(Agentes)
    agente = []
    ronda = []
    estado = []
    puntaje = []
    politica = []
    for i in range(len(Agentes)):
        for r in range(Num_iteraciones):
            agente.append(i)
            ronda.append(r)
            estado.append(Agentes[i].estado[r])
            puntaje.append(Agentes[i].score[r])
            politica.append(Agentes[i].estrategia[r])

    data = pd.DataFrame.from_dict(\
    {\
    'Agente': agente,\
    'Ronda': ronda,\
    'Estado': estado,\
    'Puntaje': puntaje,\
    'Politica': politica\
    })

def guardar(dataFrame, archivo):
    dataFrame.pd.to_csv(archivo, index=False)

def cargar(archivo):
    data = pd.read_csv(archivo)

# SIMULACION
#
# ANALISIS_ESTRATEGIAS
#
# ANALISIS_ASISTENCIA
#
# ANALISIS_AGENTES
