import numpy as np
import matplotlib.pyplot as plt
import json

with open('json/processeddata.json', 'r') as file:
    data = json.load(file)

def make_np(x):
    facet = []
    for user in data:
        facet.append(data[user][x])
    return np.array(facet)

x1_data = make_np("followers")
y1_data = make_np("public_repos")

x2_data = make_np("following")
y2_data = make_np("public_gists")

plt.scatter(x1_data, y1_data, color = 'r')
plt.scatter(x2_data, y2_data, color = 'b')
plt.show()

