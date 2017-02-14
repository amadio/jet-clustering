#!/usr/bin/env python

import sys
import math
import pandas
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

params = plt.rcParams['axes.prop_cycle']
colors = params.by_key()['color']

def make_plot(name, data):
	fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(7,4), sharey=True)
	axes[0].set_title('Real classification')

	clusters = data.jet.unique()
	model = KMeans(init='k-means++', n_clusters=len(clusters))
	model.fit_predict(data[['px','py','pz']].as_matrix())
	data['KMeans'] = model.labels_

	for c in clusters:
		data[data.jet == c].plot.scatter(x='eta', y='phi', color=colors[c], ax=axes[0])

	axes[1].set_title('KMeans with %d clusters' % (clusters))

	for c in data.Kmeans.unique():
		data[data.KMeans == c].plot.scatter(x='eta', y='phi', color=colors[c], ax=axes[1])

	plt.tight_layout()
	plt.savefig(name)

if __name__ == "__main__":
    data = pandas.read_csv(sys.argv[1])
	name = sys.argv[1].replace('.csv','.pdf'))
	make_plot(name, data)
