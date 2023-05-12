import streamlit as st
import src.config
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import pickle
import plotly.express as px
import os
import subprocess


from sklearn import preprocessing, pipeline, compose
from sklearn import linear_model, model_selection, svm
from sklearn import metrics
from sklearn.cluster import KMeans, DBSCAN, OPTICS, AgglomerativeClustering
from sklearn.metrics import silhouette_score,calinski_harabasz_score,davies_bouldin_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import GridSearchCV

st.set_option('deprecation.showPyplotGlobalUse', False)



# st.write( subprocess.run(['ls', '-a'], stdout=subprocess.PIPE).stdout.decode())
pkey = 'quadkey'
geometry = 'geometry'
id_and_names = ['DAUID', 'CDUID', 'CDNAME', 'CCSUID', 'CSDNAME', 'CMAUID', 'CMAPUID', 'CMANAME', 
'CCSNAME', 'CSDUID', 'ERUID', 'ERNAME', 'CTUID', 'CTNAME', 'ADAUID', 
'PCUID', 'PCNAME', 'PCPUID', 'SACCODE',] ##SACCODE is half a category half ID values

categorical_labels = [
    #'PRUID', #PRUID is redundant with PRNAME
    'PRNAME', 'CDTYPE', 
    'CSDTYPE',  
    'SACTYPE', 
    'CMATYPE', 'PCTYPE', 'PCCLASS',
]
numerical_vars = [
    'tests', 'devices',
    'das_area', 'tile_area', 'tile_frac',  'das_frac', 
    'DAPOP','POP_DENSITY'
]
target_vars = ['avg_d_kbps', 'avg_u_kbps']

# Load data placed in "notebooks/" as generated by Clustering.ipynb and Population-wise_Analysis.ipynb. 
features_table = pd.read_pickle(r'notebooks/data.pickle')
cluster_features = ['CDTYPE', 'CSDTYPE']
cluster_data = features_table[cluster_features + target_vars]
# cluster_data = cluster_data.sample(n=10000)  # fit using a random subset of data to save time



st.markdown("# Clustering Data")

st.markdown("""
## Motivation 
Earlier analysis had performed regression analysis to identify correlations between the various features in the data and the target variables viz. download speeds and upload speeds. One of the features in the data was the type of census division or subdivision that an area belongs to. However, the regression analysis was not very interpretable and did not help to identify census division types that need attention. Hence, we perform clustering to find out such division types that should be the focus of future policies. 
""")

st.markdown("### Choosing a k-value for K-means Clustering")
colTransformer = compose.ColumnTransformer(
    [(f"{cat}",preprocessing.OneHotEncoder(),[cat]) for cat in set(categorical_labels) & set(cluster_features)] \
    + [(f"{num}", preprocessing.StandardScaler(), [num]) for num in set(numerical_vars) & set(cluster_features)] 
    #+ [(f"{y}_stdscaler", preprocessing.StandardScaler(), [y]) for y in target_vars]
)

sse = {}
for k in range(1, 9):
    clustering = KMeans(n_clusters=k)


    clustering_pipe = pipeline.Pipeline([
        ('preprocess',colTransformer),
        ('clustering', clustering)
    ])
    clustering_pipe.fit(cluster_data)

    sse[k] = clustering.inertia_

    # plot SSE vs. k with elbow point
plt.figure()
plt.plot(list(sse.keys()), list(sse.values()))
plt.xlabel('Number of clusters, k')
plt.ylabel('SSE')
plt.vlines(5, ymin=min(sse.values()), ymax=max(sse.values()), linestyle='--') 
st.pyplot()

st.markdown('We see that there is a roughly linear decrease in the SSE and no clear elbow is seen. Let us choose to use 5 as the best k for K-Means clustering. ')


st.markdown('### Clustering results')

np.random.seed(7)
clustering = KMeans(n_clusters=5)

colTransformer = compose.ColumnTransformer(
    [(f"{cat}",preprocessing.OneHotEncoder(),[cat]) for cat in set(categorical_labels) & set(cluster_features)] \
    + [(f"{num}", preprocessing.StandardScaler(), [num]) for num in set(numerical_vars) & set(cluster_features)] 
    #+ [(f"{y}_stdscaler", preprocessing.StandardScaler(), [y]) for y in target_vars]
)
clustering_pipe = pipeline.Pipeline([
    ('preprocess',colTransformer),
    ('clustering', clustering)
])

clustering_pipe.fit(cluster_data)

labels = clustering.labels_

cluster_data['kmeans_cluster_label'] = labels


def scatter_3d(df, x:str='CDTYPE', y:str='CSDTYPE', z:str='avg_d_kbps', color:str='kmeans_cluster_label'):
    fig = px.scatter_3d(df, x=x, y=y, z=z, color=color, color_continuous_scale=px.colors.sequential.Viridis)
    fig.update_layout(
        autosize=False,
        width=1000,
        height=700,
        plot_bgcolor='rgb(30, 30, 40)',
        paper_bgcolor='rgb(30, 30, 40)'
    )
    st.plotly_chart(fig)


scatter_3d(cluster_data.sample(n=int(0.5*len(cluster_data))), x='CDTYPE', y='CSDTYPE', z='avg_d_kbps', color='kmeans_cluster_label')


st.markdown("""
#### Interpretations

- The orange cluster represents a large number of areas all have weak connectivity. This cluster should likely receive the most attention for policy direction.

- Census subdivisions of Self-government, Nisga'a land, Settlements, Municipality of Canton Unis have weak connectivity and should be a focus of future work. 

- There is a huge variation in all CD types. This indicates that no matter what type of area we consider (such as rural/urban areas) there are both areas with high speeds and low speeds. We confirm the findings of regression analysis that area type is not a very good indicator of internet connectivity.  

- We can naturally divide the data points into two layers at the cutoff point 400k kbps. Areas below this can be given special attention. 


""")


def threshold_data(threshold=400000):
    np.random.seed(111)
    cluster_data['cluster'] = cluster_data.loc[:, 'kmeans_cluster_label']
    cluster_data.loc[cluster_data['avg_d_kbps'] < threshold, 'cluster'] = 5
    scatter_3d(cluster_data.sample(n=int(0.4*len(cluster_data))), x='CDTYPE', y='CSDTYPE', z='avg_d_kbps', color='cluster')
    
    
threshold = st.slider("Select Threshold",  100000, 800000, 400000, 50000 )    
threshold_data(int(threshold))

st.markdown("""" We can collect all areas in the new (yellow) cluster and focus on them for future infrastructure development. 





Note: We also experimented with other clustering algorithms such as hierarchical clustering, DBSCAN, and OPTICS. However, their results have been omitted as K-means provided the most interpretable results""")