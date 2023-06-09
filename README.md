# Geodetic coordinate transformations
The program is used to transform coordinates between different systems.
##### Available transformation variants:
```
[XYZ geocentric] --> [BLH ellipsoidal]
[BLH] --> [XYZ]
[XYZ] --> [NEUp topocentric]
[BL] --> [PL2000]
[BL] --> [PL1992]
```
##### Available ellipsoid models:
- GRS80
- WGS84
- KRASOWSKI

## Minimum hardware and software requirements:
- Windows 10
- Python 3.9 - recommended application: spyder (5.2.2) or PyCharm 2022.2.3
- The program uses libraries: math, numpy, argparse

## Program description:
To perform a transformation, the user should answer the questions asked in the console.

Selected transformation (XYZ2BLH, BLH2XYZ, XYZ2NEU, BL2XY2000, BL2XY1992)
```sh
-method
```
Selected ellipsoid model (WGS84/ GRS80/ KRASOWSKI)
```sh
-ellip
```
File with data or its path.
```sh
-dat
```
### Example call:
```sh
transformations.py
-method BLH2XYZ
-ellip GRS80
-dat blh.txt
```
After entering the above data on the console, the following printout will appear:
```sh
A report has been created and saved in the folder as the code.
If you want to close the program, type - THE END, if you want to continue, type anything: 
```
If we enter the phrase "THE END" with any number of characters, the program will end and a printout will be created on the console.
```sh
THE END ********************
```
If the program is to perform additional transformations, click any key on the keyboard and then fill in the data from the beginning.

Console printout:
```sh
Transformation name: XYZ2BLH
Ellipsoid model: GRS80
Enter the path to the txt file with data: C:\Users\Patrycja\Documents\studia\!PYTHON\Proj1_Transformations\xyz.txt
The report has been created and saved in the same folder as the code.
If you want to close the program, type - THE END, if you want to continue, type anything: THE END
THE END ******************** 
```

## Errors
If the path to the file is incorrect or the name of the transformation or geoid model is incorrect (regardless of case), the following message will appear:
```sh
Incorrect program parameters.
```
If the program has trouble reading data from the input file, the following message will appear:
```sh
Wrong data format.
```

## Example transformation:
for the XYZ2BLH method will create the file report_XYZ2BLH.txt:

File with input data.

Point_number    X [m]         Y [m]            Z[m]
```sh
1 3588382.360 696708.212 5209346.664 
2 3860222.175 518788.966 5034121.370 
3 4023193.575 880557.950 4854017.681 
```
Report saved on the user's computer.
```sh
Date of creation of the report with coordinates: 2023-04-28 
-------------------------------------------------------
Point_number    B [°]         L [°]            H [m]       
-------------------------------------------------------
    1         55.12345        10.98765         112.870    
    2         52.45678         7.65432         234.560    
    3         49.87654        12.34567         87.430 
```
## Other reports:
for the BLH2XYZ method will create the file report_BLH2XYZ.txt:
```sh
Date of creation of the report with coordinates: 2023-04-28 
-------------------------------------------------------
Point_number      X [m]           Y [m]           Z [m]     
    1        3588382.360     696708.212      5209346.664  
    2        3860222.175     518788.966      5034121.370  
    3        4023193.575     880557.950      4854017.681 
```
File with input data for the XYZ2NEU method (Calculations are performed based on the coordinates of the initial and final points of the segment).

Point_number    Xi[m]         Yi[m]         Zi[m]       Xf[m]         Yf[m]            Zf[m]
```sh
1 3588382.360 696708.212 5209346.664 3588301.222 696607.908 5209478.416
2 3860222.175 518788.966 5034121.370 3860207.527 518899.237 5033962.965
3 4023193.575 880557.950 4854017.681 4023158.879 880424.207 4854154.969
```
for the XYZ2NEU method will create the file report_XYZ2NEU.txt:
```sh
Date of creation of the report with coordinates: 2023-04-28 
-------------------------------------------------------
Point_number    northing         easting          upper     
    1          156.365         -83.001         51.611     
    2          -96.661         111.240        -125.495    
    3          136.256        -123.232         64.708
```
for the BL2XY2000 method will create the file report_BL2XY2000.txt:
```sh
Date of creation of the report with coordinates: 2023-04-28 
-------------------------------------------------------
Point_number      X [m]           Y [m]     
    1        6165803.286     1199423.389  
    2        5841329.260     1019874.949  
    3        5600212.483     1386122.802 
```
for the BL2XY1992 method will create the file report_BL2XY1992.txt:
```sh
Date of creation of the report with coordinates: 2023-04-29 
-------------------------------------------------------
Point_number       X [m]              Y [m]       
    1        836043.605      -10229.868   
    2        570847.921      -269380.345  
    3        244505.719       22210.752 
```

## Known errors:
Transformation BL_krasowski -> PL2000 and transformation BL_krasowski -> PL1992 give incorrect results of coordinates. There is no direct possibility of such transformation. If a person using this repository can solve this problem, please contact us.
