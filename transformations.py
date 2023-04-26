from math import *
import numpy as np
import datetime
import argparse


class Transformations:
    def __init__(self):
       
        """
        Ellipsoid parameters:
                a - major axis of the ellipsoid - equatorial radius
                b - minor axis of the ellipsoid - polar radius
                e2 - square of the eccentricity.
        """
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
        
        """
        Hirvonen's algorithm - an algorithm used to transform Cartesian (rectangular)
        coordinates X, Y, Z into geodetic coordinates B, L, H.

        INPUT:
        file_txt : [str] - a string containing the name of the input file with XYZ coordinates
        ellipsoid_name : [str] - a string containing the name of the ellipsoid to be used

        OUTPUT:
        data_out : [list] - a list containing the geodetic coordinates (latitude, longitude, height) for each point in
                            the input file.

        """
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
        today = datetime.date.today()
        with open('report_XYZ2BLH.txt', 'w') as file:
            file.write(f'Date of creation of the report with coordinates: {today} \n')
            file.write('-------------------------------------------------------\n')
            file.write('{:^10s} {:^12s} {:^14s} {:^18s}\n'.format('Point_number', 'B [°]', 'L [°]', 'H [m]'))
            file.write('-------------------------------------------------------\n')
            for x in data_out:
                file.write('{:^10} {:^15.5f} {:^15.5f} {:^15.3f}\n'.format(x[0], x[1], x[2], x[3]))
            file.write('-------------------------------------------------------')
        return (data_out)


    def BLH2XYZ(self, file_txt, ellipsoid_name):
        
        """
        The following function converts geodetic coordinates (BLH) to cartesian coordinates (XYZ) using the specified
        ellipsoid.

        INPUT:
        file_txt : [str] - Path to the input file containing BLH coordinates of points
        ellipsoid_name:[str]    - Name of the ellipsoid to use for the conversion
                                  (must be a key in the `ellipsoid` dictionary of the object)
        OUTPUT:
        data_out : [list] - List of XYZ coordinates of each point in the input file
        """
        a = self.ellipsoid[ellipsoid_name]['a']
        e2 = self.ellipsoid[ellipsoid_name]['e2']
        data_in = self.file_reading(file_txt)

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

        today = datetime.date.today()
        with open('report_BLH2XYZ.txt', 'w') as file:
            file.write(f'Date of creation of the report with coordinates: {today} \n')
            file.write('-------------------------------------------------------\n')
            file.write('{:^10s} {:^15s} {:^15s} {:^15s}\n'.format('Point_number', 'X [m]', 'Y [m]', 'Z [m]'))
            for x in data_out:
                file.write('{:^10} {:^15.3f} {:^15.3f} {:^15.3f}\n'.format(x[0], x[1], x[2], x[3]))
            file.write('-------------------------------------------------------')
        return (data_out)

    def XYZ2NEU(self, file_txt, ellipsoid_name):
        
        """
        This function transforms XYZ coordinates to NEU coordinates based on a specified ellipsoid.

        INPUTS:
        file_txt : [str] - a string containing the name of the input file with XYZ coordinates
        ellipsoid_name : [str] - a string containing the name of the ellipsoid to be used.

        OUTPUTS:
        data_out : [list] - a list containing the NEU coordinates (northing, easting, upper) for each point in the
        input file.
        """
        a = self.ellipsoid[ellipsoid_name]['a']
        e2 = self.ellipsoid[ellipsoid_name]['e2']
        data_in = self.file_reading(file_txt)

        data_out = []
        for i in data_in:
            Point_number, X_init, Y_init, Z_init, X_final, Y_final, Z_final = i
            p = np.sqrt(X_init ** 2 + Y_init ** 2)
            B = np.arctan(Z_init / (p * (1 - e2)))
            while True:
                N = a / np.sqrt(1 - e2 * np.sin(B) ** 2)
                H = (p / np.cos(B)) - N
                Bp = B
                B = np.arctan(Z_init / (p * (1 - e2 * (N / (N + H)))))
                if np.abs(Bp - B) < (0.000001 / 206265):
                    break
            L = np.arctan2(Y_init, X_init)
            R = np.array([[-np.sin(B) * np.cos(L), -np.sin(L), np.cos(B) * np.cos(L)],
                          [-np.sin(B) * np.sin(L), np.cos(L), np.cos(B) * np.sin(L)],
                          [np.cos(B), 0, np.sin(B)]])
            dXYZ = np.array([[X_final - X_init], [Y_final - Y_init], [Z_final - Z_init]])
            dNEU = R.T @ dXYZ
            data_out.append([Point_number, dNEU[0][0], dNEU[1][0], dNEU[2][0]])

        today = datetime.date.today()
        with open('report_XYZ2NEU.txt', 'w') as file:
            file.write(f'Date of creation of the report with coordinates: {today} \n')
            file.write('-------------------------------------------------------\n')
            file.write('{:^10s} {:^15s} {:^15s} {:^15s}\n'.format('Point_number', 'northing', 'easting', 'up'))
            for x in data_out:
                file.write('{:^10} {:^15.3f} {:^15.3f} {:^15.3f}\n'.format(x[0], x[1], x[2], x[3]))
            file.write('-------------------------------------------------------')
        return (data_out)
        
    def BL2XY2000(self, file_txt, ellipsoid_name):
        
        """
        This function converts BL (latitude and longitude) coordinates to XY2000 coordinates based on a specified ellipsoid.

        INPUTS:
        - file_txt : [str] - the name of the input file containing the BL coordinates.
        - ellipsoid_name : [str] - the name of the ellipsoid to be used.

        OUTPUTS:
        - data_out : [list] - a list containing the XY2000 coordinates for each point in the input file.
        """
        a = self.ellipsoid[ellipsoid_name]['a']
        e2 = self.ellipsoid[ellipsoid_name]['e2']
        data_in = self.file_reading(file_txt)

        data_out = []
        for i in data_in:
            Point_number, B, L = i

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

            data_out.append([Point_number, X, Y])
            today = datetime.date.today()

            with open('report_BL2XY2000.txt', 'w') as file:
                file.write(f'Date of creation of the report with coordinates: {today} \n')
                file.write('-------------------------------------------------------\n')
                file.write('{:^10s} {:^15s} {:^15s}\n'.format('Point_number', 'X [m]', 'Y [m]'))
                for x in data_out:
                     file.write('{:^10} {:^15.3f} {:^15.3f}\n'.format(x[0], x[1], x[2]))
                file.write('-------------------------------------------------------')
        return (data_out)


        
       
    def BL2XY1992(self, file_txt, ellipsoid_name):
        
        """
        This function converts BL (latitude and longitude) coordinates to XY1992 coordinates based on a specified ellipsoid.

        INPUTS:
        - file_txt : [str] - the name of the input file containing the BL coordinates.
        - ellipsoid_name : [str] - the name of the ellipsoid to be used.

        OUTPUTS:
        - data_out : [list] - a list containing the XY1992 coordinates for each point in the input file.
        """
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
            data_out.append([Point_number, X, Y])

        today = datetime.date.today()
        with open('report_BL2XY1992.txt', 'w') as file:
            file.write(f'Date of creation of the report with coordinates: {today} \n')
            file.write('-------------------------------------------------------\n')
            file.write('{:^10s} {:^18s} {:^18s}\n'.format('Point_number', 'X [m]', 'Y [m]'))
            for x in data_out:
                file.write('{:^10} {:^15.3f} {:^15.3f}\n'.format(x[0], x[1], x[2]))
            file.write('-------------------------------------------------------')
        return (data_out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Transformation of coordinates')

    parser.add_argument('-dat',
                        type=str,
                        help='If the file is located in the same folder, enter its name with the extension. If the file is located elsewhere, enter the path.')
    parser.add_argument('-method',
                        type=str,
                        help='Accepts the name of the selected transformation (XYZ2BLH, BLH2XYZ, XYZ2NEU, BL2XY2000, BL2XY1992)')
    parser.add_argument('-ellip',
                        type=str,
                        help='Accepts the ellipsoid model (WGS84/ GRS80/ KRASOWSKI)')

    args = parser.parse_args()
    
    
    transformations = {'XYZ2BLH': 'XYZ2BLH',
                       'BLH2XYZ': 'BLH2XYZ',
                       'XYZ2NEU': 'XYZ2NEU',
                       'BL2XY2000': 'BL2XY2000',
                       'BL2XY1992': 'BL2XY1992'}

    end = ""
    