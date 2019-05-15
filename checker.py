import csv
import pandas

fs_csv = pandas.read_csv("fifty-states.csv")
fs_csv.rename(columns={'Land Area: Sq. Mi.': 'LAND_AREA_SQ_MI'}, inplace = True)
fs_csv['LAND_AREA_SQ_MI'] = fs_csv['LAND_AREA_SQ_MI'].str.replace(",", "")
fs_csv.LAND_AREA_SQ_MI = pandas.to_numeric(fs_csv.LAND_AREA_SQ_MI)

required = fs_csv[['STATE', 'LAND_AREA_SQ_MI']]
sortLandArea = required.sort_values('LAND_AREA_SQ_MI', ascending = False)

print(sortLandArea) 
