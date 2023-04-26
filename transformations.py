class Transformations:
    def __init__(self):
       
            self.ellipsoid = {
                'GRS80': {'a': 6378137,
                          'b': 6356752.3141,
                          'e2': (a**2-b**2)/a**2},
                        
                'WGS84': {'a': 6378137,
                          'b': 6356752.3142,
                          'e2': (a**2-b**2)/a**2},
                         
                'KRASOWSKI': {'a': 6378245,
                              'b': 6356863.019,
                              'e2': (a**2-b**2)/a**2}}
            
    def hirvonen(): 
        
