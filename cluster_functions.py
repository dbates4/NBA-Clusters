# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:52:12 2020

@author: dylan
"""

def maxvalkey(d): 
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def kmeans_func(n_clusters, data):
    ''' Applies sklearn.cluster.kmeans algorithm to dataset 'data' for 
        all cluster numbers from 2 to n_clusters '''
    
    # Test for required moduls and import    
    if 'KMeans' not in globals():
        from sklearn.cluster import KMeans
    if 'silhouette_score' not in globals():
        from sklearn.metrics import silhouette_score
    
    # Fit model using different numbers of clusters
    # Store restults
    tries = {}
    for i in range(2, n_clusters+1):
        model = KMeans(n_clusters=i).fit(data)
        preds = model.predict(data)
        tries[i] = silhouette_score(data, preds)
    
    # Find best model
    best_cluster = maxvalkey(tries)
    best_model = KMeans(n_clusters=best_cluster).fit(data)

    return(best_model)