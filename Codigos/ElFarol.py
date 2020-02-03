import pandas as pd
import random as rd
import numpy as np
import matplotlib.pyplot as plt
import redes

class agente:
    def __init__(self, estados, scores, politicas, vecinos):
        self.estado = estados # lista
        self.score = scores # lista
        self.politica = politicas # lista
        self.vecinos = vecinos

    def __str__(self):
        return "E:{0}, S:{1}, P:{2}, V{3}".format(self.estado, self.score,self.politica,self.vecinos)

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

def leer_red(Agentes):

    net = {}

    In = open("connlist.dat", "r")
    for line in In:
        v = list(map(int, line.split()))

        if v[0] not in net.keys():
            net[v[0]] = [v[1]]
        else:
            net[v[0]].append(v[1])

        if v[1] not in net.keys():
            net[v[1]] = [v[0]]
        else:
            net[v[1]].append(v[0])

    In.close()
    # print('Red', net)
    for i in range(len(Agentes)):
        try:
            Agentes[i].vecinos = net[i]

        except:
            Agentes[i].vecinos = []


def calcula_medio(agentes):
    a = [x.estado[-1] for x in agentes]
    return np.sum(a)/len(a)

def juega_ronda(Agentes, politicas, UMBRAL):
    for a in Agentes:
        polit = politicas[a.politica[-1]]
        a.estado.append(polit[(a.estado[-1], a.score[-1])])

    X = calcula_medio(Agentes)
    # print('Medio', X)
    for a in Agentes:
        if a.estado[-1] == 1:
            if X > UMBRAL:
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

def crea_dataframe_agentes(Agentes, Num_iteraciones, PARAMETROS, N):

    muestra = []
    agente = []
    ronda = []
    estado = []
    puntaje = []
    politica = []
    lista_num_iteraciones = []
    lista_parametros = []
    for p in PARAMETROS:
        lista_parametros.append([])
    for i in range(len(Agentes)):
        for r in range(Num_iteraciones):
            muestra.append(N)
            agente.append(i)
            ronda.append(r)
            estado.append(Agentes[i].estado[r])
            puntaje.append(Agentes[i].score[r])
            politica.append(Agentes[i].politica[r])
            lista_num_iteraciones.append(Num_iteraciones)
            for x in range(len(PARAMETROS)):
                lista_parametros[x].append(PARAMETROS[x])


    data = pd.DataFrame.from_dict(\
    {\
    'Identificador': muestra,\
    'Agente': agente,\
    'Ronda': ronda,\
    'Estado': estado,\
    'Puntaje': puntaje,\
    'Politica': politica\
    })

    for p in range(len(PARAMETROS)):
        nombre = 'Parametro-' + str(p)
        data[nombre] = lista_parametros[p]

    return data

def guardar(dataFrame, archivo, inicial):
    # dataFrame.to_csv(archivo, index=False)

    with open(archivo, 'a') as f:
        dataFrame.to_csv(f, header=inicial, index=False)

    f.close()

def cargar(archivo):
    data = pd.read_csv(archivo)

def simulacion(Num_agentes, Num_iteraciones, UMBRAL, TIPO_RED, PARS, inicial, N):

    agentes = crear_agentes_aleatorios(Num_agentes)
    # print('***********************************************')
    # print('* PREPARACION *')
    # print('***********************************************')
    # print('Ronda: 0',end=" ")
    # print('Estados:', [x.estado[-1] for x in agentes],end=" ")
    # print('Score:', [x.score[-1] for x in agentes],end=" ")
    # print('Politicas:', [x.politica[-1] for x in agentes])
    # print(agentes)

    politicas = crear_politicas()

    # Generando red a archivo
    if TIPO_RED == 0:
        # print('---------')
        # print('Parametros red:', PARS)
        # print('---------')
        redes.random_graph(*PARS)

    # Leyendo red de archivo
    leer_red(agentes)

    # print('***********************************************')
    # print('* ITERACIONES *')
    # print('***********************************************')
    for i in range(Num_iteraciones):
        agentes = juega_ronda(agentes, politicas, UMBRAL)
        # print('\nRonda:', str(i+1),end=" ")
        # print('Estados:', [x.estado[-1] for x in agentes],end=" ")
        # print('Score:', [x.score[-1] for x in agentes],end=" ")
        agentes = agentes_aprenden(agentes)
        # print('Politica:', [x.politica[-1] for x in agentes])

    data = crea_dataframe_agentes(agentes, Num_iteraciones, PARS, N)

    # print(data[:10])

    guardar(data, 'agentes.csv', inicial)
