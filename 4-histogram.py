import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sns

"""
Histogram of gh-index
"""

# get the data from file
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

x1_data = make_np("gh-index", "librarians")
x2_data = make_np("gh-index", "randoms")

avg_librarians = np.around(np.mean(x1_data), decimals=1)
avg_randoms = np.around(np.mean(x2_data), decimals=1)

# create the bins
bins = np.arange(11)-0.5

sns.set(style='darkgrid')

# create the histogram
fig, ax = plt.subplots()
plt.hist([x1_data, x2_data], bins, alpha=1,
         label=['Librarians', 'Control group'], color=['k', '0.75'],
         rwidth=0.75)
plt.text(7, 66.6, 'Average gh-index for librarians: ' +
         str(avg_librarians), ha='right', size=10)
plt.text(7, 63.3, 'Average gh-index for control group: ' +
         str(avg_randoms), ha='right', size=10)
plt.xlim(-0.5, 9.5)
plt.xticks(range(10))

plt.legend(loc='upper right')
plt.suptitle('Distribution of gh-index')
plt.xlabel('gh-index')
plt.ylabel('Number of users')

plt.show()
