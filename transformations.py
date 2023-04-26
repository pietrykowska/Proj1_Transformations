from math import *
import numpy as np

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
                              

    def hirvonen(self): 
        a = self.ellipsoid['a']
        e2 = self.ellipsoid['e2']
        
        p = np.sqrt(X**2 + Y**2)
        f = np.arctan(Z / (p*(1 - e2)))
        while True:
            N = Np(f,a,e2)
            h = (p/np.cos(f)) - N
            fs = f
            f = np.arctan(Z / (p * (1 - e2 * N / (N + h))))
            if np.abs(fs - f) < (0.000001/206265):
                break
        l = np.arctan2(Y,X)
        return(f,l,h)
    
        
    def BLH2XYZ(ellipsoid_name):
        a = self.ellipsoid['a']
        e2 = self.ellipsoid['e2']

    #def NEU():

    #def XY2000():
        
    #def XY1992():    

        

#if __name__ == '__main__':
    