import pandas as pd
import numpy as np
import io
import pandas_profiling
retail_raw = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

print('Korelasi quantity dengan item_price')
print(retail_raw[['quantity', 'item_price']].corr())