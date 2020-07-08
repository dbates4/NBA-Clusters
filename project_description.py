# -*- coding: utf-8 -*-
"""
The goal of this project is to find if there are objective groups one can
use to classify players. Are these different player groups important in
determining team outcomes? Will these groups signify different levels of 
ability or be more associated with different roles? Fans break players
up into groups all the time, so do coaches break players into different roles.
Games like 2k give players different archetypes. Can any of these types
of groupings be found through clustering algorithms and do any of them have
objective criteria? Alternatively, if groupings are hard coded based on my 
intuition, can those groupings be linked to team performance?

Levels to look at:
    Season Averages
    Player Games

Variables:
    Standardized vs Unstandardized
    Dimensionality Reduction vs Normal Dimensions
    Box Score vs Advanced Stats

Methods to use:
    Kmeans
    Mixed
    Hierarchical
    Spectral
    
Metrics:
    AIC
    Silhouette Score

Produce a common table of best performers for each of these approaches.


OTHER IDEAS:
    take the best candidate for groups and see if it explains team performance
    Find how much each stat matters for team performance and then group on the
        most important stats
    


PROJECT SUB_GOAL:
    Use this project as an excuse to build out cluster analysis functions. As
    you work on different scripts, functionalize them so that eventually all
    you have to do is input a list of columns to a function and it will run
    all of the analysis. This project is basically doing the same thing to a 
    bunch of different datasets so it is the perfect opportunity to build this
    out as you go.



"""

