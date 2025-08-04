import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos
data = pd.read_csv('medical_examination.csv')

data['overweight'] = np.where(
    data['weight'] / ((data['height'] / 100) ** 2) > 25,
    1,  # Si es mayor a 25 → 1
    0   # Si no → 0
)

# Normalizamos Colesterol y glucosa a 0 si en 1 y dejamos en 1 si tiene riesgo (valores mayores a 1)
data['cholesterol'] = np.where(data['cholesterol'] > 1, 1, 0)
data['gluc'] = np.where(data['gluc'] > 1, 1, 0)

def draw_cat_plot():
    # 5 - Pasar a formato largo
    df_cat = pd.melt(
        data,
        id_vars=['cardio'],
        value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    )

    # 6 - Agrupar por categoría (conteos)
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])['value'].count().reset_index(name='total')

    # 7 - Crear el gráfico categórico
    g = sns.catplot(
        data=df_cat,
        x='variable', y='total',
        hue='value',
        col='cardio',
        kind='bar',
        height=5, aspect=1
    )

    # 8 - Obtener la figura desde el FacetGrid
    fig = g.fig

    # 9 - Guardar y devolver
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    # 11 - Limpiar datos
    df_heat = data[
    (data['ap_lo'] <= data['ap_hi']) &
    (data['height'] >= data['height'].quantile(0.025)) &
    (data['height'] <= data['height'].quantile(0.975)) &
    (data['weight'] >= data['weight'].quantile(0.025)) &
    (data['weight'] <= data['weight'].quantile(0.975))
]

    # 12 - Correlación
    corr = df_heat.corr()

    # 13 - Máscara superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14 - Crear figura y ejes
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15 - Dibujar heatmap
    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask,
                square=True, linewidths=.5, ax=ax)

    # 16 - Guardar y devolver
    fig.savefig('heatmap.png')
    return fig

# Llamar a las funciones para generar los gráficos
draw_cat_plot()
draw_heat_map()