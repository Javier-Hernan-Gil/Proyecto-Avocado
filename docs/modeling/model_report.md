# Final Model Report

El modelo final que se reporta es un perceptrón multicapa para regresión, el cuál  tiene las siguientes características:

El perceptrón multicapa esta compuesto  por una capa de entrada, una capa de salida y k capas ocultas entremedias.

En el perceptrón multicapa se distinguen dos etapas importantes:

- Propagación en la que se calcula el resultado de salida de la red desde los valores de entrada hacia delante.

- Aprendizaje en la que los errores obtenidos a la salida del perceptrón se van propagando hacia atrás (backpropagation) con el objetivo de modificar los pesos de las conexiones para que el valor estimado de la red. 

## Data
Los datos que se reportan para la realización del proyecto provienen del  escaneo de minorista semanales entre los años 2015 a 2018 para el volumen minorista nacional (unidades) y el precio. Los datos de escaneo minorista provienen directamente de las cajas registradoras de los minoristas en función de las ventas minoristas reales de aguacates Hass.
## Features

Las carácterísticas princnipales que se usraón para poder realizar la tarea de predicción con el perceptrón multicapa para regresión, fueron:
Date: La fecha de la observación
AveragePrice: Precio promedio de un solo aguacate
Total Volume: Número total de aguacates vendidos
4046: Número total de aguacates vendidos con PLU 4046
4225: Número total de aguacates vendidos con PLU 4225
4770: Número total de aguacates vendidos con PLU 4770
type: Convencional u orgánico
year: Año
Region: Ciudad o región de la observación
Los códigos de búsqueda de productos (PLU) de la tabla son solo para aguacates Hass, otra clase de aguacates no fueron consignados en esta tabla.
Las características Total Bags, Small Bags, Large Bags y Xlarge Bags corresponde al número de bolsas de aguacates vendidos en la fecha correspondiente.

## Algorithm
La tarea que se pretendía realizar pertence al aprendizaje supervisado. Se deseaba como bien se ha mencionado antes, predecir a partir de algunas características de interés, ya mencionadas, el precio promedio del aguacate.  El algorítmo que se aplicó usando python fue:
model = MLPRegressor(solver = 'lbfgs',
                   activation = 'relu',
                   hidden_layer_sizes=(5,10, 25, 100,200),
                   max_iter=3000,                   
                   n_iter_no_change=100, 
                   validation_fraction=0.2,               
                   random_state=1234)

## Results
Los resultados de haber aplicado nuestro modelo de red neuronal perceptrón multicapa para regrsión, podemos decir que son resultados satisfactorios, dado que el observar las métricas para el monitoreo de la perdida, estas métricas presentarón valores muy bajos, valores práctica mente de cero. 
