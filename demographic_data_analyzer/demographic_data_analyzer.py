import pandas as pd

# Cargar los datos
data = pd.read_csv("adult_data.csv.csv")

# Calcular el total de registros por raza
race_count = data['race'].value_counts()
print(f'La distribución de registros por raza es:\n{race_count}')

# Calculamos el promedio de edad de los hombres
age_men = data.loc[data["sex"] == 'Male']['age'].mean()
print(f'El promedio de edad de los hombres es: {age_men}')

# Porcentaje de personas con Bachelor's degree
total = data.shape[0]
bachelor = data.loc[data['education'] == 'Bachelors'].shape[0]
porcentaje = round((bachelor/total)*100, 2)
print(f'El porcentaje de personas con Bachelor\'s degree es: {porcentaje}%')

# Porcentaje con educación avanzada que gana más de 50k  
adv_educ = data.loc[((data["education"] == 'Bachelors') | (data["education"] == 'Masters') | (data["education"] == 'Doctorate')) & (data['salary'] == '>50K')].shape[0]
adv_educ_porc = round((adv_educ/total)*100, 2)
print(f'El porcentaje de personas con educación avanzada que gana más de 50k es: {adv_educ_porc}%')

# Porcentaje sin educación avanzada quecobra más de 50k
not_adv_educ = data.loc[~(data["education"].isin(['Bachelors', 'Masters', 'Doctorate'])) & (data['salary'] == '>50K')].shape[0]
not_adv_educ_porc = round((not_adv_educ/total)*100, 2)
print(f'El porcentaje de personas sin educación avanzada que gana más de 50k es: {not_adv_educ_porc}%')

# El mínimo de hora que una persona trabaja por semana
min_hora_sem = float(data["hours-per-week"].min())
print(f'El mínimo de horas que una persona trabaja por semana es: {min_hora_sem}')

# Porcentaje de personas que trabajan el mínimo y cobran más de 50k
min_hora_sem_df = data.loc[(data["hours-per-week"] == min_hora_sem) & (data['salary'] == '>50K')].shape[0]
min_hora_sem_df_porc = round((min_hora_sem_df/total)*100, 2)
print(f'El porcentaje de personas que trabajan el mínimo y cobran más de 50k es: {min_hora_sem_df_porc}%')

# Pais con mayor porcentaje que gana más de 50k
df_mas_50k = data.loc[data['salary'] == '>50K']
pais_mayor_50k = df_mas_50k['native-country'].value_counts().idxmax()
df_mas_50k_porc = round((df_mas_50k.shape[0]/total)*100, 2)
print(f'{pais_mayor_50k} tiene el mayor porcentaje de personas que ganan más de 50k: {df_mas_50k_porc}%')  

# Moda de trabajo con más de 50k en India
df_india = data.loc[data['native-country'] == 'India']
most_common_job = df_india.loc[df_india['salary'] == '>50K']['occupation'].mode()[0]
print(f'La ocupación más común con más de 50k en India es: {most_common_job}')