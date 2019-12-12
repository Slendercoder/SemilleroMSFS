import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def bins_labels(bins, **kwargs):
    bin_w = (max(bins) - min(bins)) / (len(bins) - 1)
    plt.xticks(np.arange(min(bins)+bin_w/2, max(bins), bin_w), bins, **kwargs)
    plt.xlim(bins[0], bins[-1])

data = pd.read_csv('agentes.csv')

# Encuentra la frecuencia promedio de uso de las politicas por ronda
data = data.sort_values(['Identificador', 'Politica', 'Ronda'], ascending=[True, True, True])
data['Freq1'] = data.groupby(['Identificador', 'Politica', 'Ronda'])['Politica'].transform('count')
data['Sum1'] = data.groupby(['Identificador', 'Ronda'])['Politica'].transform('size')
data['Freq1'] = data['Freq1'] / data['Sum1']
del data['Sum1']
data = data.sort_values(['Identificador', 'Ronda', 'Politica'], ascending=[True, True, True])
print(data[['Identificador', 'Ronda', 'Politica', 'Freq1']][:15])
data['AV_Freq1'] = data.groupby(['Politica', 'Ronda'])['Freq1'].transform('mean')
data['AV_Freq1_cuad'] = np.std(data['Freq1'])
# data['AV_Freq1_cuad'] = data.apply(lambda x: np.sqrt(np.mean(x['Freq1']*x['Freq1']) - (x['AV_Freq1']*x['AV_Freq1'])), axis=1)

 # - data['AV_Freq1']*data['AV_Freq1']).apply(lambda x: np.sqrt(x))
for key, grp in data.groupby('Politica'):
    print(grp[['Ronda', 'Politica', 'Freq1', 'AV_Freq1', 'AV_Freq1_cuad']][:10])

# # Crea plot de uso promedio de las politicas por ronda
rondas = list(data.Ronda.unique())
# print('Rondas', rondas)
politicas = data.Politica.unique()
lista_colores = ['#d55e00', '#cc79a7', '#0072b2', '#f0e442', '#009e73', '#004949', '#db6d00', '#924900']
colores = {}
for p in range(len(politicas)):
    colores[politicas[p]] = lista_colores[p]
# print(colores)
fig, ax = plt.subplots()
for key, grp in data.groupby('Politica'):
    # print('Trabajando con politica', key)
    av_freq = []
    for Key, Grp in grp.groupby('Ronda'):
        av_freq.append(list(Grp['AV_Freq1'].unique())[0])
    # print(av_freq)
    # print(colores[key])
    ax.plot(rondas, av_freq, label=key, color=colores[key])
ax.set_xlabel('Ronda', fontsize = 14)
ax.set_ylabel('Promedio Frecuencia uso', fontsize = 14)
ax.set_title(u'Frecuencia promedio de uso de las políticas')
print('Dibujando')
plt.legend(loc='best')
plt.show()


# # Crea histograma de uso de las politicas
# fig, ax = plt.subplots()
# bins = range(9)
# bins_labels(bins, fontsize=12)
# grp.hist('Politica', align='mid', bins=bins, grid=False, ax=ax)
# ax.set_xlabel(u'Política', fontsize = 14)
# ax.set_title(u'Frecuencia total de uso de las políticas')
# plt.show()

# # Encuentra el puntaje acumulado por politica
# data = data.sort_values(['Identificador', 'Politica'], ascending=[True, True]).reset_index(drop=True)
# data['AcScorPol'] = data.groupby(['Identificador', 'Politica'])['Puntaje'].transform('sum')
# # print(data[['Politica', 'AcScorPol']][:100])
#
# # Encuentra el puntaje acumulado por politica por ronda
# data['AcScorPolRond'] = data.groupby(['Identificador', 'Politica', 'Ronda'])['Puntaje'].transform('sum')
# # print(data[['Politica', 'Ronda', 'AcScorPolRond']][:10])

# pols = data.Politica.unique()
# print(pols)

# grp = data.groupby('Politica').get_group(pols[4])
# print(grp[:10])
#
# ax = grp.plot(x='Ronda', y='Freq1')

# ax = data.groupby('Politica').plot(x='Ronda', y='Freq1', marker='o')

# ags = data.Agente.unique()
# print(ags)
#
# grp = data.groupby('Agente').get_group(ags[0])
# print(grp)
#
# ax = grp.plot(x='Ronda', y='Politica')

# ax = data.plot.bar(x='Politica', y='AcScorPol')

# ax = data.groupby('Politica').plot(x='Ronda', y='AcScorPolRond', marker='o')

# plt.show()

# # EDGAR
# HISTOGRAMA_USO, GRAFICA_USO_VS_TIEMPO, GRAFICA_PUNTAJE = ANALISIS_ESTRATEGIAS(AGENTES)
#
# # ROJAS
# GRAFICA_ASISTENTES_BAR_VS_RONDA = ANALISIS_ASISTENCIA(AGENTES)
#
# # MIGUEL
# GRAFICA_PUNTAJE_VS_RONDA, GRAFICA_ESTRATEGIA_VS_RONDA = ANALISIS_AGENTES(AGENTES)
