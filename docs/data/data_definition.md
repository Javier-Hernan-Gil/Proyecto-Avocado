# Data and Feature Definitions

This document provides a central hub for the raw data sources, the processed/transformed data, and feature sets. More details of each dataset is provided in the data summary report. 

For each data, an individual report describing the data schema, the meaning of each data field, and other information that is helpful for understanding the data is provided. If the dataset is the output of processing/transforming/feature engineering existing data set(s), the names of the input data sets, and the links to scripts that are used to conduct the operation are also provided. 

For each dataset, the links to the sample datasets in the _**Data**_ directory are also provided. 

_**For ease of modifying this report, placeholder links are included in this page, for example a link to dataset 1, but they are just placeholders pointing to a non-existent page. These should be modified to point to the actual location.**_

## Raw Data Sources

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| Dataset 1 | los datos fueron extraidos de https://hassavocadoboard.com/ | Luego de realizar la primera fase del proyecto los datos fueron ubicados en una carpeta Drive [Dataset](https://docs.google.com/spreadsheets/d/1fHdpdgPA7kLffB1pF8g76FjyZfAGQoTUp6dNY12TcJc/edit?usp=sharing)| [Notebook](https://colab.research.google.com/drive/1uAxEuVDdEszRSOs4Uuo7l8dQY3mCPZCl?usp=sharing) | [Dataset 1 Report](data_dictionary.md)|

* Para Mayor información del Dataset consulte [Sumario del Dataset](data_dictionary.md)

## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Processed Dataset 1 | [Dataset1](https://docs.google.com/spreadsheets/d/1fHdpdgPA7kLffB1pF8g76FjyZfAGQoTUp6dNY12TcJc/edit?usp=sharing) |[Notebook](https://colab.research.google.com/drive/1uAxEuVDdEszRSOs4Uuo7l8dQY3mCPZCl?usp=sharing)| [Reporte Prepro](Report_Prepro.txt)|

* Processed Data1 summary. Se realiza el proceso de selección,limpieza y transformación de los de los datos, identificando los datos faltantes, valores incorrectos o datos con algún tipo de ruido.


## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Feature Set 1 | [Dataset1](link/to/dataset1/report), [Processed Dataset2](link/to/dataset2/report) | [R_Script2.R](link/to/R/script/file/in/Code) | [Feature Set1 Report](link/to/report1)|
| Feature Set 2 | [Processed Dataset2](link/to/dataset2/report) |[SQL_Script2.sql](link/to/sql/script/file/in/Code) | [Feature Set2 Report](link/to/report2)|

* Feature Set1 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set1 Report.>
* Feature Set2 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set2 Report.> 
