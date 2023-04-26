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
    try:
        while end != "THE END":
            if args.method == None:
                args.method = input(str('Transformation name: ')).upper()
            if args.ellip == None:
                args.ellip = input(str('Ellipsoid model: ')).upper()
            if args.dat == None:
                args.dat = input(str('Enter the path to the txt file with data: '))

            sth = Transformations()
            method = transformations[args.method]
            if method == 'XYZ2BLH':
                data_out = sth.XYZ2BLH(args.dat, args.ellip)
            if method == 'BLH2XYZ':
                data_out = sth.BLH2XYZ(args.dat, args.ellip)
            if method == 'XYZ2NEU':
                data_out = sth.XYZ2NEU(args.dat, args.ellip)
            if method == 'BL2XY2000':
                data_out = sth.BL2XY2000(args.dat, args.ellip)
            if method == 'BL2XY1992':
                data_out = sth.BL2XY1992(args.dat, args.ellip)

            end = input(str("If you want to close the program, type - THE END, if you want to continue, type anything: ")).upper()
            args.ellip = None
            args.dat = None
            args.method = None

    except FileNotFoundError:
        print('File not found.')
    except KeyError:
        print('Incorrect program parameters.')
    except IndexError:
        print('Wrong data format.')
    except ValueError:
        print('Wrong data format.')
    finally:
        print(20 * '*')
        print('THE END')
