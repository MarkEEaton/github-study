import matplotlib.pyplot as plt
import numpy as np
import json
import seaborn as sns
import pprint

"""
A bar chart of what programming languages are used
"""

with open('json/processedlanguages.json', 'r') as f:
    data = json.load(f)

ldata = data['librarians']
xdata, ydata = ldata.keys(), ldata.values()

sns.set(style='darkgrid')

plt.xticks(np.arange(len(xdata)), xdata, rotation=90)
plt.bar(np.arange(len(xdata)), ydata)

plt.show()
