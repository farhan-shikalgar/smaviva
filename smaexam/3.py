import pandas as pd
import numpy as np

fbDf = pd.read_csv('fb.csv')
fbDf['text'].replace('', np.nan, inplace=True)
print(fbDf)
fbDf.dropna(subset=['text'], inplace=True)
print(fbDf)
fbDf.to_csv('cleaned_fb.csv')