import ElFarol as EF

Num_agentes = 9
Num_iteraciones = 100
TIPO_RED = 0 # COMPLETA

agentes = EF.crear_agentes_aleatorios(Num_agentes)
print('Ronda: 0',end=" ")
print('Estados:', [x.estado[-1] for x in agentes],end=" ")
print('Score:', [x.score[-1] for x in agentes],end=" ")
print('Politicas:', [x.politica[-1] for x in agentes])
# print(agentes)

politicas = EF.crear_politicas()

# CARLOS
agentes = EF.crear_red(agentes)

EF.leer_red(agentes)

for i in range(Num_iteraciones):
    agentes = EF.juega_ronda(agentes, politicas)
    print('\nRonda:', str(i+1),end=" ")
    print('Estados:', [x.estado[-1] for x in agentes],end=" ")
    print('Score:', [x.score[-1] for x in agentes],end=" ")
    agentes = EF.agentes_aprenden(agentes)
    print('Politica:', [x.politica[-1] for x in agentes])


# data = EF.crea_dataframe_agentes(agentes, Num_iteraciones)

# EF.guardar(data, 'agentes.csv')

# # EDGAR
# HISTOGRAMA_USO, GRAFICA_USO_VS_TIEMPO, GRAFICA_PUNTAJE = ANALISIS_ESTRATEGIAS(AGENTES)
#
# # ROJAS
# GRAFICA_ASISTENTES_BAR_VS_RONDA = ANALISIS_ASISTENCIA(AGENTES)
#
# # MIGUEL
# GRAFICA_PUNTAJE_VS_RONDA, GRAFICA_ESTRATEGIA_VS_RONDA = ANALISIS_AGENTES(AGENTES)
