import pandas as pd
import matplotlib.pyplot as plt

fbDf = pd.read_csv('cleaned_fb.csv')

fbDf[['comments', 'likes']].plot()
plt.show()