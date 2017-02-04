import numpy as np
import matplotlib.pyplot as plt
import json
import matplotlib.dates as mdate
import datetime
import pandas as pd
import seaborn as sns

"""
Histogram grid of followers vs. following
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

y1_data = make_np("following", "librarians")
# this slice needs to be removed once data lengths are harmonized
y2_data = make_np("following", "randoms")[:98]

d1 = [[x1_data], [y1_data]]
d2 = [[x2_data], [y2_data]]
xaxes = ['followers', 'following', 'followers', 'following']
titles = ['librarians', 'librarians', 'randoms', 'randoms']

sns.set(style='darkgrid')
f,a = plt.subplots(1,2)
a = a.ravel()
for idx, ax in enumerate(a):
    ax.hist(d1[idx], bins=70)
    ax.hist(d2[idx], bins=70)
    ax.set_title(titles[idx])
    ax.set_xlabel(xaxes[idx])
    ax.set_ylim([0, 90])
plt.tight_layout()

plt.show()
