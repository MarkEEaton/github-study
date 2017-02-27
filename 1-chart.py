import numpy as np
import matplotlib.pyplot as plt
import json

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

x1_data = make_np("followers", "librarians")
y1_data = make_np("public_repos", "librarians")

x2_data = make_np("followers", "randoms")
y2_data = make_np("public_repos", "randoms")

plt.axis([-2, 150, -2, 150])
plt.scatter(x1_data, y1_data, alpha=1, color='k')
plt.scatter(x2_data, y2_data, alpha=0.25, color='k')

plt.ylabel("public repos")
plt.xlabel("followers")
plt.legend(('Librarians', 'Randoms'), loc='upper right')
plt.suptitle('Activity measured by public repos and followers')

plt.show()
