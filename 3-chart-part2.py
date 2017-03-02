import matplotlib.pyplot as plt
import numpy as np
import json
import seaborn as sns

"""
A bar chart of what programming languages are used
"""

with open('json/processedlanguages.json', 'r') as f:
    data = json.load(f)

ldata = data['randoms']
ldata = {k: v for k, v in ldata.items() if k != 'null'}
ldata = sorted(ldata.items(), key=lambda x: -x[1])
ldata = list(zip(*ldata))

xdata = ldata[0][:15]
ydata = ldata[1][:15]

sns.set(style='darkgrid')

plt.xticks(np.arange(len(xdata)), xdata, rotation=90)
plt.bar(np.arange(len(xdata)), ydata, align='center', color='0.75')

plt.ylabel('Number of repositories')
plt.xlabel('Language')
plt.suptitle('Language choice among control group')

plt.show()
