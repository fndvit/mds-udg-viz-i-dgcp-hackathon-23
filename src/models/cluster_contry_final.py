import pandas as pd
import numpy as np
import json
import hdbscan
import os
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


df = pd.read_csv('src/data/flatten_data.csv')

df_columns = df.columns.tolist()
df_columns.remove('country')

# detect outliers in the remaining columns
df = df[(np.abs(stats.zscore(df[df_columns])) < 3).all(axis=1)]

df_original = df.copy()

df.drop(columns='country', inplace=True)

data = df.to_numpy()

from minisom import MiniSom

# Initialization and training
som_shape = (15, 4)
som = MiniSom(som_shape[0], som_shape[1], len(df.columns), sigma=.5, learning_rate=.5,
              neighborhood_function='gaussian')

som.train_batch(data, 500, verbose=True)

# each neuron represents a cluster
winner_coordinates = np.array([som.winner(x) for x in data]).T
# with np.ravel_multi_index we convert the bidimensional
# coordinates to a monodimensional index
cluster_index = np.ravel_multi_index(winner_coordinates, som_shape)

df_original['cluster'] = cluster_index

df_original.to_csv('src/data/country_cluster_som.csv', index = False)