from math import *
import numpy as np
import datetime
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
        with open(file_txt, 'r') as file:
            lines = file.readlines()
            data = []
            for x in lines:
                x = x.split()
                b = [x[0]]
                x = [b.append(float(i)) for i in x[1:]]
                data.append(b)
        return (data)

    def XYZ2BLH(self, file_txt, ellipsoid_name):
        a = self.ellipsoid[ellipsoid_name]['a']
        e2 = self.ellipsoid[ellipsoid_name]['e2']
        
        data_in = self.file_reading(file_txt)
        data_out = []
        for i in data_in:
            Point_number, X, Y, Z = i
            p = np.sqrt(X ** 2 + Y ** 2)
            B = np.arctan(Z / (p * (1 - e2)))
            while True:
                N = a / np.sqrt(1 - e2 * np.sin(B) ** 2)
                H = (p / np.cos(B)) - N
                Bp = B
                B = np.arctan((Z / (p * (1 - e2 * (N / (N + H))))))
                if np.abs(Bp - B) < (0.000001 / 206265):
                    break
            L = np.arctan2(Y, X)
            B = B * 180 / pi
            L = L * 180 / pi
            data_out.append([Point_number, B, L, H])
        return (data_out)    
    
    def BLH2XYZ(self, file_txt, ellipsoid_name):
        a = self.ellipsoid[ellipsoid_name]['a']
        e2 = self.ellipsoid[ellipsoid_name]['e2']
        data_in = [self.file_reading(file_txt)]

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
        return (data_out)
    
    def XYZ2NEU(self, file_txt, ellipsoid_name):
        a = self.ellipsoid[ellipsoid_name]['a']
        e2 = self.ellipsoid[ellipsoid_name]['e2']
        data_in = self.file_reading(file_txt)
        
        p = np.sqrt(X_init ** 2 + Y_init ** 2)
        B = np.arctan(Z_init / (p * (1 - e2)))
        
        
        
        N = a / np.sqrt(1 - e2 * np.sin(f)**2)
        
        dneu = np.array([s * np.sin(z) * np.cos(alfa),
                         s * np.sin(z) * np.sin(alfa),
                         s * cos(z)])
        
        
        R = np.array([[-np.sin(f) * np.cos(l), -np.sin(l), np.cos(f) * np.cos(l)],
                     [ -np.sin(f) * np.sin(l), np.cos(l), np.cos(f) * np.sin(l)],
                     [np.cos(f), 0 ,np.sin(f)]])
    def BL2XY2000(self, file_txt, ellipsoid_name):
        a = self.ellipsoid[ellipsoid_name]['a']
        e2 = self.ellipsoid[ellipsoid_name]['e2']
        data_in = [self.file_reading(file_txt)]
        
        B = B * pi / 180
        L = L * pi / 180
        l0 = 0
        n = 0
        if L > 13.5 * pi / 180 and L < 16.5 * pi / 180:
            l0 = l0 + (15 * pi / 180)
            n = n + 5
        if L > 16.5 * pi / 180 and L < 19.5 * pi / 180:
            l0 = l0 + (18 * pi / 180)
            n = n + 6
        if L > 19.5 * pi / 180 and L < 22.5 * pi / 180:
            l0 = l0 + (21 * pi / 180)
            n = n + 7
        if L > 22.5 * pi / 180 and L < 25.5 * pi / 180:
            l0 = l0 + (24 * pi / 180)
            n = n + 8

        b2 = (a ** 2) * (1 - e2)
        ep2 = (a ** 2 - b2) / b2
        dL = L - l0
        t = np.tan(B)
        n2 = ep2 * (np.cos(B) ** 2)
        N = a / np.sqrt(1 - e2 * np.sin(B) ** 2)

        A0 = 1 - (e2 / 4) - ((3 * e2 ** 2) / 64) - ((5 * e2 ** 3) / 256)
        A2 = (3 / 8) * (e2 + (e2 ** 2) / 4 + (15 * e2 ** 3) / 128)
        A4 = (15 / 256) * (e2 ** 2 + (3 * e2 ** 3) / 4)
        A6 = (35 * e2 ** 3) / 3072
        sigma = a * ((A0 * B) - (A2 * np.sin(2 * B)) + (A4 * np.sin(4 * B)) - (A6 * np.sin(6 * B)))

        Xgk = sigma + ((dL ** 2 / 2) * N * np.sin(B) * np.cos(B) * (1 + (((dL ** 2) / 12) * (np.cos(B) ** 2) *
            (5 - t ** 2 + 9 * n2 + 4 * n2 ** 2)) + (((dL ** 4) / 360) * (np.cos(B) ** 4) * (61 - 58 * (t ** 2) +
            t ** 4 + 270 * n2 - 330 * n2 * (t ** 2)))))
        Ygk = dL * N * np.cos(B) * (1 + (((dL ** 2) / 6) * (np.cos(B) ** 2) * (1 - t ** 2 + n2)) +
                                    (((dL ** 4) / 120) * (np.cos(B) ** 4) * (5 - 18 * t ** 2 + t ** 4 + 14 * n2 -
                                                                             58 * n2 * t ** 2)))

        X = Xgk * 0.999923
        Y = Ygk * 0.999923 + n * 1000000 + 500000
        
    def BL2XY1992(self, file_txt, ellipsoid_name):
        a = self.ellipsoid[ellipsoid_name]['a']
        e2 = self.ellipsoid[ellipsoid_name]['e2']

        data_in = self.file_reading(file_txt)
        data_out = []

        for i in data_in:
            Point_number, B, L = i
            B = B * pi / 180
            L = L * pi / 180
            l0 = 19 * pi / 180
            b2 = (a ** 2) * (1 - e2)
            ep2 = (a ** 2 - b2) / b2
            dL = L - l0
            t = np.tan(B)
            n2 = ep2 * (np.cos(B) ** 2)
            N = a / np.sqrt(1 - e2 * np.sin(B) ** 2)

            A0 = 1 - (e2 / 4) - ((3 * e2 ** 2) / 64) - ((5 * e2 ** 3) / 256)
            A2 = (3 / 8) * (e2 + (e2 ** 2) / 4 + (15 * e2 ** 3) / 128)
            A4 = (15 / 256) * (e2 ** 2 + (3 * e2 ** 3) / 4)
            A6 = (35 * e2 ** 3) / 3072
            sigma = a * ((A0 * B) - (A2 * np.sin(2 * B)) + (A4 * np.sin(4 * B)) - (A6 * np.sin(6 * B)))

            Xgk = sigma + ((dL ** 2 / 2) * N * np.sin(B) * np.cos(B) * (
                    1 + (((dL ** 2) / 12) * (np.cos(B) ** 2) * (5 - t ** 2 + 9 * n2 + 4 * n2 ** 2)) + (
                    ((dL ** 4) / 360) * (np.cos(B) ** 4) * (
                    61 - 58 * (t ** 2) + t ** 4 + 270 * n2 - 330 * n2 * (t ** 2)))))
            Ygk = dL * N * np.cos(B) * (1 + (((dL ** 2) / 6) * (np.cos(B) ** 2) * (1 - t ** 2 + n2)) + (
                    ((dL ** 4) / 120) * (np.cos(B) ** 4) * (5 - 18 * t ** 2 + t ** 4 + 14 * n2 - 58 * n2 * t ** 2)))

            X = Xgk * 0.9993 - 5300000
            Y = Ygk * 0.9993 + 500000

       

#if __name__ == '__main__':
    