import numpy as np
import matplotlib.pyplot as plt
import json
import matplotlib.dates as mdate
import datetime

"""
Double-histogram of followers vs. following
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
        facet_list.append(i[group][user][facet]) 
    return np.array(facet_list)

x1_data = make_np("followers", "librarians")
x2_data = make_np("followers", "randoms")

x1_negative = np.array([-x for x in make_np("following", "librarians")])
x2_negative = np.array([-x for x in make_np("following", "randoms")])

#bins1 = np.histogram(np.hstack((x1_data, x2_data)), bins=30)[1]
#bins2 = np.histogram(np.hstack((x1_negative, x2_negative)), bins=30)[1]

print(len(x1_data))
print(len(x1_negative))

x1 = range(66)
fig1 = plt.figure()
ax1 = plt.subplot(111)
ax1.bar(x1, x1_data, width=1, color='r')
ax1.bar(x1, x1_negative, width=1, color='b')

x2 = range(29)
ax2 = plt.subplot(111)
ax2.bar(x2, x2_data, width=1, color='g')
ax2.bar(x2, x2_negative, width=1, color='y')
#fig, ax = plt.subplots()
#plt.plot(x1_data, x2_data)
#plt.plot(-x1_data, -x2_data)
#plt.hist([x1_data, x2_data], bins=30, alpha=1, label=['librarians', 'randoms'])
#plt.hist([x1_negative, x2_negative], bins=30, alpha=1, label=['librarians', 'randoms'])

#plt.legend(loc='upper left')

plt.show()
