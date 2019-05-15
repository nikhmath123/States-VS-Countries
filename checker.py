import csv
import pandas

#Read CSV and format data 
fs = pandas.read_csv("fifty-states.csv")
fs.rename(columns={'Land Area: Sq. Mi.': 'LAND_AREA_SQ_MI'}, inplace = True)
fs.LAND_AREA_SQ_MI = fs.LAND_AREA_SQ_MI.str.replace(",", "")
fs.LAND_AREA_SQ_MI = pandas.to_numeric(fs.LAND_AREA_SQ_MI)

#Grab the two rows interested in and sort Land Area by Descending
required = fs[['STATE', 'LAND_AREA_SQ_MI']]
sortLandArea = required.sort_values('LAND_AREA_SQ_MI', ascending = False)
print(sortLandArea) 
