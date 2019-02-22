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

######################################
# Comienzo ejecucion
######################################

Num_Agentes = 10
media = 0.5
desviacion = 0
Num_Iteraciones = 10
Macro = []
Agentes = [agente(rd.randint(0,1),rd.normalvariate(media,desviacion)) for i in range(Num_Agentes)]
Estados = [i.estado for i in Agentes]

plt.hist(Estados)
plt.savefig("Histograma.png")
plt.show()

for i in range(Num_Iteraciones):
    Macro.append(calcula_macro(Agentes))
    print(Macro[-1])
    for a in Agentes:
        a.decision(Macro[-1])