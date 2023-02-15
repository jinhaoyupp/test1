import cv2 as cv
import numpy as np
# from libtiff import TIFF
import matplotlib.pyplot as plt
import pandas as pd
# from pykrige.ok import OrdinaryKriging
import shapefile
from matplotlib.path import Path
from matplotlib.patches import PathPatch
# import matplotlib.pyplot as plt
# import numpy as np
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

#
# def shp2clip(originfig, ax, shpfile):
#     sf = shapefile.Reader(shpfile)
#     vertices = []
#     codes = []
#     for shape_rec in sf.shapeRecords():
#         pts = shape_rec.shape.points
#         prt = list(shape_rec.shape.parts) + [len(pts)]
#         for i in range(len(prt) - 1):
#             for j in range(prt[i], prt[i + 1]):
#                 vertices.append((pts[j][0], pts[j][1]))
#             codes += [Path.MOVETO]
#             codes += [Path.LINETO] * (prt[i + 1] - prt[i] - 2)
#             codes += [Path.CLOSEPOLY]
#         clip = Path(vertices, codes)
#         clip = PathPatch(clip, transform=ax.transData)
#     for contour in originfig.collections:
#         contour.set_clip_path(clip)
#     return contour
#
#
# img1 = cv.imread('/Users/jinhaoyu/Downloads/extremePreExpo/GDP/GDP1995.tif', -1)
# img2 = cv.imread('/Users/jinhaoyu/Downloads/extremePreExpo/GDP/GDP2000.tif', -1)
# img3 = cv.imread('/Users/jinhaoyu/Downloads/extremePreExpo/GDP/GDP2005.tif', -1)
# img4 = cv.imread('/Users/jinhaoyu/Downloads/extremePreExpo/GDP/GDP2010.tif', -1)
# img5 = cv.imread('/Users/jinhaoyu/Downloads/extremePreExpo/GDP/GDP2015.tif', -1)
#
#
# gdp1995 = img1
# gdp1995[gdp1995 < 0] = 0
#
# gdp2000 = img2
# gdp2000[gdp2000 < 0] = 0
#
# gdp2005 = img3
# gdp2005[gdp2005 < 0] = 0
#
# gdp2010 = img4
# gdp2010[gdp2010 < 0] = 0
#
# gdp2015 = img5
# gdp2015[gdp2015 < 0] = 0


# print (img1)
# print (img1.shape)
# print (img1.dtype)
# print (img1.min())
# print (img1.max())
# #创建窗口并显示图像
# # cv.namedWindow("Image")
# # cv.imshow("Image",img)
# # cv.waitKey(0)
# # #释放窗口
# # cv.destroyAllWindows()
# gdp1995 = img1
# gdp1995[gdp1995 < 0] = 0
plt.imshow(gdp1995)
plt.show()

#
# fig = plt.figure(figsize=(12, 8))
# ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
# ax.set_extent([116, 122.1, 30, 35.6], crs=ccrs.PlateCarree())
#
# province = shpreader.Reader('/Users/jinhaoyu/Downloads/china-shapefiles/provincesample.shp')
# # c = ax.contourf(lon,lat,data,cmap='coolwarm')
# c = ax.contourf(gdp1995)
# ax.add_geometries(province.geometries(), crs=ccrs.PlateCarree(), linewidths=0.5, edgecolor='k',
#                 facecolor='none')
#
# ax.xaxis.set_major_formatter(LongitudeFormatter(zero_direction_label=True))
# ax.yaxis.set_major_formatter(LatitudeFormatter())
# ax.set_xticks(np.arange(116,122.1,1),crs=ccrs.PlateCarree())
# ax.set_yticks(np.arange(30,35.7,1),crs=ccrs.PlateCarree())
#
# shp2clip(c, ax, '/Users/jinhaoyu/Downloads/china-shapefiles/provincesample.shp')
# cb = plt.colorbar(c)
# cb.set_label('克里金温度插值', fontsize=15)
# plt.show()
#

















