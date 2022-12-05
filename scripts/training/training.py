"""# **Fase 3. Análisis y modelamiento de los datos**

###**Construcción de la serie de tiempo**

De acuerdo a los datos del dataframe "avocado.cvs" procedemos a construir una serie de tiempo teniendo como referencia las caracterisiticas fecha y precio promedio.
"""

datos['Fecha'] =pd.to_datetime(datos['Fecha'])
datos.sort_values(by=['Fecha'], inplace=True, ascending=True)
serie=pd.Series(datos['Precio_Promedio'].values, index= datos['Fecha'].values);

serie

"""de acuerdo a lo anterior, procedemos a promediar los valores por semana, obteniedo un serie de los promedios por semana de los precios entre el período 2015-01-04 y 2018-03-25"""

serie_t = serie.resample('W').mean()

"""Según la serie de datos, la fecha de inicio es el 2015-01-04 y el registro se culminó el 2018-03-25, es decir un total de 169 semanas.
La gráfica muestra el comportamiento del precio promedio de aguacáte por unidad.
"""

plt.figure(figsize=(14,4), dpi = 105)
plt.plot(serie_t, label='Precio_Promedio',color='blue',linewidth=2, markersize=16,)
plt.title("Precio promedio por unidad(dólares)")
plt.legend();

"""##**Construcción de las particiones y ventanas**

Para inicar la construcción de nuestro modelo, se crea la particion de entrenamiento y prueba con una ventana de tiempo de 5 semanas.

Usaremos los registros de los primeras 118 semanas para el conjunto de entrenamiento-validación y las siguientes 51 semanas para el conjunto de pruebas.
"""

data_train = serie_t.loc[:'2017-04-02'] #Primeros 118 semanas (70% aprox)
data_test  = serie_t.loc['2017-04-03':] #ültimas 51 semanas (30% aprox).

data_train.shape ,data_test.shape #Tamaño de las particiones.

"""la siguiente función permite crear las ventanas de tiempo, según el tamaño de la ventana y los datos de la serie de tiempo."""

# Función para obtener las ventanas de tiempo.

def sliding_time(st, window_size=1):

  n = st.shape[0] - window_size  

  X = np.empty((n, window_size))
  y = np.empty(n)

  for i in range(window_size, st.shape[0]):   
    y[i - window_size] = st[i]
    X[i- window_size, 0:window_size] = np.array(st[i - window_size:i])
    
  return X, y

"""Para poder contrastar los resultados obtenidos posteriormente por el modelo, debemos crear las ventanas y valores para el entrenamiento-validación utilizando los datos entrenamiento.
De igual forma se deben crear las ventanas y valores para el entrenamiento- validación del modelo utilizando los datos de prueba, para lo cual se utiliza un tamaño de ventana de 5 semanas.
"""

k=21

X_train, y_train = sliding_time(data_train.values, window_size=k)  
print(f"Número de ejemplos de entrenamiento: {X_train.shape[0]} (Ventana de tamaño {X_train.shape[1]})")
print(f"Número de valores a predecir: {y_train.shape[0]}")

X_test, y_test = sliding_time(data_test.values, window_size=k)
print(f"Número de ejemplos de entrenamiento: {X_test.shape[0]} (Ventana de tamaño {X_test.shape[1]})")
print(f"Número de valores a predecir: {y_test.shape[0]}")

"""El valor 30 corresponde al numero de filas de la particíon de prueba menos el tamaño de la ventana

Tomando una ventana de 21 semanas, obtenemos el siguiente DataFrame
"""

#Observaciones de X en formato de DataFrame.
pd.DataFrame(X_train)



