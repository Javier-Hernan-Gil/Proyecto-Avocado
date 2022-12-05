# Data and Feature Definitions

Este documento proporciona un eje central para las fuentes de datos sin procesar, los datos procesados/transformados y los conjuntos de funciones. Se proporcionan más detalles de cada conjunto de datos en el informe de resumen de datos.

Para cada dato, se proporciona un informe individual que describe el esquema de datos, el significado de cada campo de datos y otra información que es útil para comprender los datos. Si el conjunto de datos es el resultado de los conjuntos de datos existentes de procesamiento/transformación/ingeniería de características, también se proporcionan los nombres de los conjuntos de datos de entrada y los enlaces a los scripts que se utilizan para realizar la operación.

Para cada conjunto de datos, también se proporcionan los enlaces a los conjuntos de datos de muestra en el directorio de datos  

## Raw Data Sources

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| Dataset 1 | los datos fueron extraidos de https://hassavocadoboard.com/ | Luego de realizar la primera fase del proyecto los datos fueron ubicados en una carpeta Drive [Dataset](https://docs.google.com/spreadsheets/d/1fHdpdgPA7kLffB1pF8g76FjyZfAGQoTUp6dNY12TcJc/edit?usp=sharing)| [Notebook](https://colab.research.google.com/drive/1wCf37UxrxbBZgMYVwoMkG4CdeYVyd0kP?usp=sharing) | [Dataset 1 Report](data_dictionary.md)|

* Para Mayor información del Dataset consulte [Sumario del Dataset](data_dictionary.md)

## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Processed Dataset 1 | [Dataset1](https://docs.google.com/spreadsheets/d/1fHdpdgPA7kLffB1pF8g76FjyZfAGQoTUp6dNY12TcJc/edit?usp=sharing) |[Notebook](https://colab.research.google.com/drive/1wCf37UxrxbBZgMYVwoMkG4CdeYVyd0kP?usp=sharing)| [Reporte Prepro](/scripts/preprocessing/Report_feature_extraction)|

* Processed Data1 summary. Se realiza el proceso de selección,limpieza y transformación de los de los datos, identificando los datos faltantes, valores incorrectos o datos con algún tipo de ruido.


## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Feature Set 1 | [Dataset1](https://docs.google.com/spreadsheets/d/1fHdpdgPA7kLffB1pF8g76FjyZfAGQoTUp6dNY12TcJc/edit?usp=sharing) | [Notebook](https://colab.research.google.com/drive/1wCf37UxrxbBZgMYVwoMkG4CdeYVyd0kP?usp=sharing)| [Reporte Extracción](/scripts/preprocessing/Report_Prepro.txt)

