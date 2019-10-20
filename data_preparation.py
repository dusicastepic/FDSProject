import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore') 

train_data=pd.read_csv('train.csv')
test_data=pd.read_csv('test.csv')
houses_data = train_data.append(test_data,ignore_index=True)

# =============================================================================
# Data Preparation (Data tidyng/cleaning)
# =============================================================================

def number_unique_col(df,col_name):
    return 'Number of unique values'+' for '+col_name+' :'+str(len(np.unique(df[col_name])))

'''
    Doing imputation of missing values

'''
def convert_to_categorical(df,col_names):    
    for col in col_names:
        df[col] = df[col].astype(str)
    return df

def fill_top(df,column_lst):
    for column in column_lst:
        df[column]=df[column].fillna(df[column].value_counts().index[0])
    return df

def fill_with_zero(df,column_lst):
    for column in column_lst:
        df[column]=df[column].fillna(0)
    return df

 
def fill_with_none(df,column_lst):
    for column in column_lst:
        df[column]=df[column].fillna("None")
    return df  
        
def mapping_dict(col,df):
    q_dict = {"None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5}
    df[col] = df[col].map(q_dict).astype(int)