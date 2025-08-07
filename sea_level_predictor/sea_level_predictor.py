import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    ruta = 'epa-sea-level.csv'
    df = pd.read_csv(ruta)

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="CSIRO Data", alpha=0.6)
    plt.xlabel("Year")
    plt.ylabel("CSIRO Adjusted Sea Level (mm)")
    plt.title("CSIRO Sea Level Over Time")
    plt.legend()
    plt.grid(True)
    #plt.show()

    # Create first line of best fit
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Crear puntos para graficar la línea
    years_extended = pd.Series(range(df["Year"].min(), 2051))
    line_all = res_all.slope * years_extended + res_all.intercept
    

    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    line_recent = res_recent.slope * years_extended + res_recent.intercept

    # Add labels and title
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="CSIRO Data", alpha=0.6)
    plt.plot(years_extended, line_all, color="red", label="Best Fit (All Data)")
    plt.plot(years_extended, line_recent, color="green", label="Best Fit (From 2000)")
    plt.xlabel("Year")
    plt.ylabel("CSIRO Adjusted Sea Level (mm)")
    plt.title("CSIRO Sea Level and Regression Lines")
    plt.legend()
    plt.grid(True)
    #plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()