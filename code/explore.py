import numpy as np
import pandas as pd
import math as math

  
# get list of numeric column names

def numeric_columns(df):
    return df.select_dtypes(np.number).columns.tolist()

  
    
    
# get list of categorical column names

def categorical_columns(df):
    return df.select_dtypes(['object']).columns.tolist()



# custom function to include unique values of categorical variables in the describe() funtion

def describe_categorical_variables(dataframe):
    
    # generate stat for categorical variable and clone the row index
    cat_columns = categorical_columns(dataframe)
    df_cat_stat = dataframe[cat_columns].describe().transpose()
    df_cat_stat['variable'] = df_cat_stat.axes[0].tolist() # common key to join join
    
    # generate list of unique values for each categorical variable
    row_list = []
    for i in cat_columns:
        lst_unique  = dataframe[i].unique().tolist()
        row = str().strip('[]')
        # convert all elements in the list to string of list as sometime elements can be NaN
        s = [str(j) for j in lst_unique]       
        row  = [i, ','.join(s)]
        row_list.append(row)
    cat_unique_values_df = pd.DataFrame(row_list,columns =['variable','unique values'])
    # join stat output df and unique values df
    df_final = pd.merge(cat_unique_values_df,df_cat_stat, on='variable')
    return df_final

