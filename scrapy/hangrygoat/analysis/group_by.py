import numpy as np
import pandas as pd



def group_by(df, *args):
    if args:
        return df.groupby(args)
    else:
        return df.groupby(df.index)
    
    

if __name__ == '__main__':
    example_df = pd.DataFrame({'a': [1,1,2,2], 'b': [5,6,7,8], 'c': [1,3,5,7]})
    grouped_df = group_by(example_df, 'a', 'b')
    for key, value in grouped_df:
        print key
    grouped_df = group_by(example_df)
    for key, value in grouped_df:
        print key