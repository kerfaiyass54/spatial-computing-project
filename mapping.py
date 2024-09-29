import os
import pandas as pd
import numpy as np 
from joblib import dump, load
import six
# Clustering
from sklearn.cluster import DBSCAN, OPTICS, cluster_optics_dbscan
from sklearn.preprocessing import normalize, StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn import metrics
import sklearn.utils
import matplotlib
from matplotlib import gridspec
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches 
from PIL import Image
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy import config
from cartopy.io import shapereader
import cartopy.io.img_tiles as cimgt
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from urllib.request import urlopen, Request

def new_get_image(self, tile):
    url = self._image_url(tile)  # added by H.C. Winsemius
    req = Request(url) # added by H.C. Winsemius
    req.add_header('User-agent', 'your bot 0.1')
    # fh = urlopen(url)  # removed by H.C. Winsemius
    fh = urlopen(req)
    im_data = six.BytesIO(fh.read())
    fh.close()
    img = Image.open(im_data)

    img = img.convert(self.desired_tile_form)

    return img, self.tileextent(tile), 'lower'



# loading the file
geotag_df = pd.read_csv('CSV/dirty.csv')
geotag_df.set_index('photo_id', inplace=True)
print ("Shape of the DataFrame: ", geotag_df.shape)

owner_list = geotag_df.owner_nsid.unique()
owner_df = pd.DataFrame({'owner_nsid': owner_list})

geotag_test = geotag_df.sample(13,replace=True)
owner_test = owner_df.sample(13,replace=True)


# defining the maps border
lower_longitude = 7.87765
lower_latitude = 32.92967
upper_longitude = 11.21965
upper_latitude = 37.27442

extent = [lower_longitude, upper_longitude, lower_latitude, upper_latitude]

# Filtering data based on the coordinate
geotag_df = geotag_df.loc[(geotag_df['location_longitude'] > lower_longitude) &
                          (geotag_df['location_longitude'] < upper_longitude) &
                          (geotag_df['location_latitude'] > lower_latitude) &
                          (geotag_df['location_latitude'] < upper_latitude)]
print ("Shape of the DataFrame: ", geotag_df.shape)
geotag_df.head()


i = 0
total_user = len(owner_test.index)
#plt.ioff()

for index, row in owner_test.iterrows():
	cimgt.GoogleWTS.get_image = new_get_image
	request = cimgt.GoogleTiles()

	fig = plt.figure(figsize=(18,12))
	mymap = plt.axes(projection=ccrs.PlateCarree())
	mymap.set_extent(extent)
	mymap.add_image(request, 10)
	
	plot_df = geotag_df.loc[geotag_df['owner_nsid'] == row.owner_nsid]

	total_nodes = len(geotag_df.index)
	for index,row in plot_df.iterrows():
		mymap.plot(row.location_longitude, row.location_latitude, markerfacecolor = 'blue', markeredgecolor = 'yellow', marker = 's', markersize = 10, alpha = 0.6)
	plt.title("Photo map of user: {0}" .format(row.owner_nsid), fontsize=14)
	#plt.savefig("/content/drive/My Drive/Colab Notebooks/FlickrCrawling/Maps/User Photomap/{0}.png" .format(row.owner_nsid), dpi=300)
	plt.close(fig)
	i += 1
	if i % 50 == 0:
		print('{0} / {1} user photo map created.' .format(i, total_user))
    
print('Total of {0} user photo map created.' .format(i))


cimgt.GoogleWTS.get_image = new_get_image
request = cimgt.GoogleTiles()

fig = plt.figure(figsize=(16, 16))
mymap = plt.axes(projection=ccrs.PlateCarree())
mymap.set_extent(extent)
mymap.add_image(request, 10)

i = 0
total_nodes = len(geotag_df.index)
for index,row in geotag_df.iterrows():
    mymap.plot(row.location_longitude, row.location_latitude, markerfacecolor = 'red', marker = '.', markersize = 50, alpha = 0.4)
    i += 1
    if i % 5000 == 0:
        print('{0} / {1} nodes plotted to the map.' .format(i, total_nodes))
print('Total of {0} nodes has been plotted to the map.' .format(i))

plt.title("Flickr Geotagged Photo Distribution in Tunisia\nData from 2017 - 2023", fontsize=14)
plt.savefig("IMG/points.jpg",dpi=800)
#plt.show()

# Taking longitude and latitude data from the geotag_df
geotag_clus = geotag_df[['location_longitude', 'location_latitude']]
print ("Shape of the DataFrame: ", geotag_clus.shape)
print(geotag_clus.head())

# standardize the feature
geotag_clus_scaled = StandardScaler().fit_transform(geotag_clus)
pd.set_option('display.precision', 8)
geotag_clus_scaled = pd.DataFrame(data=geotag_clus_scaled, columns=['location_longitude', 'location_latitude'])
print(geotag_clus_scaled.head())

optics_result = []
i = 0
min_samples = [10, 12]
xi = [0.5, 0.1]
min_cluster_size = [0.01, 0.5, 0.1]

for x in min_samples:
	for y in xi:
		for z in min_cluster_size:
			optics_model = OPTICS(min_samples=x, xi=y, min_cluster_size=z)

			optics_model.fit(geotag_clus_scaled)
			labels = optics_model.labels_
			if len(set(labels)) < 2:
				n_noise_ = 'Invalid model: Cluster < 2'
				silhouette_score = 'Invalid model: Cluster < 2'
				n_clusters_ = 'Invalid model: Cluster < 2'
				print('Error when trying with the following parameter: min_samples={0}, xi={1}, min_cluster_size={2}' .format(x, y, z))
				break
			else:
				n_noise_ = list(labels).count(-1)
				silhouette_score = metrics.silhouette_score(geotag_clus_scaled, labels)
				n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
				
				result = {'min_samples': x,
									'xi': y,
									'min_cluster_size': z,
									'n_clusters_': n_clusters_,
									'n_noise_': n_noise_,
									'silhouette_score': silhouette_score}
				optics_result.append(result)
				i += 1
				if i % 10 == 0:
					print('%d / 125 model has been made' % i)

optics_benchmark_df = pd.DataFrame(optics_result)
optics_benchmark_df.head()

# Building the OPTICS Clustering model 
min_samples = 12
xi = 0.04
min_cluster_size = 0.08
optics_model = OPTICS(min_samples=min_samples, xi=xi, min_cluster_size=min_cluster_size) 

# Training the model 
optics_model.fit(geotag_clus_scaled)

# Storing the cluster labels of each point 
labels = optics_model.labels_#[optics_model.ordering_] 
geotag_clus['cluster'] = optics_model.labels_
  
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)
silhouette_score = metrics.silhouette_score(geotag_clus_scaled, labels+1)

print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
print('Silhouette Coefficient: %0.3f' % silhouette_score)

cimgt.GoogleWTS.get_image = new_get_image
request = cimgt.GoogleTiles()

fig = plt.figure(figsize=(16,16))
mymap = plt.axes(projection=ccrs.PlateCarree())
mymap.set_extent(extent)
mymap.add_image(request, 11)

# adding silhouette_score to the plot
props = dict(boxstyle='square', facecolor='white', alpha=1)
mymap.text(0.63, 0.05, 'Silhouette score: %.3f' % silhouette_score, transform=mymap.transAxes, fontsize=10,
           verticalalignment='top', bbox=props)

colors = ['c.', 'b.', 'r.', 'y.', 'g.', 'm.']

for Class, colour in zip(range(0, n_clusters_), colors): 
  Xk = geotag_clus.loc[geotag_clus['cluster'] == Class]
  mymap.plot(Xk['location_longitude'], Xk['location_latitude'], colour, alpha = 0.3) 
geotag_clus['location_longitude'].loc[geotag_clus['cluster'] == -1]
# plotting the outlier
mymap.plot(geotag_clus['location_longitude'].loc[geotag_clus['cluster'] == -1],
           geotag_clus['location_latitude'].loc[geotag_clus['cluster'] == -1], 
           'k+', alpha = 0.1) 

plt.suptitle('Geotagged Photo in Sarbagita Metropolitan Area\nClustered using OPTION Algorithm', fontsize=16, fontweight=600, ha='center', va='top')
plt.title('(min_samples = {0}, xi = {1}, min_cluster_size = {2})' .format(min_samples, xi, min_cluster_size), fontsize=12, ha='center', va='bottom')
# plt.savefig("/content/drive/My Drive/Colab Notebooks/FlickrCrawling/Sarbagita/Maps/OPTICS({0}, {1}, {2}).png" .format(min_samples, xi, min_cluster_size), dpi=1200)

plt.savefig("IMG/clustering.jpg")