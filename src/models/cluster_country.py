import pandas as pd
import numpy as np
import json
import hdbscan

df_pop_sep = pd.read_csv('src/data/examples/exemple_dt_1_with_pop_life.csv')

# create a dictionary to store the final data structure
data = {}

# loop through each row of the dataframe
for index, row in df_pop_sep.iterrows():
    country = row['iso_code']
    # create an inner dictionary for the country
    if country not in data:
        data[country] = {}
    # loop through each year from 2005 to 2007
    for year in range(2005, 2008):
        year_str = str(year)
        # create a nested dictionary for each year
        data[country][year] = {}
        population = row['population_' + year_str]
        data[country][year]['min'] = row[year_str + '_min'] / population
        data[country][year]['avg'] = row[year_str + '_avg'] / population
        data[country][year]['max'] = row[year_str + '_max'] / population
        data[country][year]['life_expectancy'] = row['life_expectancy_' + year_str]

# convert the final data structure to a JSON string
json_str = json.dumps(data)

# write the JSON string to a file
with open('src/data/examples/data_example.json', 'w') as f:
    f.write(json_str)
    
    # Loop through the years from 2005 to 2007
df_no_pop = pd.read_csv('src/data/examples/exemple_dt_1_with_pop_life.csv')

for year in range(2005, 2008):
    year_str = str(year)
    # Divide the min, max and avg by the population
    df_no_pop[year_str + "_min"] = df_no_pop[year_str + "_min"] / df_no_pop["population_" + year_str]
    df_no_pop[year_str + "_max"] = df_no_pop[year_str + "_max"] / df_no_pop["population_" + year_str]
    df_no_pop[year_str + "_avg"] = df_no_pop[year_str + "_avg"] / df_no_pop["population_" + year_str]
    df_no_pop.drop("population_" + year_str, axis=1, inplace=True)

# Save the updated dataframe to a new csv file
df_no_pop.to_csv("src/data/examples/for_clustering.csv", index=False)

import hdbscan

clusterer = hdbscan.HDBSCAN()

df_no_pop_original = df_no_pop.copy()

df_no_pop.drop("iso_code", axis=1, inplace=True)
df_no_pop.drop("country", axis=1, inplace=True)
clusterer.fit(df_no_pop)
print(clusterer.labels_)
df_no_pop_original['cluster'] = clusterer.labels_
df_no_pop_original.to_csv("src/data/examples/clustered_hdbscan.csv", index=False)


from minisom import MiniSom

# Initialization and training
som_shape = (1, 3)
som = MiniSom(som_shape[0], som_shape[1], len(df_no_pop.columns), sigma=.5, learning_rate=.5,
              neighborhood_function='gaussian')

data = df_no_pop.to_numpy()

som.train_batch(data, 500, verbose=True)

# each neuron represents a cluster
winner_coordinates = np.array([som.winner(x) for x in data]).T
# with np.ravel_multi_index we convert the bidimensional
# coordinates to a monodimensional index
cluster_index = np.ravel_multi_index(winner_coordinates, som_shape)

df_no_pop_original['cluster'] = cluster_index
df_no_pop_original.to_csv("src/data/examples/clustered_som.csv", index=False)

print(cluster_index)

import matplotlib.pyplot as plt

# plotting the clusters using the first 2 dimentions of the data
for c in np.unique(cluster_index):
    plt.scatter(data[cluster_index == c, 0],
                data[cluster_index == c, 1], label='cluster='+str(c), alpha=.7)

# plotting centroids
for centroid in som.get_weights():
    plt.scatter(centroid[:, 0], centroid[:, 1], marker='x', 
                s=80, linewidths=35, color='k', label='centroid')
plt.legend()
plt.show()