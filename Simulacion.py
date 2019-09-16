import pandas as pd
import random as rd
import numpy as np
import matplotlib.pyplot as plt

################################
# VARIABLES GLOBALES
################################

estrategias = [
{(0,0): 0, (1,1): 0, (1, -1): 0},
{(0,0): 0, (1,1): 0, (1, -1): 1},
{(0,0): 0, (1,1): 1, (1, -1): 0},
{(0,0): 0, (1,1): 1, (1, -1): 1},
{(0,0): 1, (1,1): 0, (1, -1): 0},
{(0,0): 1, (1,1): 0, (1, -1): 1},
{(0,0): 1, (1,1): 1, (1, -1): 0},
{(0,0): 1, (1,1): 1, (1, -1): 1},
]

class agente:
    def __init__(self, Estado, score, acumulado, estrategia):
        self.estado = Estado
        self.score = score
        self.acumulado = acumulado
        self.estrategia = estrategia

def calcula_medio(agentes):
    a = [x.estado for x in agentes]
    return np.sum(a)/len(a)

def juegoCoqueto(agentes):
    X = calcula_medio(agentes)
    for a in agentes:
        if a.estado == 1:
            if X > 0.5:
                a.score = -1
            else:
                a.score = 1
        else:
            a.score = 0

        a.acumulado += a.score

def todasCombinaciones(Num_Iteraciones):
    Ganacias = [0]*8
    for i in estrategias:
        for j in estrategias:
            for k in estrategias:
                combinaciones = [(r, s, t) for r in range(2) for s in range(2) for t in range(2)]
                for p in combinaciones:
                    Agentes = []
                    # print('k', k)
                    a = agente(p[0], 0, 0, i)
                    Agentes.append(a)
                    a = agente(p[1], 0, 0, j)
                    Agentes.append(a)
                    a = agente(p[2], 0, 0, k)
                    Agentes.append(a)

                    for T in range(Num_Iteraciones):
                        juegoCoqueto(Agentes)
                        for a in Agentes:
                            a.estado = a.estrategia[(a.estado, a.score)]

                    for a in Agentes:
                        l = estrategias.index(a.estrategia)
                        Ganacias[l] += a.acumulado

    return Ganacias

tallaFinita = []
for i in range(1, 10):
    print('Corriendo con', i*10, 'iteraciones')
    Ganacias = todasCombinaciones(10*i)
    print(Ganacias)
    tallaFinita.append(Ganacias)

data = pd.DataFrame(tallaFinita)
data = data.transpose()
print(data[:3])

archivo = 'tallaFinita.csv'
data.to_csv(archivo, index=False)
print("Data saved to ", archivo)

plt.bar(range(8), Ganacias)

plt.show()
