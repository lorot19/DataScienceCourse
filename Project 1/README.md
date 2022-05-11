Table of contents:
1. [ Project 1](#project1)
  * [ Business Understanding ](#project1BU)
  * [ Data Understanding ](#project1DU)
  * [ Data Preparation ](#project1DP)
  * [ Data Modeling ](#project1DM)
  * [ Q1: What interesting corelation is between bad habbits and music preferencies? ](#project1Q1)
  * [ Q2: What is the proportion of individuals according to the gender? ](#project1Q2)
  * [ Q3: What is the proportion of individuals according to the age? ](#project1Q3)
  * [ Q4: How many of individuals have smoking experience? ](#project1Q4)
  * [ Q5: How many of individuals have alcohol experience? ](#project1Q5)
  * [ Q6: When young people starsts with alcohol? ](#project1Q6)
  * [ Evaluation ](#project1E)
  * [ How to run code ](#project1RC)



<a name="project1"></a>
# Project 1: Write a data science blog post

<a name="project1BU"></a>
## Business Understanding
Purpose of first project was practice work with dataset in Jupyter notebook. 

For someone listening too much music could be one of bad habit but what if I told you that I can guess if you are drinker, smoker or if you are cheating in school just by your music preferencies? I belive that now you checked your Spotify account what do you have in public playlists but dont worry and lets see what we really know about you.

Question 1: What interesting corelation is between bad habbits and music preferencies?
Question 2: What is the proportion of individuals according to the gender?
Question 3: What is the proportion of individuals according to the age?
Question 4: How many of individuals have smoking experience?
Question 5: How many of individuals have alcohol experience?
Question 6: When young people starsts with alcohol?

<a name="project1DU"></a>
## Data Understanding
Our dataset “Young People Surve” is from kaggle https://www.kaggle.com/miroslavsabo/young-people-survey and contains answers to questionnaire were collected by students of Statistics class at FSEV UK in Slovakia were they was asked to invite their friends to participate in this survey.
Dataset contains at least 150 unique columns with questions focusen on demographic, music and movies preferencies, bad habbits and other personality related questions asked 1010 individuals.

We selected only part of the dataset and focused on relationship between bad habits like drinking, cheating or smoking and music preferencies. Let's see what we found.

<a name="project1DP"></a>
## Data Preparation
In this project following techniques are used:
* NaN drop
* Data imputation with mean
* Creating subset
* Corelation analysis

<a name="project1DM"></a>
## Modeling(optional)
not used in this project

<a name="project1Q1"></a>
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

<a name="project1Q2"></a>
## Question 2
**What is the proportion of individuals according to the gender?**

We used following command to answer our question:
```python
(data['Gender_female'].value_counts()/data.shape[0]).plot(kind="bar")
```

![Screen Shot 2022-02-04 at 13 19 53](https://user-images.githubusercontent.com/29026461/152528105-2b85495a-5af9-409d-93f1-aecb170833c3.png)

It looks like proportion of individuals are more over same with 59% (label 1) of females and 40% (label 0) of males

<a name="project1Q3"></a>
## Question 3
**What is the proportion of individuals according to the age?**

We used following command to answer our question:
```python
(data['Age'].value_counts()/data.shape[0]).plot(kind="bar")
```

![Screen Shot 2022-02-04 at 13 24 58](https://user-images.githubusercontent.com/29026461/152528713-ae82e680-df30-4ea3-8588-6613cab2b6e6.png)

Dataset is based mainly on data from young people between 18 and 22 years

<a name="project1Q4"></a>
## Question 4
**How many of individuals have smoking experience?**

We used following command to answer our question:
```python
(data['SmokingExperience'].value_counts()/data.shape[0]).plot(kind="bar")
```
![Screen Shot 2022-02-04 at 13 26 25](https://user-images.githubusercontent.com/29026461/152528891-15b124f8-b977-405d-a395-db0e29c1e28d.png)

Interesting is that at least 80% of young people has smoking experience. (label 1 means that individuals have smoking experience)

<a name="project1Q5"></a>
## Question 5
**How many of individuals have alcohol experience?**

We used following command to answer our question:
```python
(data['AlcoholExperience'].value_counts()/data.shape[0]).plot(kind="bar")
```

![Screen Shot 2022-02-04 at 13 28 56](https://user-images.githubusercontent.com/29026461/152529192-fc0f72d6-b84e-4402-b25b-f651990ff767.png)

Almost 88% of individuals has some Alcohol experience. (label 1 means that individuals have drinking experience)

<a name="project1Q6"></a>
## Question 6
**When young people starsts with alcohol?**

We used following command to answer our question:
```python
(data.groupby('Age').mean()['AlcoholExperience'].sort_values()).plot(kind="bar")
```

![Screen Shot 2022-02-04 at 13 31 20](https://user-images.githubusercontent.com/29026461/152529543-489ab795-f9c3-469d-83df-94d7134704ea.png)

It looks like 44% of young individuals starts with alcohol at age 15 while 100% have some experince at 28years

<a name="project1E"></a>
## Evaluation
It looks like there are some corelations between bad habits and music preferencies which means that even our public Spotify playlist should be protected and considered as private data. Please find more findings in that article: https://medium.com/@tomas.lorinc/what-music-youre-listing-tells-about-your-bad-habits-and-why-you-should-protect-your-playlists-bbf6ab5bd35f

<a name="project1RC"></a>
## How to run code
Please clone repositar including datasets and run Project1.ipynb inside your Jupyter Lab.

Source code is dependant on following modules:

* numpy
* pandas
* matplotlib
* scikit
* seaborn

URL to github project: https://github.com/lorot19/DataScienceCourse


