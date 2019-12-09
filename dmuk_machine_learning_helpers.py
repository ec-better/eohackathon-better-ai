import os
from urllib.parse import urlparse
import gdal

def hello_world():
    
    print ('Hello World!')
    
    
def get_vsi_url(enclosure, username, api_key):
    
    
    parsed_url = urlparse(enclosure)

    url = '/vsicurl/{}://{}:{}@{}/api{}'.format(list(parsed_url)[0],
                                            username, 
                                            api_key, 
                                            list(parsed_url)[1],
                                            list(parsed_url)[2])
    
    return url 


def vsi_download(enclosure, geom, username, api_key, bands):
    
    vsi_url = get_vsi_url(enclosure, username, api_key)
    
    bbox = list(geom.bounds)
    
    ulx, uly, lrx, lry = bbox[0], bbox[3], bbox[2], bbox[1] 
    
    res = []
    for band in bands:
        
        output = 'data/subset_b{}_{}'.format(band,
                                             os.path.split(urlparse(enclosure).path)[1])

        ds = gdal.Open(vsi_url)


        ds = gdal.Translate(destName=output, 
                            srcDS=ds, 
                            projWin = [ulx, uly, lrx, lry], 
                            projWinSRS = 'EPSG:4326',
                            outputType=gdal.GDT_UInt16, 
                            bandList=[band])
        ds = None
    
        res.append(output)
        
    return res