# Baseline Model Report

## Analytic Approach

Se tomó un dataset de los precios del aguacate en EE.UU. con el cual se construyó una serie que permitiera ver el comportamieto del precio promedio durante los años 2015 a 2018, con lo cual se construye un modelo percepetrón multicapa que permite predecir el precio promedio del aguacate de la siguiente semana, utilizando utilizando el historico del precio promedio de las semanas anteriores(archivo .CSV).

## Model Description

* Models and Parameters

El modelo que se usó para desarrollar este proyecto fue un perceptrón multicapa.
Este es un algoritmo de aprendizaje supervisado, el  cuál presenta las siguientes ventajas y desventajas:

### Las ventajas de Perceptron multicapa son:

- Capacidad para aprender modelos no lineales.

- Capacidad para aprender modelos en tiempo real 

### Las desventajas de Perceptron multicapa son:


- MLP con capas ocultas tiene una función de pérdida no convexa donde existe más de un mínimo local. Por lo tanto, diferentes inicializaciones de pesos aleatorios pueden conducir a una precisión de validación diferente.

- MLP requiere ajustar una serie de hiperparámetros, como la cantidad de neuronas, capas e iteraciones ocultas.

- MLP es sensible al escalado de funciones.

En python podemos usar la función MLPRegressor, que permite implementar un perceptrón multicapa (MLP)
 que entrena usando retropropagación sin función de activación en la capa de salida, 
que también puede verse como el uso de la función de identidad como función de activación.

El modelo tiene las siguientes características:

model = MLPRegressor(solver = 'lbfgs',
                   activation = 'relu',
                   hidden_layer_sizes=(5,10, 25, 100,200),
                   max_iter=3000,                   
                   n_iter_no_change=100, 
                   validation_fraction=0.2,               
                   random_state=1234)


## Results (Model Performance)
![](https://drive.google.com/uc?export=view&id=1tbPr6QiS0S__QvhV1CBPg2ftCQoW-gw2)

* Conclusion on Feasibility Assessment of the Machine Learning Task

El preceptrón multicapa para regresión utiliza el error cuadrático, como función de pérdida y la salida es un conjunto de valores continuos. Recordemos que esta es una de las métricas más comúnmente utilizada para las tareas de regresión.Valores más bajos de Error cuadrático medio  indican un mejor ajuste, esta métrica  es una buena medida de la precisión con que el modelo predice la respuesta, y es el criterio más importante para ajustar si el propósito principal del modelo es la predicción.Para el perceptrón multicapa para regresión presentado en este proyecto, como se pudo obervar antes(imágen) presentró un error cuadrático metio de prácticamente de cero, lo cuál indica que modelo propuesto tiene un muy buen ajuste.  

* Discussion on Overfitting (If Applicable)
Recordemos que uno de los principales problemas a que se enfrentan los modelo de machine learning en aprendizaje supervizado es en overfitting. El overfitting en inglés o su traducción en español sobreajuste, puede tener muchas causas pero alguna de ellas, pueden den ser: Complejidad del modelo y poco datos.

En nuestro caso, podemos ver en el  gráfico anterior que nuestro modelo está libre de tal mal que tienden a presentar los modelos de machine learning. Se observa en el gráfico que la dos linea tienen la misma tendencia, y que están muy próximas entre si. La línea discontinua que corresponde a valores verdaderos y la línea continua corresponde a los valores predichos , se puede ver queson muy similares entre sí.
