class Transformations:
    def __init__(self):
       
            self.ellipsoid = {
                'GRS80': {'a': 6378137,
                          'b': 6356752.3141,
                          'e2': 0.00669438002290},
                        
                'WGS84': {'a': 6378137,
                          'b': 6356752.3142,
                          'e2': 0.00669437999014},
                         
                'KRASOWSKI': {'a': 6378245,
                              'b': 6356863.019,
                              'e2': 0.00669342162297}}
                              
#def XYZ2BLH
    def BLH2XYZ(ellipsoid_name):
        a = self.ellipsoid['a']
        e2 = self.ellipsoid['e2']

#def XYZ2NEU
#def BL2XY2000
#def BL2XY1992
            
       
