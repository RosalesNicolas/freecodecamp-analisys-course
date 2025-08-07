import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import calendar

# cargamos el df en "data"
data = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Nos quedamos con los valores mayores al cuantil inferior y menores al cuantil superior
df = data.copy()
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Realizamos gráfico de linea del df sin los extremos superior e inferior
def draw_line_plot():
    plt.figure(figsize=(18, 6))

    g = sns.lineplot(data=df, x='date', y='value', color='red')
    g.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    plt.xlabel('Date')
    plt.ylabel('Page Views')
    #plt.show()
    g.savefig('line_plot.png')
    return g


def draw_bar_plot():

    df_month = data.resample('M').mean().copy()
    df_month['Year'] = df_month.index.year
    df_month['Month'] = df_month.index.month



    df_month = df.resample('M').mean().copy()
    df_month['Year'] = df_month.index.year
    df_month['Month'] = df_month.index.month
    #df_month['Month'] = df_month['Month'].apply(lambda x: calendar.month_name[x])


    plt.figure(figsize=(10, 10))
    g = sns.barplot(data=df_month, x='Year', y='value', hue='Month', palette='tab20')
    plt.xlabel('Year')
    plt.ylabel('Page Views')    

    handles, labels = g.get_legend_handles_labels()
    g.legend(handles, [calendar.month_name[int(x)] for x in labels], title='Months', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout()
    #plt.show()
    g.savefig('bar_plot.png')
    return g

def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Orden correcto de meses
    month_order = list(calendar.month_abbr)[1:]
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)

    # Crear figura y ejes
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))

    # Boxplot por año
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0], palette="Set2")
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Boxplot por mes
    sns.boxplot(data=df_box, x='month', y='value', ax=axes[1], palette="Set3")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    plt.tight_layout()
    #plt.show()
    fig.savefig('box_plot.png')
    return fig