import pandas as pd
import random as rd
import numpy as np
import matplotlib.pyplot as plt

class agente:
    def __init__(self, estados, scores, politicas, vecinos):
        self.estado = estados # lista
        self.score = scores # lista
        self.politica = politicas # lista
        self.vecinos = vecinos

def crear_agentes_aleatorios(Num_agentes):
    Agentes = []
    for i in range(Num_agentes):
        Agentes.append(agente([rd.randint(0,1)], [], [rd.randint(0,7)], []))

    X = calcula_medio(Agentes)
    for a in Agentes:
        if a.estado[-1] == 1:
            if X > 0.5:
                a.score.append(-1)
            else:
                a.score.append(1)
        else:
            a.score.append(0)

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

def leer_red(Agentes):
    net = {}

    In = open("Networks/connlist.dat", "r")
    for line in In:
        v = list(map(int, line.split()))
        if v[0] not in net.keys():
            net[v[0]] = [v[1]]
        else:
            net[v[0]].append(v[1])

    In.close()
    print(net)
    for i in range(len(Agentes)):
        try:
            Agentes[i].vecinos = net[i]
        except:
            Agentes[i].vecinos = []


def calcula_medio(agentes):
    a = [x.estado[-1] for x in agentes]
    return np.sum(a)/len(a)

def juega_ronda(Agentes, politicas):
    for a in Agentes:
        polit = politicas[a.politica[-1]]
        a.estado.append(polit[(a.estado[-1], a.score[-1])])

    X = calcula_medio(Agentes)
    # print('Medio', X)
    for a in Agentes:
        if a.estado[-1] == 1:
            if X > 0.5:
                a.score.append(-1)
            else:
                a.score.append(1)
        else:
            a.score.append(0)

    return Agentes

def agentes_aprenden(Agentes):
    #Los agentes copian la politica del ganador de la Ronda
    for agente in Agentes:
        maximo=agente.score[-1]
        maximo_vecino=Agentes.index(agente)
        # print('Vencinos', agente.vecinos)
        for index_vecino in agente.vecinos:
            if((Agentes[index_vecino].score[-1])>(maximo)):
                maximo=Agentes[index_vecino].score[-1]
                maximo_vecino=index_vecino
        # print('Agente',Agentes.index(agente),'aprende de',maximo_vecino)
        # print('Politica nueva',Agentes[maximo_vecino].politica[-1])
        agente.politica.append(Agentes[maximo_vecino].politica[-1])
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
            politica.append(Agentes[i].politica[r])

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
# ANALISIS_politicaS
#
# ANALISIS_ASISTENCIA
#
# ANALISIS_AGENTES
