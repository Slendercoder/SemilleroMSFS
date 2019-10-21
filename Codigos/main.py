import ElFarol as EF

Num_agentes = 2
Num_iteraciones = 10
TIPO_RED = 0 # COMPLETA

agentes = EF.crear_agentes_aleatorios(Num_agentes)
# print(agentes)

politicas = EF.crear_politicas()

# CARLOS
red = EF.crear_red(agentes)

# YA
agentes = EF.juega_ronda(agentes, politicas)
# print(agentes)

# ESTEBAN
agentes = EF.agentes_aprenden(agentes, red)

print([x.score[-1] for x in agentes])

# # MARIA JOSE
# SIMULACION(Num_Iteraciones)
#     RONDA
#     APRENDIZAJE

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
