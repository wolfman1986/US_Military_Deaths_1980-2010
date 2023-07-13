import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.ticker as mticker

def file_import(filepath):
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip()
    return df


if __name__ == '__main__':
    my_df = file_import('Data/U.S. Military Deaths by cause 1980-2010.csv')
    print(my_df.head(2))

