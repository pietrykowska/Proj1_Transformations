import argparse

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