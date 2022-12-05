pip install -U plotly # Versión más reciente de plotly
import numpy as np
import pandas as pd
import datetime
import seaborn as sns 
import plotly
import plotly.graph_objs as go 
import plotly.express as px
import matplotlib.pyplot as plt
%matplotlib inline

# Selección del modelo
from sklearn.model_selection import train_test_split   #Subconjuntos de entrenamiento y pruebas.
from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold #Validación cruzada de K-pliegues.
from sklearn.model_selection import GridSearchCV  #Búsqueda en cuadrícula de hiperparámetros.

# Selección de los datos en series de tiempo
from sklearn.model_selection import TimeSeriesSplit

# Regresores
from sklearn.neural_network import MLPRegressor    #Regresor con red neuronal de tipo percetron multicapa.

# Métricas de rendimiento
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_squared_log_error #Error absoluto, cuadrado, y cuadrado logarítmico.


datos.describe().round(4)
datos['type'].value_counts()
datos['region'].value_counts()
plt.figure(figsize=(18,10))
sns.lineplot(x="region", y="AveragePrice",hue='year',data=dff,palette='gist_rainbow',)
plt.xticks(rotation=90, horizontalalignment="center")
datos.year.value_counts()

#Algunas observaciones generales de los Datos.

#1. Los valores de mayor precio por unidad ocurrieron en los años 2016 y 2017. 
#2. El precio promedio del aguacáte orgánico ha sido superior 1.5 dólares en período entre el 2015 a 2018.
#3. El aguacate tipo organico ha sido más costoso que el aguacate convencional.
#4. El precio máximo del aguacáte Hass ocurrió el año 2016.
