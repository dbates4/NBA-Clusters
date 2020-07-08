# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:36:13 2020

@author: dylan

level: season
Variables: Offensive only

"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from cluster_functions import kmeans_func

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
# drop defense variables
data = data.drop(columns = ['mean_BLK','mean_BLK%','mean_DRB','mean_DRB%'
                            ,'mean_DRTG','mean_PF','mean_STL','mean_STL%'
                            ,'mean_TRB','mean_TRB%'])

#kmeans
best_model = kmeans_func(25, data)

data['clusters'] = best_model.predict(data)

cluster_attributes = data.groupby('clusters').agg(['mean','min','max'])
