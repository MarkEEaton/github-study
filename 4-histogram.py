import numpy as np
import matplotlib.pyplot as plt
import json
import decimal
import seaborn as sns
from scipy import stats

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

print('gh-index t-test: ')
print(stats.ttest_ind(x1_data, x2_data, equal_var=False))

two_places = decimal.Decimal(10) ** -2
avg_librarians = decimal.Decimal(np.mean(x1_data)).quantize(two_places)
avg_randoms = decimal.Decimal(np.mean(x2_data)).quantize(two_places)

# create the bins
bins = np.arange(11)-0.5

sns.set(style='darkgrid')

# create the histogram
fig, ax = plt.subplots()
plt.hist([x1_data, x2_data], bins, alpha=1,
         label=['Librarians', 'Comparison group'], color=['k', '0.75'],
         rwidth=0.75)
plt.text(6.5, 66.6, 'Average GH index for librarians: ' +
         str(avg_librarians), ha='right', size=10)
plt.text(6.5, 63.3, 'Average GH index for comparison group: ' +
         str(avg_randoms), ha='right', size=10)
plt.xlim(-0.5, 9.5)
plt.xticks(range(10))

plt.legend(loc='upper right')
plt.suptitle('Distribution of GH index')
plt.xlabel('GH index')
plt.ylabel('Number of users')

plt.show()
