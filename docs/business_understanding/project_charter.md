# Project Charter

## Business background
HAB es la única organización de aguacate que equipa a toda la industria global para el éxito al recolectar, enfocar y distribuir inversiones para mantener y expandir la demanda de aguacates en los Estados Unidos.

HAB proporciona a la industria datos consolidados de suministro y mercado, realiza investigaciones sobre nutrición, educa a los profesionales de la salud y reúne a personas de todos los rincones de la industria para trabajar colectivamente hacia un crecimiento que beneficie a todos. La organización también recauda y reasigna fondos a California y asociaciones de importadores para beneficiar a países de origen específicos en la promoción de sus marcas de aguacate a clientes y consumidores en todo Estados Unidos.

## Scope

* Construir una serie de tiempo que permita identifcar el comportamiento del precio promedio del aguacate entre el 4 de enero de 2015 al 25 de Marzo del 2018.
* Entrenar un modelo autorregresivo que permita predecir la variable 'precio promedio por unidad' determinando el valor que tomará la variable en el futuro, cuya evaluación se sustentará en una validación cruzada mediante sliding window y forward chaining validation
* El cliente tendra el acceso al modelo final mediante un servicio Web ó aplicación Android para dispositivos móviles.

## Personnel
* Who are on this project:
	* Microsoft:
		* Project lead : Javier Hernan Gil
		* Data scientist(s) : Emiliano Rodríguez
		* Account manager : Juan Sebástian Malagón
	* Client:
		* Data administrator: Grupo HASS AVOCADO BOARD
		* Business contact:Juan Sebástian Malagon - Juan Sebastian Lara
	
## Metrics
* What are the qualitative objectives? (e.g. reduce user churn)
* What is a quantifiable metric  (e.g. reduce the fraction of users with 4-week inactivity)
* Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the  fraction of users with 4-week inactivity by 20%) 
* What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%)
* How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; or comparison of performance after implementation to baseline)
El proyecto de análisis de datos sobre Aguacate Hass en Estados Unidos se basa en los datos obtenidos por HAB, la cual apoya a los proveedores de aguacate con programas de datos estratégicos, de calidad, de oferta y de demanda para que puedan tomar mejores decisiones al administrar su negocio. proporcionan información que es vital para el éxito de la industria, ya sean datos de inventario a corto plazo o datos de consumidores a largo plazo que ayudan a todos en la cadena de suministro a vigilar al consumidor y sus impulsores de compra.

El Informe de datos de categoría proporciona datos procesables a la industria sobre cuándo, dónde y cuánto aguacate vende el canal minorista, tanto en libras como en dólares. Su objetivo es rastrear y monitorear el desempeño del aguacate Hass en el comercio minorista en los Estados Unidos, dividido en 8 regiones separadas y 45 mercados individuales
## Plan
* Phases (milestones), timeline, short description of what we'll do in each phase.
Metas del Proyecto
El desarrollo del proyecto está enmarcado en tres fases, en cada una de ellas se realizan una serie de actividades que permiten alcanzar los objetivos del proyecto. La información central para realizar dicho proyecto, se basa en un Dataset que contiene el precio promedio por unidad de aguacáte clase Hass en algunas regiones y/o cidudades de Estados Unidades entre el período 2015-01-04 y 2018-03-25, entre otras características.

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
3. Presentar algunas consideraciones iniciales según el desempeño del modelo

### **Fase 5. Despliegue del modelo**
1. Desplegar el modelo mediante una aplicación android ó un servicio Web

## Architecture

* Data
  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)
* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
  * all the data, 
  * after some pre-aggregation on-prem,
  * Sampled data enough for modeling 

* What tools and data storage/analytics resources will be used in the solution e.g.,
  * ASA for stream aggregation
  * HDI/Hive/R/Python for feature construction, aggregation and sampling
  * AzureML for modeling and web service operationalization
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Communication
* How will we keep in touch? Weekly meetings?
* Who are the contact persons on both sides?
