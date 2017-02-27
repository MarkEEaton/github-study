import numpy as np
import matplotlib.pyplot as plt
import json
import matplotlib.dates as mdate
import datetime
import pandas as pd
import seaborn as sns

"""
Histogram grid of followers
"""

with open('json/processedlibrarians.json', 'r') as file1:
    data1 = json.load(file1)
with open('json/processedrandoms.json', 'r') as file2:
    data2 = json.load(file2)

def make_np(facet, group):
    """ extract the data """ 
    facet_list = []
    i = {"librarians": data1,
         "randoms": data2}
    for user in i[group]:
        facet_list.append(i[group][user][facet]) 
    return np.array(facet_list)

x1_data = make_np("followers", "librarians")
# this slice needs to be removed once data lengths are harmonized
x2_data = make_np("followers", "randoms")[:98]

sns.set(style='darkgrid')
bins = np.logspace(1.0, 4.0, 20)

fig, ax = plt.subplots()
plt.hist([x1_data, x2_data], bins, alpha=1, label=['librarians', 'randoms'], color=['k', '0.75'], rwidth=1)
plt.gca().set_xscale('log')
plt.legend(loc='upper right')

plt.show()