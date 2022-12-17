# Baseline Model Report

## Analytic Approach

Se tomó un dataset de los precios del aguacate en EE.UU. con el cual se construyó una serie que permitiera ver el comportamieto del precio promedio durante los años 2015 a 2018, con lo cual se construye un modelo percepetrón multicapa que permite predecir el precio promedio del aguacate de la siguiente semana, utilizando utilizando el historico del precio promedio de las semanas anteriores(archivo .CSV).

## Model Description

* Models and Parameters
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

* Discussion on Overfitting (If Applicable)

* What other Features Can Be Generated from the Current Data

* What other Relevant Data Sources Are Available to Help the Modeling
