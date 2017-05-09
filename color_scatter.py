import gmplot
import pandas as pd
gmap = gmplot.GoogleMapPlotter.from_geocode("Chicago",12)
cols=['cyan','aqua','blueviolet','burlywood','brown','cadetblue','chartreuse','chocolate',
    'coral','cornflowerblue','darkcyan','darkgoldenrod','darkgray','darkgreen','darkmagenta','darkolivegreen',
    'darkorange','darkorchid','darkred','darkseagreen',
    'darkturquoise','darkviolet','deeppink','deepskyblue','dimgray',
     'firebrick','fuchsia','gold','gray','green','greenyellow','honeydew',
    'hotpink',
'indianred',
'indigo',
'ivory',
'khaki',
'lavender',
'lawngreen'  
'lightblue',
'lightcoral',
'lightcyan',
'lightgreen',
'lightgray',
'lightpink'
'lightsalmon',
'lightseagreen',
'lightskyblue',
'limegreen',
'magenta',
'maroon',
'mediumpurple',
'mediumseagreen',
'mediumslateblue',
'mediumspringgreen',
'mediumturquoise',
'mediumvioletred',
'midnightblue',
'mintcream',
'mistyrose',
'moccasin',
'navajowhite',
'navy',
'oldlace',
'olive',
'olivedrab',
'orange',
'orangered',
'orchid',
'palegoldenrod'
'papayawhip',
'peachpuff',
'peru',
'pink',
'plum',
'powderblue',
'purple',
'red',
'royalblue',
'silver',
'seagreen']
#reading from csv file
df=pd.read_csv('Graffiti_Removal.csv')

#creating lists of latitute and longitude
lats=[]
long=[]
import numpy as np
communiry_area=[]
for i in range(25000):
    if( np.isfinite(df.iloc()[i][15]) and np.isfinite(df.iloc()[i][16]) and  np.isfinite(df.iloc()[i][13])):
        lats.append(df.iloc()[i][15])
        long.append(df.iloc()[i][16])
        communiry_area.append(df.iloc()[i][13])

#plotting for each latitute and longitude		
for i in range(len(communiry_area)):
    community_area=int(communiry_area[i])
    gmap.scatter([lats[i]],[long[i]],cols[community_area], size=50,marker=False)

gmap.draw('map.html')

 
