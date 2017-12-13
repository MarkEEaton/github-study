import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sns

"""
Histogram of number of followers
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

x1_data = make_np("followers", "librarians")
x2_data = make_np("followers", "randoms")

"""
Add one to all values because 0 can't display on a log scale.
This is important because showing zero values is more important in this
case than the exact precision of the values. The binning used makes the 
exact values in the chart indechipherable anyway.
"""
x1_data += 1
x2_data += 1

sns.set(style='darkgrid')

# make the bins logarithmic
bins = np.logspace(0.0, 4.0, 20)

# plot the histogram
fig, ax = plt.subplots()
plt.hist([x1_data, x2_data], bins, alpha=1,
         label=['Librarians', 'Comparison group'], color=['k', '0.75'],
         rwidth=1)

# make the scale logarithmic
plt.gca().set_xscale('log')

plt.legend(loc='upper right')
plt.suptitle('Followers')
plt.xlabel('Followers')
plt.ylabel('Number of users')

plt.show()
