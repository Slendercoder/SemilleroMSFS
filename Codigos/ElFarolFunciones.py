import numpy as np
import pandas as pd

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

def encontrar_consistencia(politica, politica_lag):
    #print(politica_lag, type(politica_lag))
    if np.isnan(politica_lag):
        return np.nan
    elif politica == politica_lag:
        return 1
    else: return 0
