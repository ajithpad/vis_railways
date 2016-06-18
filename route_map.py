import urllib2
import json
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
from matplotlib.colors import LinearSegmentedColormap
from geopy.geocoders import Nominatim
<<<<<<< HEAD
from bokeh import mpl
=======
>>>>>>> 1a3c3a0f65787327ab98bcba508a61812615dbfb
geolocator = Nominatim()
train_num = np.load('data/train_num.npy')
sbn.set(style = 'white',font_scale = 2)

def get_route(train_no):
    with open('data/route_json/route_of_'+train_no+'.json') as jsonfile:
        json_data = json.load(jsonfile)
    return json_data

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
fig3 = pl.figure(3, facecolor = 'white')
map = Basemap(projection='merc', lat_0 = 20, lon_0 = 80,
    resolution = 'h', area_thresh = 1.,
    llcrnrlon=67.0, llcrnrlat=7.0,
    urcrnrlon=96.0, urcrnrlat=37.0)

map.drawmapboundary()
#map.fillcontinents()
map.drawcoastlines()
map.drawcountries()

sup_lat_lis = []
sup_lon_lis = []
for train_no in train_num: 
    route = get_route(train_no)
    if route['route']: 
        data = route['route']
        lat_list = []
        lon_list = []
        for ii in range(len(data)-1):
#            location = geolocator.geocode(data[ii]['state'][-6:])
#            if location:
#                lat_list.append(location.latitude)
#                lon_list.append(location.longitude)
             
            if not data[ii]['lat'] == 0:
                if type(data[ii]['lat']) is float:
                    lat_list.append(data[ii]['lat'])
                    lon_list.append(data[ii]['lng'])

        sup_lat_lis += lat_list
        sup_lon_lis += lon_list
#        if (len(lon_list) > 1 and len(lat_list) > 1):
#            x,y = map(lon_list, lat_list)    
#            map.plot(x, y,'-',lw=1., alpha = 0.25, color = 'red') 

cdict = {'red':  ( (0.0,  1.0,  1.0),
                   (1.0,  1.0,  1.0) ),
         'green':( (0.0,  1.0,  1.0),
                   (1.0,  0.03, 0.0) ),
         'blue': ( (0.0,  1.0,  1.0),
                   (1.0,  0.0, 0.0) ) }
custom_map = LinearSegmentedColormap('custom_map', cdict)
plt.register_cmap(cmap=custom_map)
            
#Heatmaps to show the distribution of trains in India
db = 1
lon_bins = np.linspace(min(sup_lon_lis)-db, max(sup_lon_lis)+db, 30+1)
lat_bins = np.linspace(min(sup_lat_lis)-db, max(sup_lat_lis)+db, 30+1)

density, _, _ = np.histogram2d(sup_lat_lis, sup_lon_lis, [lat_bins, lon_bins])
density = np.hstack((density,np.zeros((density.shape[0],1))))
density = np.vstack((density,np.zeros((density.shape[1]))))

lon_bins_2d, lat_bins_2d = np.meshgrid(lon_bins, lat_bins)

xs, ys = map(lon_bins_2d, lat_bins_2d)
<<<<<<< HEAD

pl.pcolormesh(xs, ys, density, cmap = custom_map,vmax = 800, shading = 'flat')
#pl.contourf(xs,ys,density, cmap = custom_map, vmax = 800)
pl.title('Train density in India')
pl.colorbar()
=======

pl.pcolormesh(xs, ys, density, cmap = custom_map,vmax = 800, shading = 'flat')
#pl.contourf(xs,ys,density, cmap = custom_map, vmax = 800)
pl.title('Train density in India')
pl.colorbar()

>>>>>>> 1a3c3a0f65787327ab98bcba508a61812615dbfb
plt.show()