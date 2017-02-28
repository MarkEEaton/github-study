import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sns

"""
A scatterplot with number of public repos and number of followers.
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

x1_data = make_np("following", "librarians")
y1_data = make_np("public_repos", "librarians")

x1_avg = np.mean(np.ma.masked_greater(x1_data, 300))
y1_avg = np.mean(np.ma.masked_greater(y1_data, 300))

x2_data = make_np("following", "randoms")
y2_data = make_np("public_repos", "randoms")

x2_avg = np.mean(np.ma.masked_greater(x2_data, 300))
y2_avg = np.mean(np.ma.masked_greater(y2_data, 300))

sns.set(style='darkgrid')
plt.axis([-5, 300, -5, 300])
plt.scatter(x1_data, y1_data, color='k', s=50)
plt.scatter(x2_data, y2_data, facecolor='1', edgecolor='0', s=50)
plt.scatter(x1_avg, y1_avg, marker='*', facecolor='k', 
            edgecolor='w', linewidth=1, s=200)
plt.scatter(x2_avg, y2_avg, marker='*', facecolor='w', 
            edgecolor='k', linewidth=1, s=200)

plt.ylabel("Public repos")
plt.xlabel("Following")
plt.legend(('Librarians', 'Randoms'), loc='upper right')
plt.suptitle('Activity')

plt.show()
