import matplotlib
matplotlib.use('pdf')

from sklearn.cluster import KMeans
import numpy as np
from sklearn.manifold import TSNE
from sklearn.preprocessing import normalize
from scipy.spatial.distance import pdist, squareform
from matplotlib import pyplot as plt

f_orig = np.asarray([filter(bool, i.split(' ')) for i in filter(bool, open('essay-y').read().split('\n'))])
f_orig = normalize(f_orig, axis=1)
f = pdist(f_orig, 'euclidean')
f = squareform(f)

nos=6
kmeans = KMeans(n_clusters=nos, random_state=0).fit(f_orig)
for i in range(nos):
    val = np.where(kmeans.labels_==i)[0]
    print "=======================\n", i, val[:5], len(val)

#for i in range(nos):
#    for j in range(i+1, nos):
#        print i, j, 
#        print np.linalg.norm(kmeans.cluster_centers_[i]-kmeans.cluster_centers_[j])


model = TSNE(n_components=2, random_state=0, metric='precomputed')
coords = model.fit_transform(f)

color = np.asarray(['red', 'green', 'blue', 'black', 'purple', 'yellow'])

f = plt.figure()
plt.scatter(coords[:, 0], coords[:, 1], color=color[kmeans.labels_])
f.savefig("foo.pdf")
