
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

def make_datetime(df, col_name):
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