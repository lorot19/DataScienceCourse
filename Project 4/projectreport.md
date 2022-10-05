# Data Science Course - Capstone project - Movie name clasifier

#Section 1: Project Definition

##Project Overview:
Imagine life without IMDb, Netflix, HBO Max and other streaming platforms where you can 
find all information about specific movie like story, actors and even filter them using 
genres categories. Imagine that someone tells you just movie name without trailer or movie
pictures and you need to decide if you would like to see that movie or not. Exactly for 
that purpose is our service. Doesnt matter if you are watcher or movie producer you can 
type any movie name and our service will try to predict what movie geners suits best to it.

##Problem Statement: 

Problem definition: Predict one or more movie categories from user provided string (Movie name)

Strategy: 
1. Find suitable and valid datasource for training dataset
2. Analyse selected dataset
3. Preprocess dataset for model training purposes
4. Split and train model using preprocessed dataset
5. Validate model accuracy
6. Develop simple web application providing problem solution using trained model and other techniques
7. Deploy web application to the cloud provider architecture 

##Metrics: 

Most straightforward way to test our solution will be manual test using known movie 
name which is not presented in both training and testing dataset. Using jsut few movie names
we should be able to guess if our solution is accurate or not. However this kind of test is
not very scientific. Better approach could be automate same test as mentioned above however
using larger independent dataset provided from different source. 

Second validation will be using accuracy score on top of our test-train dataset. Accuracy
should be sufficient because our problem is quite simple and straightforward.

#Section 2: Analysis

##Data Exploration: 
Dataset was checked using standard data exploration techniques. We checked size, shape
and proportion of our dataset as well as NaN drop/imputation

##Data Visualisation: 
Our dataset is quite simple so there was not high demand to plot unnecessary graphs however
we were interested in proportion of movie geners after data dataset cleanup. We used standard
techniques and plotly library.

#Section 3: Methodology

##Data Preprocessing: 
Please see provided jupyter notebooks where every step is commented.
##Implementation: 
Please see provided jupyter notebooks where every step is commented.
##Refinement: 
Training parameters were tuned using manual tests and accuracy score.

#Section 4: Results
Fully working public web aplication deployed using CI/CD pipeline to the heroku cloud.

You can find it on this URL: https://movie-name-clasifier.herokuapp.com

Its running on free tier so please be patien. First page load could take few seconds as
heroku needs to wake up our instance if there was no activity for more than 30 minutes.

#Section 5: Conclusion
## Reflection
First of all I am really satisfied that I finished this final projects. When I started 
DS course I had no experience from data science, data analysis and data engineering. 
I learned a lot of new things and it needs more time and practice to be better in 
datasciene. However I tried to follow all reccomendation from previous projects and
do this project as well as I can. I added also something extra which was not covered 
in course. I deplyed whole application to the Heroku cloud which was my first time and
I spent a lot of time debunging why my fully working local solution cant work on heroku.
Finally I solved all issues and now you can enjoy my work from public internet.

## Improvement
1. Extend initial dataset which have now only 5129 individuals
2. Improve proportion of movie categories inside datased as currently used dataset is little bit biased.
3. Improve model evaluation and tune training parameters
4. Improve UX/UI experience on web application
#How to run code

Application is hosted publicly on this url: https://movie-name-clasifier.herokuapp.com

To run it locally please clone repository including datasets.

1. Data preprocessing - please run jupyter notebook with name netflix_prepare_data.ipynb
2. Model training - please run jupyter notebook with name netflix_train_data.ipynb
3. Web Application - please install all dependencies and run app.py using gunicorn
   or directly with command python3 app.py

If you are interested in web aplication only, please use second repository which was created
for auto CI/CD deployment to the heroku cloud: https://github.com/lorot19/DataScienceCourse-capstone-project

Source code is dependant on following modules:
click==8.1.3
Flask==2.1.2
gunicorn==20.0.4
h11==0.14.0
importlib-metadata==5.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
joblib==1.1.0
MarkupSafe==2.1.1
nltk==3.7
numpy==1.23.3
pandas==1.4.2
python-dateutil==2.8.2
pytz==2022.4
regex==2022.9.13
scikit-learn==1.1.2
scipy==1.9.1
six==1.16.0
sklearn==0.0
SQLAlchemy==1.4.35
threadpoolctl==3.1.0
tqdm==4.64.1
uvicorn==0.18.3
Werkzeug==2.2.2
zipp==3.8.1


URL to github project: https://github.com/lorot19/DataScienceCourse