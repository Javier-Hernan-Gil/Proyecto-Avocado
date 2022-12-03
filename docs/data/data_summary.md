# Repor de Datos

En esta fase se realizará una exploración inicial del dataset que permita conocer algunos aspectos relevantes de los datos, permitiendo una mayor comprensión del proceso de venta del aguacáte en Estados Unidos. La siguiente tabla muestra algunas estadísticas descriptivas del conjunto de datos, teniendo en cuenta únicamente las variables númericas.

## Resumen general de los datos

La siguiente descripción incial del dataset permite conocer las posibles variables quese pueden analizar, que conlleve a una selección de los datos de acuerdo a los objetivos del proyecto. Las caracterísitcas mas relevantes para nuesntro análisis son:

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

Las características Total Bags, Small Bags, Large Bags y Xlarge Bags corresponde al número de bolsas de aguacates vendidos en la fecha correspondiente

## Resumen de calidad de datos

Algunas observaciones generales de los datos.

1. El  precio promedio de un aguacate tipo Hass es de 1.40 dólares aproximadamente.
2. El precio máximo  de un aguacate tipo Hass entre el 2015 y 2018 fue de 3.25 dólares y minímo de 0.44 dólares  
3. El mayor volumen de venta fue de 62505650
4. Los valores de mayor precio por unidad ocurrieron en los años 2016 y 2017. 
5. El precio promedio del aguacáte orgánico ha sido superior 1.5 dólares en período entre el 2015 a 2018.
6. El aguacate tipo organico ha sido más costoso que el aguacate convencional.
7. El precio máximo del aguacáte Hass ocurrió el año 2016.

## Variable objetivo
AveragePrice: Precio promedio de un solo aguacate
## Variables individuales

Date: La fecha de la observación
AveragePrice: Precio promedio de un solo aguacate

## Clasificación de variables

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

## Relación entre variables explicativas y variable objetivo

De acuerdo a los datos del dataframe "avocado.cvs" procedemos a construir una serie de tiempo teniendo como referencia las caracterisiticas fecha y precio promedio.











