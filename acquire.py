# prepare file for anomaly detection exercises
import pandas as pd
import numpy as np

# defining some functions to make it easier. will go in Wrangle function
from env import host, password, user
import os

###################### Getting database Url ################
def get_db_url(db_name, user=user, host=host, password=password):
    """
        This helper function takes as default the user host and password from the env file.
        You must input the database name. It returns the appropriate URL to use in connecting to a database.
    """
    url = f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
    return url

######################### get generic data #########################
def get_any_data(database, sql_query):
    '''
    put in the query and the database and get the data you need in a dataframe
    '''

    return pd.read_sql(sql_query, get_db_url(database))

######################### Acquire function for curriculum logs ##################
def acquire_curriculum_logs(csv_name = "anonymized-curriculum-access-07-2021.txt"):
    '''
    This function reads the csv of curriculum access logs
    If the file name needs to be changed change the default arguement
    '''
    # assign column names to use
    colnames = ['date', 'endpoint', 'user_id', 'cohort_id', 'source_ip']
    # read csv
    df = pd.read_csv(csv_name, 
                 sep="\s", 
                 header=None, 
                 names = colnames, 
                 usecols=[0, 2, 3, 4, 5])
    return df

###################### Acquire for cohort data ######################
def get_full_cohort_data():
    '''
    This function takes care of getting the cohort data from the compiled CSV
    Ensure the data is called 'full_cohort_list.csv'
    '''

    cohorts = pd.read_csv('full_cohort_list.csv')

    return cohorts


def get_cohort_data():
    '''
    DEPRECIATED: USE GET FULL COHORT DATA AND PULL FROM CSV INSTEAD OF SQL DB
    This function takes care of getting the cohort data from the SQL db
    Need env file to make work
    '''

    dbase = 'curriculum_logs'
    sqlquery = 'SELECT * FROM cohorts'

    cohorts = get_any_data(dbase, sqlquery)

    return cohorts


def get_joined_curriculum_data():
    '''
    This function joins the log data and the cohort data
    Returns one dataframe ready to be prepped. 
    '''

    df = acquire_curriculum_logs()

    df2 = get_full_cohort_data()

    df_merge = df.merge(df2, left_on='cohort_id', right_on= 'id', how = 'left')

    cols_to_drop = ['id', 'created_at', 'updated_at', 'deleted_at', 'slack']

    df_merge = df_merge.drop(columns = cols_to_drop)
    
    # fill the nulls with 0s
    df_merge = df_merge.fillna(value = 0)

    return df_merge