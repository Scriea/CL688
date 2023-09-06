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
data_hmap = data.iloc[:, 5:15]
print(data.columns)

cor_matrix = data_hmap.corr()  

plt.figure(figsize=(18, 15))  
sns.set(font_scale=2)
heatmap = sns.heatmap(cor_matrix, annot=True, fmt=".2f", cmap="coolwarm", xticklabels=data_hmap.columns, yticklabels=data_hmap.columns, cbar=False)
#heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.xticks([])
plt.title("Covariance Heatmap (First 10 Features)")
plt.savefig('covariance_heatmap.png')
# plt.show()

print()
thermal_load_data = data[data.columns[-2]].iloc[0:2400]
#data[data.columns[2]] = pd.to_datetime(data[data.columns[2]])
date_column = data[data.columns[0]].iloc[0:2400] 
print(date_column)

# Create a line plot
plt.figure(figsize=(20, 12))  # Adjust the figure size as needed
plt.plot(date_column, thermal_load_data, marker='o', linestyle='-')
plt.title('Thermal Load Over Time (For 100 Days)')
plt.xlabel('Date')
plt.ylabel('Thermal Load')
plt.grid(True)

# Rotate x-axis labels for better readability (if necessary)
plt.xticks([])

# Show the plot
plt.tight_layout()
plt.savefig('linechart.png')
# plt.show()








