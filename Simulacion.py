import random as rd
import numpy as np
import matplotlib.pyplot as plt

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

Ganacias = [0]*8
Num_Iteraciones = 10

for i in estrategias:
    print(i)
    for j in estrategias:
        for k in estrategias:
            Agentes = []
            # print('k', k)
            a = agente(rd.randint(0, 1), 0, 0, i)
            Agentes.append(a)
            a = agente(rd.randint(0, 1), 0, 0, j)
            Agentes.append(a)
            a = agente(rd.randint(0, 1), 0, 0, k)
            Agentes.append(a)

            for T in range(Num_Iteraciones):
                juegoCoqueto(Agentes)
                for a in Agentes:
                    a.estado = a.estrategia[(a.estado, a.score)]

            for a in Agentes:
                l = estrategias.index(a.estrategia)
                Ganacias[l] += a.acumulado

# Ganacias = [0, 1, 2, 3, 4, 3, 2, 1]

print(Ganacias)

plt.bar(range(8), Ganacias)

plt.show()
