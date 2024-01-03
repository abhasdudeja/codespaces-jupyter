import osmnx as ox
import pandas as pd
from osmnx import settings, graph, geocoder
from shapely import Polygon
import time
import numpy as np
settings.max_query_area_size = 150000000000

class Osm_Wrapper():

    '''
    Class to read OSM data and respond back with outputs

    Author: Abhas Dudeja

    Dependencies: Pandas, GeoPandas, OSMnx, Shapely.
    Date: 04 01 2024
    '''

    @staticmethod
    def get_bounds(name,type="country"):
        '''
        Return bounds of any name value, default type of name "country"
        '''
        res = geocoder.geocode_to_gdf({type:name})
        return res.unary_union.bounds