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
#print(sortLandArea) 

#Now do the same thing with countries
c = pandas.read_csv("countries of the world.csv")
c.rename(columns={'Country': 'COUNTRY', 'Area (sq. mi.)': 'LAND_AREA_SQ_MI'}, inplace = True)
# ***The Area in this csv doesn't contain commas so nothing else needs to be done***

required2 = c[['COUNTRY', 'LAND_AREA_SQ_MI']]
sortLandArea2 = required2.sort_values('LAND_AREA_SQ_MI', ascending = False)
print(sortLandArea2)

