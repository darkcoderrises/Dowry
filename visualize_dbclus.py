from sklearn.cluster import KMeans
import numpy as np
from sklearn.manifold import TSNE
from sklearn.preprocessing import normalize
from scipy.spatial.distance import pdist, squareform
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN


f_orig = np.asarray([filter(bool, i.split(' ')) for i in filter(bool, open('essay-y').read().split('\n'))])
f_orig = normalize(f_orig, axis=1)
f = pdist(f_orig, 'euclidean')
f = squareform(f)

X = StandardScaler().fit_transform(f)
db = DBSCAN(eps=30, min_samples=1).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True

labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print n_clusters_

for i in range(n_clusters_):
    vals = np.where(labels==i)[0]
    print "=======================\n", i, vals[:5], len(vals)

#for i in range(n_clusters_):
#    for j in range(i+1, n_clusters_):
#        print i, j, 
#        print np.linalg.norm(kmeans.cluster_centers_[i]-kmeans.cluster_centers_[j])


model = TSNE(n_components=2, random_state=0, metric='precomputed')
coords = model.fit_transform(f)

color = np.asarray(['red', 'green', 'blue', 'black', 'purple', 'yellow'])
plt.scatter(coords[:, 0], coords[:, 1], color=color[labels])
plt.show()
