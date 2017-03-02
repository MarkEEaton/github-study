import numpy as np
import matplotlib.pyplot as plt
import json
import matplotlib.dates as mdate
import datetime
import seaborn as sns

"""
Histogram of when the user was created
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
        update = datetime.datetime.strptime(i[group][user][facet],
                                            "%Y-%m-%dT%H:%M:%SZ")
        facet_list.append(update)
        mpl_list = mdate.date2num(facet_list)
    return np.array(mpl_list)

x1_data = make_np("created_at", "librarians")
x2_data = make_np("created_at", "randoms")

bins = np.histogram(np.hstack((x1_data, x2_data)), bins=20)[1]

sns.set(style='darkgrid')
fig, ax = plt.subplots()

# set up the x-axis by date
ax.xaxis.set_major_locator(mdate.YearLocator())
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y'))

# plot as a histogram
plt.hist([x1_data, x2_data], bins, alpha=1,
         label=['Librarians', 'Control group'], color=['k', '0.75'])

plt.legend(loc='upper left')
plt.suptitle('Date user was created')
plt.xlabel('Date the account was created')
plt.ylabel('Number of users')

plt.show()
