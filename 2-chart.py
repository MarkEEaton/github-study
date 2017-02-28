import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sns

with open('json/processedlibrarians.json', 'r') as file1:
    data1 = json.load(file1)
with open('json/processedrandoms.json', 'r') as file2:
    data2 = json.load(file2)

def make_np(facet, group):
    facet_list = []
    i = {'librarians': data1,
         'randoms': data2}
    for user in i[group]:
        facet_list.append(i[group][user][facet])
    return np.array(facet_list)

x1_data = make_np('followers', 'librarians')
y1_data = make_np('stargazers', 'librarians')

x2_data = make_np('followers', 'randoms')
y2_data = make_np('stargazers', 'randoms')

sns.set(style='darkgrid')
plt.axis([-2, 120, -2, 170])
plt.scatter(x1_data, y1_data, color='k', alpha=1, s=50)
plt.scatter(x2_data, y2_data, facecolor='1', edgecolor='0', s=50)

plt.ylabel('Stars')
plt.xlabel('Followers')
plt.suptitle('Popularity')
plt.legend(('Librarians', 'Randoms'), loc='upper right')

plt.show()
