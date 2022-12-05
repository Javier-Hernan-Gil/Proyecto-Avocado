"""# **Extracción de Carécterísticas**"""

!pip install tsfresh

from tsfresh import extract_features, feature_extraction

""" ## Energia

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

