Table of contents:
1. [ Project 2](#project1)
  * [ Business Understanding ](#project2BU)
  * [ Data Understanding ](#project2DU)
  * [ Data Preparation - ETL pipeline ](#project2DP)
  * [ Machine learning - ML pipeline ](#project2ML)
  * [ Data Understanding ](#project2DU)
  * [ How to run code ](#project2RC)

![Screenshot 2022-05-11 at 10 49 49](https://user-images.githubusercontent.com/29026461/167809715-a54d73ba-1333-4fed-87cd-7acfff87dadc.png)
![Screenshot 2022-05-11 at 10 49 42](https://user-images.githubusercontent.com/29026461/167809789-df6264db-67f3-4aa4-9668-fad0ea85225b.png)


<a name="project2"></a>
# Project 2: Disaster Response Pipeline

<a name="project2BU"></a>
## Business Understanding
Purpose of this project was practice work with pipelines, gridsearch and deploy fully functional web app using flask
Our goal is create app which can cathegorise new messages accodinng to the proper category.

<a name="project2DU"></a>
## Data Understanding
Our data were provided by Udacity in two CSV files. Both of them contains messages across social medias
send during disaster.  

<a name="project2DP"></a>
## Data Preparation - ETL pipeline
In this project following techniques are used:
* Data load and merge using CSV
* NaN drop
* Creating subset
* Catheghorical variables conversion
* Data save using SQL DB

<a name="project2ML"></a>
## Machine learning - ML pipeline
In this project following techniques are used:
* Data load using SQL DB
* Tokenization
* Create model using pipelines
* Optimalisation using GridSearch
* Model evaluation
* Model saving using pickle file

<a name="project2RC"></a>
## How to run code
Please clone repository, install dependencies and run following commands:

    python3 data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db

    python3 models/train_classifier.py data/DisasterResponse.db classifier.pkl 

    python3 app/run.py        

Source code is dependant on following modules:

* numpy
* pandas
* sqlalchemy
* scikit
* pickle
* nltk
* re
* sys

URL to github project: https://github.com/lorot19/DataScienceCourse


