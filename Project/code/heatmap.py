import os
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ROOT = Path(__file__).resolve().parents[1]
PATH_DATA = os.path.join(ROOT,"data", '1_small_office_summary_1.csv')


data = pd.read_csv(PATH_DATA)
data = data.iloc[:, 5:15]
print(data.head())

cov_matrix = data.corr()  

plt.figure(figsize=(18, 15))  
sns.set(font_scale=2)
heatmap = sns.heatmap(cov_matrix, annot=True, fmt=".2f", cmap="coolwarm", xticklabels=data.columns, yticklabels=data.columns, cbar=False)
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.title("Covariance Heatmap (First 10 Features)")
plt.savefig('covariance_heatmap.png', bbox_inches='tight')
plt.show()








