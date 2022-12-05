### **3. Exploración y calidad de los datos**

En esta fase se realizará una exploración inicial del dataset que permita conocer algunos aspectos relevantes de los datos, permitiendo una mayor comprensión del proceso de venta del aguacáte en Estados Unidos. La siguiente tabla muestra algunas estadísticas descriptivas del conjunto de datos, teneindo en cuenta únicamente las variables númericas.
"""

datos.describe().round(4)

"""Algunas observaciones generales de los datos.

1. El  precio promedio de un aguacate tipo Hass es de 1.40 dólares aproximadamente.
2. El precio máximo  de un aguacate tipo Hass entre el 2015 y 2018 fue de 3.25 dólares y minímo de 0.44 dólares  
3. El mayor volumen de venta fue de 62505650

Las variables 'Date', 'AveragePrice', 'Total Volume', '4046', '4225', '4770', 'type' y 'región' son de gran importancia en este análisis, ya que están ligadas directamente a los objetivos del proyecto. A continuación  se muestran las tablas de frecuencia de dichas características.
"""

datos['type'].value_counts()

Grafica1= dff.pivot_table(values='AveragePrice',index='type',columns='year',aggfunc='mean',
                                   margins_name='All').round().plot(kind='bar',figsize=(12, 5),colormap='Greens_r')
Grafica1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xticks(rotation=0, horizontalalignment="center")
plt.title("Relación entre el año y el precio promedio respecto al tipo de aguacate")
plt.xlabel("Tipo de Aguacate")
plt.ylabel("Precio promedio por unidad")
Grafica1

datos['region'].value_counts()

plt.figure(figsize=(18,10))
sns.lineplot(x="region", y="AveragePrice",hue='year',data=dff,palette='gist_rainbow',)
plt.xticks(rotation=90, horizontalalignment="center");

datos.year.value_counts()

"""La siguiente gráfica muestra la relación entre precio promedio por unidad del aguacate clase Hass durante el pperido  2015-2018 respecto al tipo de aguacate. Observando que el valor pormedio ayor durante dicho años ocurrió en el 2017 en el aguacate tipo organico."""

sns.set_style('darkgrid')
ax = sns.catplot(x="year", y="AveragePrice", hue="type", data=datos,kind = "box",height=6, aspect=2,palette="tab10")

"""Algunas observaciones generales de los Datos.

1. Los valores de mayor precio por unidad ocurrieron en los años 2016 y 2017. 
2. El precio promedio del aguacáte orgánico ha sido superior 1.5 dólares en período entre el 2015 a 2018.
3. El aguacate tipo organico ha sido más costoso que el aguacate convencional.
4. El precio máximo del aguacáte Hass ocurrió el año 2016.

# **Fase 2. Preparación y procesamiento de los datos**

##**1. Selección de datos finales y Limpieza de datos**
Se realiza el proceso de limpieza de los datos, identificando los datos faltantes, valores incorrectos o datos con algún tipo de ruido, para dicho proceso se realizan las siguientes etapas:

**1. Identificar caracteristicas (Columnas) con datos faltantes.**
"""

Datos_faltantes =list(datos.columns[dff.isnull().any()])
print('Las características con datos faltos son:')
print(Datos_faltantes)

"""El resultado anterior muestra que el dataset no contiene datos faltantes.

**2. Filtrar las columnas para  establecer los elementos que componen dicha serie y luego realizar un conteo de cada elemento permitiendo reconocer valores con ruido ó inapropiados:**
"""

datos['AveragePrice'].loc[datos['Total Volume']>0]

datos['Total Volume'].loc[datos['Total Volume']>0]

datos['PLU4046'].value_counts()

datos['PLU4046'].value_counts().sum()

datos['PLU4225'].value_counts()

datos['PLU4225'].value_counts().sum()

datos['PLU4770'].value_counts()

datos['PLU4770'].value_counts().sum()

datos['type'].value_counts()

datos['type'].value_counts().sum()

datos['year'].value_counts()

datos['year'].value_counts().sum()

datos['region'].value_counts()

datos['region'].value_counts().sum()

"""**3. La selección de los datos finales luego de realizar la limpieza del dataset está basada en los siguientes aspectos:**

* La caracteristica 'Unnamed' se elimnan ya que es un código de referencia.

* La caracteristica 'Total Bags, Small Bags, Large Bags y Xlarge Bags no son variables de interés según los objetivos planteados.


"""

columns = ['Date','AveragePrice', 'Total Volume', 'PLU4046', 'PLU4225','PLU4770','type','year','region']
datos = datos[columns] 
datos[datos['Date'].notna()]
datos[datos['AveragePrice'].notna()]
datos[datos['Total Volume'].notna()]  
datos[datos['PLU4046'].notna()] 
datos[datos['PLU4225'].notna()]  
datos[datos['PLU4770'].notna()]   
datos[datos['type'].notna()]  
datos[datos['year'].notna()]  
datos[datos['region'].notna()]  
datos.head()

datos.info()

"""##**2. Transformación de los datos**

<p align="justify"> Con el análisis obtenido en el proceso de limpieza y filtrado, teniendo como referencia los objetivos del proyecto se observa que los datos están completos y sin ruido, únicamente se realiza un cambio en el nombre de las características para facilitar su lectura
</p> 

"""

datos.rename(columns={'Date':'Fecha'},inplace=True)
datos.rename(columns={'AveragePrice':'Precio_Promedio'},inplace=True)
datos.rename(columns={'PLU4046':'PLU_4046'},inplace=True)
datos.rename(columns={'PLU4225':'PLU_4225'},inplace=True)
datos.rename(columns={'PLU4770':'PLU_4770'},inplace=True)
datos.rename(columns={'type':'Tipo'},inplace=True)
datos.rename(columns={'year':'Año'},inplace=True)
datos.rename(columns={'region':'Región'},inplace=True)
datos.rename(columns={'Total Volume':'Volumen_Total'},inplace=True);

datos.head()
