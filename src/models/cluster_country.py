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
df_no_pop_original.to_csv("src/data/examples/clustered.csv", index=False)
