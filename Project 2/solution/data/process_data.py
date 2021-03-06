# -----------------------------------------------------------
# This file is part of DataScience Project 2
# Main purpose is process ETL pipeline
# 2022
# License: N/A
# GitHub: lorot19
# -----------------------------------------------------------


# import libraries
import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """
    Load both datasets
    :param messages_filepath:
    :param categories_filepath:
    :return:
    """
    #
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    # merge datasets
    df = pd.merge(messages, categories, on='id')
    return df


def clean_data(df):
    """
    Create a dataframe of the 36 individual category columns
    :param df:
    :return:
    """
    #
    categories = df['categories'].str.split(";", expand=True)

    # select the first row of the categories dataframe
    category_colnames = pd.DataFrame()
    for col in categories.iloc[0]:
        category_colnames[(col.split('-', 1)[0])] = (col.split('-', 1)[1])

    # rename original categories column names with extracted ones
    categories.columns = category_colnames.columns.values

    # drop the original categories column from `df
    df.drop('categories', axis=1, inplace=True)

    # clean data in all cells
    categories = categories.applymap(lambda x: x.split('-', 1)[1]).astype(int)

    # concatenate the original dataframe with the new `categories` dataframe
    df = df.merge(categories, left_index=True, right_index=True, how='inner')
    df = df.drop_duplicates()
    df.related.replace(2, 1, inplace=True)
    return df


def save_data(df, database_filename):
    """
    Save dataframe into SQL DB
    :param df:
    :param database_filename:
    :return:
    """
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('df', engine, index=False, if_exists='replace')
    pass


def main():
    """
    Main function of process data pipeline
    :return:
    """
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
