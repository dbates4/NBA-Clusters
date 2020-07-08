# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:09:10 2020

@author: dylan

Level: Season averages
Variables: Standardized, Reduced, All Stats

"""

# Do the imports --------------------
import pandas as pd
import os
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

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
# Scale so all units are standard deviations from the mean
sc = StandardScaler()
data = pd.DataFrame(sc.fit_transform(data), columns=data.columns)
data.index = player_ind
# Do the dimension reduction --------------
# Use number of components that explain 90% of variance
pca = PCA(n_components=.9).fit(data)
comp_cols = []
for i in range(pca.n_components_):
    comp_cols.append('Component '+str(i+1))
data_reduced = pd.DataFrame(pca.transform(data), columns=comp_cols, index=player_ind)
# Explore principle components for interpretation
pca_comps = {}
for i in range(pca.n_components_):
    pca_comps[i+1] = pca.components_[i]
pca_comps_table = pd.DataFrame(pca_comps, index=data.columns)

#pca_comps_table.sort_values(by=[1]) 
#All pos, higher pts/fg/fga, low +-/3pts (mid range scorer)
#pca_comps_table.sort_values(by=[2]) 
#Rebounds/blocks vs 3s
#pca_comps_table.sort_values(by=[3]) 
#Advanced metrics vs box score
#pca_comps_table.sort_values(by=[4]) 
#(ast%,tov%,ast,ftr,stl) vs (3par,3m, 3a, 3%) (pass vs 3s)
#pca_comps_table.sort_values(by=[5]) 
#(stl%,tov%,pf,3par) vs (+-,ftr,ft%) (gambles vs efficiency)
#pca_comps_table.sort_values(by=[6]) 
#(+- HUGE,stl%,) vs (ft%,ft,fta,usg,ftr) (high +- vs low +-)

# Kmeans
model = KMeans(n_clusters=5, random_state=0).fit(data)
preds = model.predict(data)
silhouette_score(data, preds)
# Mixed
# Hierarchical
# Spectral



