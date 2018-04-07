import matplotlib.pyplot as plt
import numpy as np
import json
import seaborn as sns

"""
A bar chart of what programming languages are used
"""

# get the data from file
with open('json/processedlanguages.json', 'r') as f:
    data = json.load(f)

# transform the data into sorted lists
ldata = data['randoms']
ldata = {k: v for k, v in ldata.items() if k != 'null'}
ldata = sorted(ldata.items(), key=lambda x: -x[1])
ldata = list(zip(*ldata))

# take the top 15 programming languages
xdata = ldata[0][:15]
ydata = ldata[1][:15]

sns.set(style='darkgrid')

# assign the labels and make the bar chart
plt.xticks(np.arange(len(xdata)), xdata, rotation=90)
plt.bar(np.arange(len(xdata)), ydata, align='center', color='0.75')

plt.ylabel('Number of repositories')
plt.suptitle('Language choice among comparison group')

plt.show()
