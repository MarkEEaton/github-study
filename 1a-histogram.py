import numpy as np
import matplotlib.pyplot as plt
import json
import matplotlib.dates as mdate
import datetime

"""
Histogram of when the user had their last update
"""

with open('json/processedlibrarians.json', 'r') as file1:
    data1 = json.load(file1)
with open('json/processedrandoms.json', 'r') as file2:
    data2 = json.load(file2)


def make_np(facet, group):
    facet_list = []
    i = {"librarians": data1,
         "randoms": data2}
    for user in i[group]:
        update = datetime.datetime.strptime(i[group][user][facet],
                                            "%Y-%m-%dT%H:%M:%SZ")
        facet_list.append(update)
        mpl_list = mdate.date2num(facet_list)
    return np.array(mpl_list)

x1_data = make_np("updated_at", "librarians")
x2_data = make_np("updated_at", "randoms")

bins = np.histogram(np.hstack((x1_data, x2_data)), bins=20)[1]

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(mdate.MonthLocator())
ax.xaxis.set_major_formatter(mdate.DateFormatter('%b'))
plt.hist([x1_data, x2_data], bins, alpha=1, label=['librarians', 'randoms'], color=['k', '0.75'])
#plt.hist(x2_data, bins, alpha=0.5, label='randoms')
plt.legend(loc='upper left')
plt.suptitle('Date of last update')

plt.show()
