import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sns
from scipy import stats

"""
A scatterplot with number of public repos and number of following.
"""

with open('json/processedlibrarians.json', 'r') as file1:
    data1 = json.load(file1)
with open('json/processedrandoms.json', 'r') as file2:
    data2 = json.load(file2)


def make_np(facet, group):
    """ make the datasets as numpy arrays """
    facet_list = []
    i = {"librarians": data1,
         "randoms": data2}
    for user in i[group]:
        facet_list.append(i[group][user][facet])
    return np.array(facet_list)

# get the scatterplot data for librarians ready
x1_data = make_np("following", "librarians") + 1
y1_data = make_np("public_repos", "librarians") + 1

# calculate the mean for librarians
x1_avg = np.mean(x1_data)
y1_avg = np.mean(y1_data)

# get the scatterplot data for randoms ready
x2_data = make_np("following", "randoms") + 1
y2_data = make_np("public_repos", "randoms") + 1

# calculate the mean for randoms
x2_avg = np.mean(x2_data)
y2_avg = np.mean(y2_data)

# do log transformations and run t-test
x1_data_log = np.log10(x1_data)
x2_data_log = np.log10(x2_data)
y1_data_log = np.log10(y1_data)
y2_data_log = np.log10(y2_data)

print('following t-test: ')
print(stats.ttest_ind(x1_data_log, x2_data_log, equal_var=False))
print('public repos t-test: ')
print(stats.ttest_ind(y1_data_log, y2_data_log, equal_var=False))

sns.set(style='darkgrid')

# make four plots
plt.scatter(x1_data, y1_data, color='k', s=50)
plt.scatter(x2_data, y2_data, facecolor='1', edgecolor='0', s=50)
plt.scatter(x1_avg, y1_avg, marker='*', facecolor='k',
            edgecolor='w', linewidth=1, s=200)
plt.scatter(x2_avg, y2_avg, marker='*', facecolor='w',
            edgecolor='k', linewidth=1, s=200)

# log scale makes the data more readable
plt.xscale('log')
plt.yscale('log')

# mark the boundaries of the plot
plt.xlim(1, 10000)
plt.ylim(1, 10000)

plt.ylabel("Public repos")
plt.xlabel("Following")
plt.legend(('Librarians', 'Comparison group', 'Librarian average',
            'Comparison group average'), loc='upper right')
plt.suptitle('Activity')

plt.show()
