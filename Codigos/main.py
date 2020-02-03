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

identificador += 1
EF.simulacion(Num_agentes, Num_iteraciones, UMBRAL, TIPO_RED, PARS, inicial, identificador)

for N in range(No_exper - 1):

    identificador += 1
    EF.simulacion(Num_agentes, Num_iteraciones, UMBRAL, TIPO_RED, PARS, False, identificador)

with open('Identificador' + str(TIPO_RED) + '.txt', 'w') as f:
    f.write(str(identificador))

f.close()

print('Listo!')
