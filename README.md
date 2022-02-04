# Project 1: Write a data science blog post

## Business Understanding
Purpose of first project was practice work with dataset in Jupyter notebook. 

For someone listening too much music could be one of bad habit but what if I told you that I can guess if you are drinker, smoker or if you are cheating in school just by your music preferencies? I belive that now you checked your Spotify account what do you have in public playlists but dont worry and lets see what we really know about you.


Question 1: What interesting corelation is between bad habbits and music preferencies?
Question 2: What is the proportion of individuals according to the gender?
Question 3: What is the proportion of individuals according to the age?
Question 4: How many of individuals have smoking experience?
Question 5: How many of individuals have alcohol experience?
Question 6: When young people starsts with alcohol?

## Data Understanding
Our dataset “Young People Surve” is from kaggle https://www.kaggle.com/miroslavsabo/young-people-survey and contains answers to questionnaire were collected by students of Statistics class at FSEV UK in Slovakia were they was asked to invite their friends to participate in this survey.
Dataset contains at least 150 unique columns with questions focusen on demographic, music and movies preferencies, bad habbits and other personality related questions asked 1010 individuals.

We selected only part of the dataset and focused on relationship between bad habits like drinking, cheating or smoking and music preferencies. Let's see what we found.

## Prepare Data
In this project following techniques are used:
* NaN drop
* Data imputation with mean
* Creating subset
* Corelation analysis

## Modeling(optional)
not used in this project

## Question 1
**What interesting corelation is between bad habbits and music preferencies?**

Best solution to see interesting relationships between variables is to use corelation table which looks in our case like this:

We used following command to answer our question:
```python
sns.heatmap(data.corr(), annot=True, fmt='.2f', annot_kws={'size':3});
```

![Screen Shot 2022-02-03 at 17 34 46](https://user-images.githubusercontent.com/29026461/152387104-e7a2ec69-b606-4b12-aa62-754b291587e2.png)

There are multiple findings about corelation between bad habits like Smoking or Drinking Alcohol and music preferencies. Some variables has interesting corelations especially HipHop or Reggea with Alcohol or Smoking experience. Other has negative corelations which could also tell something. 

To see more detailed findings please see article published on medium.com https://medium.com/@tomas.lorinc/what-music-youre-listing-tells-about-your-bad-habits-and-why-you-should-protect-your-playlists-bbf6ab5bd35f

## Question 2
**What is the proportion of individuals according to the gender?**

We used following command to answer our question:
```python
(data['Gender_female'].value_counts()/data.shape[0]).plot(kind="bar")
```

![Screen Shot 2022-02-04 at 13 19 53](https://user-images.githubusercontent.com/29026461/152528105-2b85495a-5af9-409d-93f1-aecb170833c3.png)

It looks like proportion of individuals are more over same with 59% (label 1) of females and 40% (label 0) of males

## Question 3
Analyse
Visualise
Explain the visualisation

## Evaluation
Findings



# DataScienceCourse
Project dedicated for DataScience course. 

## Project 1


This part is related to the first project within Data Science course.


## Dataset


## Corelation Table



## How to run code
Please clone repositar including datasets and run Project1.ipynb inside your Jupyter Lab.

Source code is dependant on following modules:

* numpy
* pandas
* matplotlib
* scikit
* seaborn
