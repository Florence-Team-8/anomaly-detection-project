
import pandas as pd
import numpy as np
import scipy.stats as stats
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from datetime import datetime

def active_status(df, date, start, end):
    ''' this function creates a boolean column that stores True if the date given falls 
    within the start and end dates. Outputs a new column named 'is_active'''
    df['is_active'] = (date >= df[start]) & (date <= df[end])
    return df

def make_datetime(df, col_name, set_index = False):
    '''
    This function takes in a dataframe 
    A column name of the column that is your date (as string)
    Performs basic to_datetime conversion and sets tha column as the index
    '''
    if set_index == True:
        df[col_name] = pd.to_datetime(df[col_name])
        df = df.set_index(col_name)
        return df
    else:
        df[col_name] = pd.to_datetime(df[col_name])
    return df

def get_lower_and_upper_bounds(col, multiplier=1.5):
    ''''''
    # calculate quantiles with pd.quantile()
    q1 = col.quantile(0.25)
    q3 = col.quantile(0.75)
    # then calculate iqr to calculate the upper/lower bounds
    iqr = q3 - q1   
    lower_bound = round(q1 -(multiplier * iqr), 3)
    upper_bound = round(q3 +(multiplier * iqr), 3)
    
    return lower_bound, upper_bound

def iqr_outliers(df, multiplier=1.5):
    # create empty outlier dictionary to hold values
    outliers = {}
    for col in df.columns:
        # select only columns with a number dtype
        if np.issubdtype(df[col].dtype, np.number):
            # get lower and upper bounds from other function
            lower_bound, upper_bound = get_lower_and_upper_bounds(df[col], multiplier=multiplier)
            print(f' {col}: \n upper bound: {upper_bound}\n lower bound: {lower_bound}\n')
            # create a new dict value for each column in the df
            outliers[col] = {}
            # store upper and lower bounds
            outliers[col]['bounds'] = {'upper' : upper_bound, 'lower' : lower_bound}
            # save outliers that fall below the lower bound and above the upper band
            outliers[col]['outlier'] = df[(df[col] > upper_bound) |  (df[col] < lower_bound)]
        else:
            pass
    # list comprehension that prints each outlier seperated by column
    [print('\n', key, ':\n', outliers[key]['outlier']) for key in outliers]
    
def make_active(df):
    df = merge(cohorts, how = 'left', left_on = 'cohort_id', right_on = 'id')
    df = make_datetime(df, 'start_date')
    df = make_datetime(df, 'end_date')
    df = make_datetime(df, 'date', set_index = True)
    df = active_status(df, df.index, 'start_date', 'end_date')
    df['pings'] = 1
    return df.drop(columns = ['Unnamed: 0','slack','created_at','updated_at','deleted_at'])

def filter_endpoints(df):
    '''
    This function filters out the following endpoints
    /
    toc
    contains the following strings: search, jpg, jpeg, svg
    Returns the dataframe with those endpoints removed
    '''
    # step one get rid of endpoints that are only '/'
    df2 = df[df.endpoint != '/']

    # step 2 get rid of everything tat contains the following
    df_final = df2[df2.endpoint.str.contains('toc|search|jpg|jpeg|svg') == False]
    
    return df_final