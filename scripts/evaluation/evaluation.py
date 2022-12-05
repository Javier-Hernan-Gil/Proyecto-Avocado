"""# **Extracción de Carécterísticas**"""

!pip install tsfresh

from tsfresh import extract_features, feature_extraction

"""## Energia

La energia se define como la cuatificación sumada de cada uno de los componenetes de la serie, claculada como: 

<img src="https://tsfresh.readthedocs.io/en/latest/_images/math/590da761ad7dc3cea32756fc232185cd32a391d6.png" width="180
" alt="Mapa de bits">
"""

print("Energia_Precio_Promedio:",feature_extraction.feature_calculators.abs_energy(datos['Precio_Promedio']))
print("Energia_Volumen_Total:",feature_extraction.feature_calculators.abs_energy(datos['Volumen_Total']))
print("Energia_PLU4046:",feature_extraction.feature_calculators.abs_energy(datos['PLU_4046']))
print("Energia_PLU_4225:",feature_extraction.feature_calculators.abs_energy(datos['PLU_4225']))
print("Energia_PLU_4770:",feature_extraction.feature_calculators.abs_energy(datos['PLU_4770']))

Precio_Promedio	Volumen_Total	PLU_4046	PLU_4225	PLU_4770	Tipo	Año	Región

"""# Kurtosis

Es una medida de normalidad que permite concoer el nivel de aproximación gaussiana de la distribución de la serie

"""

print("Curtosis_Precio_Promedio:",feature_extraction.feature_calculators.kurtosis(datos['Precio_Promedio']))
print("Curtosis_Volumen_Total:",feature_extraction.feature_calculators.kurtosis(datos['Volumen_Total']))
print("Curtosis_PLU4046:",feature_extraction.feature_calculators.kurtosis(datos['PLU_4046']))
print("Curtosis_PLU_4225:",feature_extraction.feature_calculators.kurtosis(datos['PLU_4225']))
print("Curtosis_PLU_4770:",feature_extraction.feature_calculators.kurtosis(datos['PLU_4770']))

"""# Numero de picos

cuenta el numero de piscos en una serie de tiempo (donde x-1 y x+1 son menores a x), es un descirptor completo que permite entender la frecuencia y varianza de la serie

"""

print("Número de picos_Precio_Promedio:",feature_extraction.feature_calculators.number_peaks(datos['Precio_Promedio'],3))
print("Número de picos_Volumen_Total:",feature_extraction.feature_calculators.number_peaks(datos['Volumen_Total'],3))
print("Número de picos_PLU4046:",feature_extraction.feature_calculators.number_peaks(datos['PLU_4046'],3))
print("Número de picos_PLU_4225:",feature_extraction.feature_calculators.number_peaks(datos['PLU_4225'],3))
print("Número de picos_PLU_4770:",feature_extraction.feature_calculators.number_peaks(datos['PLU_4770'],3))

"""# Coeficientes de fourier

Permite entender la relaciones frecuenciales y la composicion de la serie en cuestión, util para el analisis de fenomenos periodicos y semiperiodicos.
"""

coefs1 = feature_extraction.feature_calculators.fft_coefficient(datos['Precio_Promedio'],  [{"coeff": 1, "attr": 'real'}, {"coeff": 2, "attr": 'real'}])
coefs2 = feature_extraction.feature_calculators.fft_coefficient(datos['Volumen_Total'],  [{"coeff": 1, "attr": 'real'}, {"coeff": 2, "attr": 'real'}])
coefs3 = feature_extraction.feature_calculators.fft_coefficient(datos['PLU_4046'],  [{"coeff": 1, "attr": 'real'}, {"coeff": 2, "attr": 'real'}])
coefs4 = feature_extraction.feature_calculators.fft_coefficient(datos['PLU_4225'],  [{"coeff": 1, "attr": 'real'}, {"coeff": 2, "attr": 'real'}])
coefs5 = feature_extraction.feature_calculators.fft_coefficient(datos['PLU_4770'],  [{"coeff": 1, "attr": 'real'}, {"coeff": 2, "attr": 'real'}])
print("Coeficientes 1 y 2 de Número de Precio_Promedio:",list(coefs1))
print("Coeficientes 1 y 2 de Volumen_Total:",list(coefs2))
print("Coeficientes 1 y 2 de PLU4046:",list(coefs3))
print("Coeficientes 1 y 2 de PLU_4225:",list(coefs4))
print("Coeficientes 1 y 2 de PLU_4770:",list(coefs5))

"""## **Construcción y entrenamiento del modelo de aprendizaje supervisado**

Para este proyecto se utiliza el **Método Multilayer Perceptron Regressor (MLPR)**

<p align="justify">
Perceptron multicapa (MLP) es un algoritmo de aprendizaje supervisado que aprende una función $f (\cdot): R ^ m \rightarrow R ^ o$
 entrenando en un conjunto de datos, donde  es el número de dimensiones para la entrada y es el número de dimensiones para la salida. Dado un conjunto de características $X = {x_1, x_2, ..., x_m}$
 y un objetivo , puede aprender un aproximador de función no lineal para clasificación o regresión. </p>

<p align="justify">
MLPRegressor implementa un perceptrón multicapa (MLP) que entrena usando retropropagación sin función de activación en la capa de salida, que también se puede considerar que usa la función de identidad como función de activación. Por lo tanto, utiliza el error cuadrado como función de pérdida y la salida es un conjunto de valores continuos.</p>

**Fuente: Documentacíon scikit-learn**

Se entrena el modelo con las particiones de entrenamiento X_train, y_train
"""

from sklearn.neural_network import MLPRegressor
model = MLPRegressor(solver = 'lbfgs',
                   activation = 'relu',
                   hidden_layer_sizes=(10, 25, 100,200),
                   max_iter=3000,                   
                   n_iter_no_change=100, 
                   validation_fraction=0.2,               
                   random_state=1234)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

"""La siguiente gráfica muestra los valores predichos comparados con los valores verdaderos de la partición de pruebas."""

x = data_test.index[k:]

plt.figure(figsize=(12,4), dpi = 105)
plt.plot(x, y_test, ls = "--", label="Valor verdadero (pruebas)")
plt.plot(x, y_pred, ls = '-', label="Valor predicho (pruebas)")
plt.title("Predicción vs valores verdaderos (pruebas)")
plt.legend();

"""# **Fase 4. Evaluación y Análisis de resultados**

### **Validación Cruzada**

Utilizamos  el validador cruzado de series temporales **TimeSeriesSplit**  de scikit-learn para realizar la validación cruzada, teniedno en cuenta que se realiza validación tipo forward chaining según la cantidad de divisiones definidas en el argumento n_splits.
"""

# Definimos el número de splits para realizar cross-validation
from sklearn.model_selection import TimeSeriesSplit
tsp = TimeSeriesSplit(n_splits=k)

"""Utilizamos GridSearchCV para seleccionar los parámetros de entrenamiento del modelo, esto se realiza mediante los siguientes parámetros:

**estimator:**Nuestro modelo MLPRegressor.

**param_grid:** un diccionario en que se indicar los parámetros a evaluar como clave y el conjunto elementos como valor

**cv:** el número de conjuntos en los que se divide los datos, utilizamos TimeSeriesSplit.
"""

params = {    
      'hidden_layer_sizes' : [(180,), (80,), (130,), (100,) ], #Algunas arquitecturas propuestas.
      'activation' : ['logistic', 'tanh', 'relu'] #Funciones de activación.
 }

#Grid Search para el modelo MLPRegressor

tsp = TimeSeriesSplit(n_splits = k)

gsearch = GridSearchCV(estimator = MLPRegressor(solver = 'lbfgs', #Modelo  a explorar.          
                                                random_state=1234,
                                                max_iter= 3000,
                                                n_iter_no_change=50, 
                                                validation_fraction=0.2), 
                        cv = tsp,
                        param_grid = params, 
                        verbose = 3)

gsearch.fit(X_train, y_train)

# Función para Gráficar la predicción de los datos de precio promedio.

def plot_prediction(params, y_test, y_forward, y_last, test_date_index): 
  
  train_data = serie_t.loc[:test_date_index[0]]
  #y_test, y_forward, y_last = ys
  # Graficamos los valores predichos.
  fig = go.Figure(layout = dict(
       title = f'<b> Precio promedio semanal (2015-01-04 a 2018-03-25)</b> <br> {params}',
       dragmode= 'pan', width = 1300, height = 450))
  
  fig.add_trace(go.Scatter(x = train_data.index,  # Datos originales hasta la primer semana predicha. (fechas)
                          y = train_data.values, # Datos originales hasta la primer semana predicha. (precios)
                          mode = 'lines',
                          name = 'Valores de entrenamiento y pruebas'))

  #Gráfica de los valores de prueba reales.
  fig.add_trace(go.Scatter(x = test_date_index,
                          y = y_test,
                          mode='lines+markers',
                          name='Valores reales (y)'))


  #Gráfica de los valores predichos a partir de las ventanas de X_test.
  fig.add_trace(go.Scatter(x = test_date_index, 
                          y = y_forward,
                          mode = 'lines+markers',
                          name = 'Valores predichos a partir de datos reales'))
  
  #Gráfica de los valores predichos a partir de ventanas creadas proceduralmente.
  fig.add_trace(go.Scatter(x = test_date_index,
                          y = y_last,
                          mode='lines+markers',
                          name='Valores predichos a partir de datos predichos'))
  
  fig.show(config = dict({'scrollZoom': True}))

"""El objetivo del entrenamiento del modelo es predecir instancias futuras, para lo cual alimentaremos la serie con los datos predichos para obtener nuevos datos generados por el modelo."""

# Últimos valores de entrenamiento a usar para la predicción.
X_last = X_test[:1]

# Listas con los datos en y, empezando desde el primer valor de pruebas.
y_last =[]
y_forward = []

for i in range(len(X_test)):  
  # Valores predichos a partir de datos reales (X_test)
  y_pred_forward = gsearch.predict(X_test[i: i+1]) 
  y_forward.append(y_pred_forward[0])  
  
  # Valores predichos a partir de datos predichos y retroalimentados.
  y_pred_last = gsearch.predict(X_last)  # Se predice el valor siguiente a partir de datos predichos prevviamente.
  y_last.append(y_pred_last[0])          # Guardamos el valor predicho.

  # Creación de la nueva ventana añadiendo la última predicción.
  X_last = np.roll(X_last, -1)           # Desplazamos todos los valores hacia la izquierda con np.roll
  X_last[0,-1] = y_pred_last             # Guardamos el valor predicho en la última posición del arreglo.

"""Procedemos a graficar las dos prediciones distintas, la primera con los datos predichos y la segunda con los datos reales, utilizamos el atributo .best_params_ de GridSearchCV para tomar los mejores parámetros."""

test_date_index = data_test.index[k:]
plot_prediction(gsearch.best_params_ , y_test, y_forward, y_last, test_date_index)

"""A continuación, vamos a realizar este proceso desde la primera ventana del conjunto de evaluación, y comparar los resultados con los valores obtenidos al predecir a partir de las ventanas de evaluación y con los datos reales.

### **Métricas de Evaluación**
"""

# Datos predichos a partir de datos predichos

print(f"Test Mean Squared Error: {mean_squared_error(y_test, y_last)}")
print(f"Test Mean Absolute Error: {mean_absolute_error(y_test, y_last)}")
print(f"Test Mean squared log error: {mean_squared_log_error(y_test, y_last)}")

# Datos predichos a partir de datos reales
print(f"Test Mean Squared Error: {mean_squared_error(y_test, y_forward)}")
print(f"Test Mean Absolute Error: {mean_absolute_error(y_test, y_forward)}")
print(f"Test Mean squared log error: {mean_squared_log_error(y_test, y_forward)}")

"""#**Análisis y conclusiones preliminares**

De acuerdo al análisis previo se tienen algunas consideraciones generales:

* Lás métricas permiten establecer que el comportamiemto de los datos predichos es muy cercano a los datos de validación. 
*   El modelo tiene una aproximacion buena según las métricas de desempeño establecidas, realizando un ajuste de los hiperparámetros se puede  mejorar el ajuste.
*   El modelo puede predecir algunos comportamientos a corto plazo de de la serie de tiempo.

# **Proyecto - Avocado Markets in the United States**

* **Elaborado por:** Javier Hernan Gil Gómez - Emiliano Rodriguez
