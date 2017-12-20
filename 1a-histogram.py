import numpy as np
import matplotlib.pyplot as plt
import json
import matplotlib.dates as mdate
import datetime
import seaborn as sns
import arrow
from scipy import stats

"""
Histogram of when the user had their last update
"""

with open('json/processedlibrarians.json', 'r') as file1:
    data1 = json.load(file1)
with open('json/processedrandoms.json', 'r') as file2:
    data2 = json.load(file2)


def make_np(facet, group):
    """ make the datasets as numpy arrays"""
    facet_list = []
    i = {'librarians': data1,
         'randoms': data2}
    for user in i[group]:
        update = datetime.datetime.strptime(i[group][user][facet],
                                            '%Y-%m-%dT%H:%M:%SZ')
        facet_list.append(update)
    mpl_list = mdate.date2num(facet_list)
    return np.array(mpl_list)


x1_data = make_np('updated_at', 'librarians')
x2_data = make_np('updated_at', 'randoms')


def get_avg_dates():
    """ get the average timedeltas for both populations """

    avg_librarians = np.around(np.mean(x1_data))
    avg_randoms = np.around(np.mean(x2_data))

    avg_librarians_date = mdate.num2date(avg_librarians)
    avg_randoms_date = mdate.num2date(avg_randoms)

    created_date = arrow.get(datetime.datetime(2017, 3, 1), 'US/Eastern')

    librarians_delta = created_date - avg_librarians_date
    randoms_delta = created_date - avg_randoms_date

    return(librarians_delta.days, randoms_delta.days)


print('updated-at t-test: ')
print(stats.ttest_ind(x1_data, x2_data, equal_var=False))

avg_dates = get_avg_dates()

bins = np.histogram(np.hstack((x1_data, x2_data)), bins=20)[1]

sns.set(style='darkgrid')
fig, ax = plt.subplots()

# set up the x-axis by date
ax.xaxis.set_major_locator(mdate.MonthLocator())
ax.xaxis.set_major_formatter(mdate.DateFormatter('%b'))

# plot as a histogram
plt.hist([x1_data, x2_data], bins, alpha=1,
         label=['Librarians', 'Comparison group'], color=['k', '0.75'])
plt.text(datetime.date(2016, 12, 7), 25.55,
         'Average days since last update for librarians: ' + str(avg_dates[0]),
         ha='left', size=10)
plt.text(datetime.date(2016, 12, 7), 24.3,
         'Average days since last update for comparison group: '
         + str(avg_dates[1]), ha='left', size=10)

plt.legend(loc='upper left')
plt.suptitle('Date of last update')
plt.xlabel('Date')
plt.ylabel('Number of users')

plt.show()
