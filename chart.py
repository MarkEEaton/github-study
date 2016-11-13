import numpy as np
import matplotlib.pyplot as plt
import json

with open('json/processedlibrarians.json', 'r') as file1:
    data1 = json.load(file1)
with open('json/processedrandoms.json', 'r') as file2:
    data2 = json.load(file2)

def make_np(x, group):
    facet = []
    i = {"librarians": data1,
         "randoms": data2}
    for user in i[group]:
        facet.append(i[group][user][x])
    print(facet)
    return np.array(facet)

x1_data = make_np("followers", "librarians")
y1_data = make_np("public_repos", "librarians")

x2_data = make_np("followers", "randoms")
y2_data = make_np("public_repos", "randoms")

plt.axis([0, 150, 0, 150])
plt.scatter(x1_data, y1_data, color = 'r')
plt.scatter(x2_data, y2_data, color = 'b')

plt.ylabel("public repos")
plt.xlabel("followers")

plt.show()
