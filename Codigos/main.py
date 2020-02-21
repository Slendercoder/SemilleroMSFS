import ElFarol as EF
import redes

Num_agentes = 10
Num_iteraciones = 100
TIPO_RED = 0 # COMPLETA
PARS = [Num_agentes, 0.1]
No_exper = 3
inicial = True
UMBRAL = 0.5

print('********************************************************')
print(u'*            Parámetros de la simulacion               *')
print('********************************************************')
print('Num_agentes:', Num_agentes)
print('Num_iteraciones:', Num_iteraciones)
print('TIPO_RED:', TIPO_RED)
print('PARS:', PARS)
print('No_exper:', No_exper)
print('UMBRAL:', UMBRAL)

with open('Identificador' + str(TIPO_RED) + '.txt', 'r') as f:
    identificador = int(f.readline())

f.close()

# print(identificador)
# Generando red a archivo
if TIPO_RED == 0:
    # print('---------')
    # print('Parametros red:', PARS)
    # print('---------')
    redes.random_graph(*PARS)
elif TIPO_RED == 1:
    redes.small_world(*PARS)
elif TIPO_RED == 2:
    redes.scale_free(PARS[0], PARS[0]/4, PARS[0]/8, PARS[1]*0.6, PARS[1])
    
identificador += 1
EF.simulacion(Num_agentes, Num_iteraciones, UMBRAL, inicial, identificador, PARS)

for N in range(No_exper - 1):

    identificador += 1
    EF.simulacion(Num_agentes, Num_iteraciones, UMBRAL, False, identificador, PARS)

with open('Identificador' + str(TIPO_RED) + '.txt', 'w') as f:
    f.write(str(identificador))

f.close()

print('Listo!')
