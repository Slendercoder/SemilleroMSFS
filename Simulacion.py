import random as rd
import numpy as np
import matplotlib.pyplot as plt

class agente:
    def __init__(self,Estado,Umbral):
        self.estado = Estado
        self.umbral = Umbral
    def decision(self,Macro):
        if Macro >= self.umbral:
            self.estado = 0
        else:
            self.estado = 1

def calcula_macro(agentes):
    a = [i.estado for i in agentes]
    return np.sum(a)/len(a)

def crearAgentesAleatorios(media, sd, Num_Agentes):
    Agentes = []
    for i in range(Num_Agentes):
        estado = rd.randint(0,1)
        centro = rd.normalvariate(media,sd)
        while centro < 0 or centro > 1:
            centro = rd.normalvariate(media,sd)
        a = agente(estado, centro)
        Agentes.append(a)

    return Agentes

def simDesv(Agentes, Num_Iteraciones):

    Estados = []
    Macro = []
    for i in range(Num_Iteraciones):
        Macro.append(calcula_macro(Agentes))
        # print(Macro[-1])
        for a in Agentes:
            a.decision(Macro[-1])

        B = [Agentes[0], Agentes[410], Agentes[510], Agentes[910]]
        Estados.append([a.estado for a in B])

    return Macro, Estados

######################################
# Comienzo ejecucion
######################################

Num_Agentes = 10
media = 0.5
Num_Iteraciones = 100
# Macro = []
# desviacion = 0
# Agentes = [agente(rd.randint(0,1),rd.normalvariate(media,desviacion)) for i in range(Num_Agentes)]
# Estados = [i.estado for i in Agentes]

Agentes = []

# a = agente(0, 0)
# Agentes.append(a)
# a = agente(0, 0.1)
# Agentes.append(a)
# a = agente(1, 0.2)
# Agentes.append(a)
# a = agente(0, 0.3)
# Agentes.append(a)
# a = agente(1, 0.4)
# Agentes.append(a)
# a = agente(0, 0.5)
# Agentes.append(a)
# a = agente(1, 0.6)
# Agentes.append(a)
# a = agente(0, 0.7)
# Agentes.append(a)
# a = agente(1, 0.8)
# Agentes.append(a)
# a = agente(0, 0.9)
# Agentes.append(a)
# a = agente(0, 1)
# Agentes.append(a)

Agentes = []

for i in range(100):
    Agentes.append(agente(rd.randint(0,1), 0.2))

for i in range(400):
    Agentes.append(agente(rd.randint(0,1), 0.48))

for i in range(400):
    Agentes.append(agente(rd.randint(0,1), 0.51))

for i in range(100):
    Agentes.append(agente(rd.randint(0,1), 0.8))

B = [Agentes[0], Agentes[410], Agentes[510], Agentes[910]]
estAux = [a.estado for a in B]
Macro, Estados = simDesv(Agentes, Num_Iteraciones)
Estados.insert(0, estAux)

for i in Estados:
    print(i)

Macros = {}

Macros[0] = Macro

# desviaciones = [0, 0.5]
# Macros = {}
# for sd in desviaciones:
#     # Agentes = crearAgentesAleatorios(media, sd, Num_Agentes)
#     Macro = simDesv(Agentes, Num_Iteraciones)
#     Macros[sd] = Macro

# plt.hist(Estados)
# plt.savefig("Histograma.png")
# print(Macros)

for key in Macros:
    plt.plot(range(Num_Iteraciones), Macros[key], label = key)

plt.legend()

plt.ylim([0,1])

plt.show()
