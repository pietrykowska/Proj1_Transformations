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

    def file_reading(self, file_txt):
        with open(file_txt, 'read') as file:
            lines = file.readlines()
            data = []
            for x in lines:
                x = x.split()
                b = [x[0]]
                x = [b.append(float(i)) for i in x[1:]]
                data.append(b)
        return

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
    
        
    def BLH2XYZ(self, file_text, ellipsoid_name):
        a = self.ellipsoid[ellipsoid_name]['a']
        e2 = self.ellipsoid[ellipsoid_name]['e2']
        data_in = []

        data_out = []
        for i in data_in:
            Point_number, B, L, H = i

            B = B * np.pi / 180
            L = L * np.pi / 180
            N = a / np.sqrt(1 - e2 * np.sin(B) ** 2)
            X = (N + H) * np.cos(B) * np.cos(L)
            Y = (N + H) * np.cos(B) * np.sin(L)
            Z = (N * (1 - e2) + H) * np.sin(B)

            data_out.append([Point_number, X, Y, Z])

    #def NEU():

    #def XY2000():
        
    #def XY1992():    

        

#if __name__ == '__main__':
    