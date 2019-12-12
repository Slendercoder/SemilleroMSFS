import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def bins_labels(bins, **kwargs):
    bin_w = (max(bins) - min(bins)) / (len(bins) - 1)
    plt.xticks(np.arange(min(bins)+bin_w/2, max(bins), bin_w), bins, **kwargs)
    plt.xlim(bins[0], bins[-1])

data = pd.read_csv('agentes.csv')

data = data.sort_values(['Ronda', 'Politica'], ascending=[True, True]).reset_index(drop=True)
print(data[:10])

# bins = range(8)
# ax = data.hist('Politica', align='mid', bins=bins, grid=False)
# bins_labels(bins, fontsize=16)
# plt.show()

data['Freq1'] = data.groupby(['Politica', 'Ronda'])['Politica'].transform('count')
print(data[:10])

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

data = data.sort_values(['Politica'], ascending=[True]).reset_index(drop=True)
data['AcScorPol'] = data.groupby('Politica')['Puntaje'].transform('sum')
print(data[['Politica', 'AcScorPol']][:100])

ax = data.plot.bar(x='Politica', y='AcScorPol')

data['AcScorPolRond'] = data.groupby(['Politica', 'Ronda'])['Puntaje'].transform('sum')
print(data[['Politica', 'Ronda', 'AcScorPolRond']][:10])
#
# ax = data.groupby('Politica').plot(x='Ronda', y='AcScorPolRond', marker='o')

plt.show()

# # EDGAR
# HISTOGRAMA_USO, GRAFICA_USO_VS_TIEMPO, GRAFICA_PUNTAJE = ANALISIS_ESTRATEGIAS(AGENTES)
#
# # ROJAS
# GRAFICA_ASISTENTES_BAR_VS_RONDA = ANALISIS_ASISTENCIA(AGENTES)
#
# # MIGUEL
# GRAFICA_PUNTAJE_VS_RONDA, GRAFICA_ESTRATEGIA_VS_RONDA = ANALISIS_AGENTES(AGENTES)
