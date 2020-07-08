# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:44:30 2020

@author: dylan

level: season averages
Variables: Just box score stats

"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load data from season ending in 2017 ---------------
path = "C:/Users/dylan/Datasets/NBA/"
data = pd.read_csv(path+'box scores 2016 to 2017.csv', index_col=0)
# drop non-numeric columns
data.drop(['Date','Team','Game','MP'], axis=1, inplace=True)
data = data[data['Player'] != 'Team Totals']
# Replace missing values with 0
data.fillna(value=0, inplace=True)
# Collapse data to the player level
group_level = ['Player']
agg_calcs = ['mean']
data = data.groupby(group_level).agg(agg_calcs)
level0 = data.columns.get_level_values(0)
level1 = data.columns.get_level_values(1)
data.columns = level1 + '_' + level0
player_ind = data.index

#kmeans
tries = {}
for c in range(2,21):
    model = KMeans(n_clusters=c).fit(data)
    preds = model.predict(data)
    tries[c] = silhouette_score(data, preds)
tries
best_model = KMeans(n_clusters=2).fit(data)
data['clusters'] = best_model.predict(data)

cluster_attributes = data.groupby('clusters').agg(['mean','min','max'])