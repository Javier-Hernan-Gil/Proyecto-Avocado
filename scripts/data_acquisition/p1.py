# -*- coding: utf-8 -*-
"""Copia de Proyecto - Mercado de Aguacate en Estados Unidos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wCf37UxrxbBZgMYVwoMkG4CdeYVyd0kP

![](https://drive.google.com/uc?export=view&id=1ugpRfZ7DXMLZPpATxvtZfCUIMv871b0s)

HAB es la única organización de aguacate que equipa a toda la industria global para el éxito al recolectar, enfocar y distribuir inversiones para mantener y expandir la demanda de aguacates en los Estados Unidos.

HAB proporciona a la industria datos consolidados de suministro y mercado, realiza investigaciones sobre nutrición, educa a los profesionales de la salud y reúne a personas de todos los rincones de la industria para trabajar colectivamente hacia un crecimiento que beneficie a todos. La organización también recauda y reasigna fondos a California y asociaciones de importadores para beneficiar a países de origen específicos en la promoción de sus marcas de aguacate a clientes y consumidores en todo Estados Unidos.

### **Misión**
 
<p align="justify"> 
HAB existe para apoyar a las partes interesadas de la industria mundial del aguacate en nuestros esfuerzos colectivos hacia la expansión del mercado en los EE. UU. Proporcionan a los productores datos de volumen, proyecciones, conocimientos de mercado y otras herramientas comerciales para ayudarlos a tomar buenas decisiones comerciales.</p>  



### **Visión**
<p align="justify"> 
HAB es el catalizador para que los aguacates sean la fruta más consumida en los EE. UU. Y las partes interesadas de la industria tengan éxito. Brindando a los productores, comercializadores, profesionales de la salud y consumidores datos, investigaciones e información fiables e imparciales sobre el aguacate para impulsar el crecimiento de la categoría. </p> 

### **Objetivos Estratégicos**


Seis prioridades estratégicas respaldan la visión a largo plazo de la Junta de ser el catalizador para que los aguacates frescos sean la fruta consumida número uno en los EE. UU. Y las partes interesadas de la industria tengan éxito:

* Construir demanda
* Nutrición
* Datos de oferta y demanda
* Calidad
* Compromiso de la industria
* Sustentabilidad 

**Fuente:** https://hassavocadoboard.com/

# **Proyecto -  "Avocado Markets in the United States"**

<p align="justify">  El proyecto de análisis de datos sobre  Aguacate Hass en Estados Unidos se basa en los datos obtenidos por HAB, la cual  apoya a los proveedores de aguacate con programas de datos estratégicos, de calidad, de oferta y de demanda para que puedan tomar mejores decisiones al administrar su negocio. proporcionan información que es vital para el éxito de la industria, ya sean datos de inventario a corto plazo o datos de consumidores a largo plazo que ayudan a todos en la cadena de suministro a vigilar al consumidor y sus impulsores de compra.

<p align="justify"> El Informe de datos de categoría proporciona datos procesables a la industria sobre cuándo, dónde y cuánto aguacate vende el canal minorista, tanto en libras como en dólares. Su objetivo es rastrear y monitorear el desempeño del aguacate Hass en el comercio minorista en los Estados Unidos, dividido en 8 regiones separadas y 45 mercados individuales. </p>

## **Metas del Proyecto**
<p align="justify">
El desarrollo del proyecto está enmarcado en tres fases, en cada una de ellas se realizan una serie de actividades que permiten alcanzar los objetivos del proyecto. La información central para realizar dicho proyecto, se basa en un Dataset que contiene el precio promedio por unidad de aguacáte clase Hass en algunas regiones y/o cidudades de Estados Unidades entre el período 2015-01-04 y 2018-03-25, entre otras características.</p>

## **Objetivos del Proyecto**

* Construir una serie de tiempo que permita identifcar el comportamiento del precio promedio del aguacate entre el 4  de enero de 2015 al 25 de Marzo del 2018.

* Entrenar un modelo autorregresivo que permita predecir la variable 'precio promedio por unidad' determinando el valor que tomará la variable en el futuro, cuya evaluación se sustentará en una validación cruzada mediante sliding window y forward chaining validation

##**Fases del Proyecto**
Para el desarrollo se plantean algunas actividades generales en las siguientes fases:
### **Fase 1. Selección y análisis exploratorio de los datos** 

1. Presentar la información general del dataset.
2. Selecionar las variables relevantes para el análisis.
3. Realizar un análisis exploratorio  de las variables del dataset, mediante gráficos y algunas estadísticas descriptivas.

### **Fase 2. Preparación y Procesamiento de los datos** 
1. Efectuar el proceso de limpieza y filtarado de dataset, que permita identificar si hay valores faltantes, incorrectos o con ruido.
2. Renombrar algunas variables y registros que permitan uniformidad en los datos.

### **Fase 3. Análisis y modelamiento de los datos** 
1. Construir la serie de tiempo de los precios promedios por unidad del aguacate tipo Hass en algunas regiones de los Estados Unidos.
2. Utilizar el Método Multilayer Perceptron Regressor (MLPR) junto GridSearchCV para encontrar los mejores parámetros.
3. Utilizar el validador cruzado de series temporales TimeSeriesSplit de scikit-learn realizando una validación tipo forward chaining.

### **Fase 4. Evaluación y resultados** 
1. Realizar predicion del precio promedio basado en particiones de los datos conocidos.
2. Evaluar el modelo mediante algunas métricas de desempeño.
3. Presentar algunas consideraciones iniciales según el desempeño del modelo.

##**Instalación de Paquetes y Librerias**

Para iniciar el análisis, se instalan los paquetes y librerias necesarias.
"""

# Commented out IPython magic to ensure Python compatibility.
!pip install -U plotly # Versión más reciente de plotly
import numpy as np
import pandas as pd
import datetime
import seaborn as sns 
import plotly
import plotly.graph_objs as go 
import plotly.express as px
import matplotlib.pyplot as plt
# %matplotlib inline

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

"""El análisis realizado tuvo como base un conjunto de datos registrado en Kaggle, obtenido de la página oficial de Hass Avocado Board  en http://www.hassavocadoboard.com/retail/volume-and-price-data por lo cual es un proyecto netamente academico sin fines comerciales.
Este material fue realizado con las siguientes versiones:

- Python 3.6.9

- Pandas 1.0.5

- NumPy 1.18.5

- Seaborn 0.10.1

- Plotly 0.10.1

- Scipy 0.10.1


"""

!python --version
print('Pandas', pd.__version__)
print('numpy', np.__version__)
print('seaborn', sns.__version__)
print('plotly', sns.__version__)
print('scipy', sns.__version__)

"""# **Fase 1. Entendimiento de los datos**

### **1. Recoleción inicial de los datos**

<p align="justify"> En esta fase se realizará una exploración inicial del dataset "avocado.csv" obtenido de Kaggle, el cual puede ser verficado de la página oficial de Hass Avocado Board  en http://www.hassavocadoboard.com/retail/volume-and-price-data. La siguiente tabla representa los datos de escaneo minorista semanales entre los años 2015 a 2018 para el volumen minorista nacional (unidades) y el precio. Los datos de escaneo minorista provienen directamente de las cajas registradoras de los minoristas en función de las ventas minoristas reales de aguacates Hass.</p>
"""

from google.colab import drive
drive.mount('/content/drive', force_remount=True)
datos= pd.read_excel("/content/drive/MyDrive/Curso_ML_Avanzado/Metodologias/Avocado.xlsx")

dff=datos.copy()

"""####**Información general del dataset**

El resumen de las variables del dataset y su número de registros se muestran a continuación:


"""

# Ejecutar para visuzalizar la información general del Dataset
datos.info()#14 columnas

"""### **2. Descripción de los datos**

La siguiente descripción incial del dataset permite conocer las posibles variables quese pueden analizar, que conlleve a una selección de los datos de acuerdo a los objetivos del proyecto. Las caracterísitcas mas relevantes para nuesntro análisis son: 

* **Date:** La fecha de la observación
* **AveragePrice:** Precio promedio de un solo aguacate
* **Total Volume:** Número total de aguacates vendidos
* **PLU4046:** Número total de aguacates vendidos con PLU 4046 
* **PLU4225:** Número total de aguacates vendidos con PLU 4225 
* **PLU4770:** Número total de aguacates vendidos con PLU 4770 
* **type:** Convencional u orgánico
* **year:** Año
* **Region:** Ciudad o región de la observación

Los códigos de búsqueda de productos (PLU) de la tabla son solo para aguacates Hass, otra clase de aguacates no fueron consignados en esta tabla. 

Las características **Total Bags, Small Bags, Large Bags y Xlarge Bags** corresponde al número de bolsas de aguacates vendidos en la fecha correspondiente

"""

datos.head(10)

"""Se observa que la mayoria de variables son númericas y las variables categóricas son Type y Región.

"""
