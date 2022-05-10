# -----------------------------------------------------------
# This file is part of DataScience Project 2
# Main purpose is process ML pipeline and create trained model
# 2022
# License: N/A
# GitHub: lorot19
# -----------------------------------------------------------


# import libraries
import sys
import re
import pandas as pd
from sqlalchemy import create_engine
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import pickle

nltk.download(['punkt', 'wordnet', 'omw-1.4'])

# define regex characters
url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


def load_data(database_filepath, table_name='df'):
    """
    This function loads SQL db provided as argument of function and returns three objects with dropped
    noncathegorical columns
    :param database_filepath: path to the SQL DB
    :param table_name: name of table inside DB

    :return: X: list of all messages
    :return: y: list of all columns with catheghorical variables
    :return: categories: list of all messages
    """
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql_table(table_name, engine)
    X = df['message']
    y = df[df.columns].drop(['id', 'message', 'original', 'genre'], axis = 1)
    #y = df[df.columns[4:]]

    y = y.astype(int)
    categories = y.columns
    return X, y, categories


def tokenize(text):
    """
    Function which tokenize message using regular expressions
    :param text: String containing message
    :return: clean_tokens: list of words containing tokenized and cleaned message
    """
    # get list of all urls using regex
    detected_urls = re.findall(url_regex, text)
    # replace each url in text string with placeholder
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")
    # tokenize text
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    # iterate through each token
    clean_tokens = []
    for tok in tokens:
        # lemmatize, normalize case, and remove leading/trailing white space
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)
    return clean_tokens


def build_model():
    """
    This function prepares model using pipeline and gridsearch
    :return: cv: initialised model
    """
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('Tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))])
    parameters = {'clf__estimator__n_estimators': [3]}

    """
    better parameters but takes longer
    parameters = {
                    'clf__estimator__n_neighbors': [4, 6],
                    'clf__estimator__max_depth': [10, 20]
                    }
    """

    cv = GridSearchCV(pipeline, param_grid=parameters, verbose=3, n_jobs=-1)
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    """
    This function evaluate model, runs prediction and displays results
    :param model: initialised model
    :param X_test: Any
    :param Y_test: Any
    :param category_names: list of cathegory names
    :return: none
    """
    y_pred = model.predict(X_test)
    display_results(model, Y_test, y_pred, category_names)
    pass


def save_model(model, model_filepath):
    """
    This function saves trained model as pickle file
    :param model: trained model
    :param model_filepath: path to save
    :return: none
    """
    # save
    with open(model_filepath, 'wb') as f:
        pickle.dump(model, f)
    pass


def display_results(cv, y_test, y_pred, labels):
    """
    This function visualise trained model
    :param cv: Any
    :param y_test: Any
    :param y_pred: Any
    :param labels: Any
    :return: none
    """
    accuracy = (y_pred == y_test).mean()
    print("Labels:", labels)
    print("Accuracy:", accuracy)
    print("\nBest Parameters:", cv.best_params_)
    pass


def main():
    """
    Main function of train classifier
    :return:
    """
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        print('Building model...')
        model = build_model()

        print('Training model...')
        model.fit(X_train, Y_train)

        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '
              'as the first argument and the filepath of the pickle file to '
              'save the model to as the second argument. \n\nExample: python '
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')
    pass


if __name__ == '__main__':
    main()
