import pandas as pd
import ElFarolFunciones as F
import redes1

def main(Num_agentes, Num_iteraciones, Num_experimentos):

    redes1.create_graph(Num_agentes, 'Kregular', 4, True)

    identificador = 0
    UMBRAL = 0.5
    inicial = True
    PARS = [Num_agentes, 1]

    F.simulacion(Num_agentes,Num_iteraciones,0.5,inicial,identificador,PARS)

    inicial = False
    for N in range(Num_experimentos - 1):
        identificador += 1
        F.simulacion(Num_agentes,Num_iteraciones,UMBRAL,inicial,identificador,PARS)

    data = pd.read_csv('agentes.csv')

    data['Num_agentes'] = Num_agentes
    data['Tipo_red'] = '4-Regular'

    return data

print(main(50,50,50))
