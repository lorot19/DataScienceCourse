import pandas as pd
import pickle
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request
import sklearn
import joblib
from sqlalchemy import create_engine
import os


app = Flask(__name__)

def tokenize(text):
    """
    This function tokenize text from user of app
    :param text: string: message from user
    :return: series of cleaned tokens
    """
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///moviesdata.db')
df = pd.read_sql_table('name', con=engine)

# load model
model = pickle.load("../../../../DataScienceCourse-capstone-project/netflix_model.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
def index():
    return render_template(
    'master.html'
    )


@app.route('/go')
def go():
    """
    Flask, go subpage
    :return:
    """
    # save user input in query
    query = request.args.get('query', '')

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[1:], classification_labels))

    # This will render the go.html Please see that file.
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    """
    Main function
    :return:
    """
    port = int(os.environ.get("PORT", 3001))
    app.run(host='0.0.0.0', port=port, debug=True)


if __name__ == '__main__':
    main()
