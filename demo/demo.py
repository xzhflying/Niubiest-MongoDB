''' This is a simple demo of weather analyze system
    Version 0.1
    @Zihuan Xu and Hongrui Li
    Modified by Zihuan Xu

    This demo can only take in the input of a cirtain name of city (in China)
    and a distance\ a range of temperature\ a range of date which users can tolerate.
    Then output sutable cities' information.

    Entire project descriptions:
    Basic function:
        Users can select the location in which they prefer to arrange their plan.
        Users can choose a range of distance that they can tolerate. And a range of date during which they are care about the weather
        Users can choose the weather (average temperature\ weather condition\ wind may be more important than other weather information ) that they can tolerate
        Weather contains temperature(lowest and highest)\ strength of wind\ direction of wind\ weather condition\ humidity\ air quality
        Finally, system should return the places which meet the requirement or show users analyses of each place
        Data sets come from the internet (NOAA) and should be updated every day

'''


import pymongo
import math
import copy


#connect to database
connection = pymongo.Connection('localhost',27017)
db = connection.weather
temperature = db.temperature

# get the range of latitude and longitude by a given point and a distance range
def getRange(lat , lon , distance):
    PI = 3.14159265359
    DEF_R = 6370693.5

    lat = lat * PI /180
    lon = lon * PI /180
    rad_dist = distance / DEF_R
    lat_min = lat - rad_dist
    lat_max = lat + rad_dist

    if(lat_min > -PI/2 and lat_max < PI/2):
        lon_t = math.asin( math.sin(rad_dist) / math.cos(lat) )
        lon_min = lon - lon_t
        if lon_min < -PI:
            lon_min = 2 * PI +lon_min
        lon_max = lon + lon_t
        if lon_max > PI:
             lon_max = 2 * PI - lon_max

    else:
        lat_min = max (lat_min , -PI/2)
        lat_max = min (lat_max, PI/2)
        lon_min = -PI
        lon_max = PI

    lat_min = lat_min * 180 / PI
    lat_max = lat_max * 180 / PI
    lon_min = lon_min * 180 / PI
    lon_max = lon_max *180 / PI
    result = (lat_max, lat_min, lon_max, lon_min)
    return result


# get the latitude and longitude by a given city name
def getLAT_AND_LON(city):

    result = temperature.find_one({"STATION_NAME":city})
    if result is not None:
        latitude = result["LATITUDE"]
        longitude = result["LONGITUDE"]
    else:
        print("There is no such city!")
        return None
    return (latitude,longitude)


# get the average temperature of each city within the range 
def get_average_temperature(Range,earliest,latest):

    #i = latest - earliest
    tmpMax = 0
    tmpMin = 0
    index = 0
    isNewItem = True
    tmpHighCount = 0
    tmpLowCount = 0

    cityInfo = []
    #citynum = temperature.find({"LATITUDE" : {'$gt': Range[1], '$lt': Range[0]}, "LONGITUDE" : {'$gt':Range[3], '$lt': Range[2]}, "DATE" : {'$gt': earliest, '$lt': latest}}).count()
    
    row = [0]*3     # An item of city information
    
    cityInfo.append(copy.copy(row))     # The selected(or central) city's item
   
 
    for result in temperature.find({"LATITUDE" : {'$gt': Range[1], '$lt': Range[0]}, "LONGITUDE" : {'$gt':Range[3], '$lt': Range[2]}, "DATE" : {'$gt': earliest, '$lt': latest}}):
        
        if result["STATION_NAME"] != cityInfo[index-1][0]:
            cityInfo.append(copy.copy(row))
            cityInfo[index][0] = str(result["STATION_NAME"])
            if tmpHighCount != 0:
                cityInfo[index-1][1] = round(tmpMax/tmpHighCount/10,2)
            else:
                cityInfo[index-1][1] = "No Data"
            if tmpLowCount != 0:
                cityInfo[index-1][2] = round(tmpMin/tmpLowCount/10,2)
            else:
                cityInfo[index-1][2] = "No Data"
            tmpMax = 0
            tmpMin = 0
            index = index+1
            isNewItem = True  

        if isNewItem: 
            tmpHighCount = 0
            tmpLowCount = 0
            isNewItem = False
        
        if result["TMAX"] != -9999:
            tmpMax = float(result["TMAX"]) + tmpMax
            tmpHighCount = tmpHighCount + 1
        if result["TMIN"] != -9999:
            tmpMin = float(result["TMIN"]) + tmpMin
            tmpLowCount = tmpLowCount + 1
        

    # This part of code calculate the last item's average temperature, 
    # because there is no new city name to make the condition "result["STATION_NAME"] != cityInfo[index-1][0]" becomes true
    if tmpHighCount != 0:
        cityInfo[index-1][1] = round(tmpMax/tmpHighCount/10,2)
    else:
        cityInfo[index-1][1] = "No Data"
    if tmpLowCount != 0:
        cityInfo[index-1][2] = round(tmpMin/tmpLowCount/10,2)
    else:
        cityInfo[index-1][2] = "No Data"


    del cityInfo[index]  # delete the last blank row
    
    return cityInfo

# take in the average temperature of each city within the range then return information of suitable cities
def get_suitable_cities(AVER_TEMP,MAXT,MINT):
    cities = ()
    for item in AVER_TEMP:
        if item[1] <= MAXT and item[2] >= MINT:
            cities = cities + (item[0],)
    if cities == ():
        return None
    else:
        return cities
    
# user input the central city
while(True):
    central_city = raw_input("please input central city's name :")
    LAT_AND_LON = getLAT_AND_LON(central_city)      # convert city name into latitude and longitude
    if LAT_AND_LON != None:
        break

while(True):     # user input a tolerable distance
    distance = None
    # make sure that user input a number
    try:
        distance = input("please input limit of distance (meters):")
    except:pass

    if (type(distance) == float or type(distance) == int) and distance >= 0:
        distance = float(distance)
        break

Range = getRange(LAT_AND_LON[0], LAT_AND_LON[1], distance)      # count latitude and longitude range

# input a range of date
while (True):
    earliest = None
    # make sure that user input a number
    try:
        earliest = input("please input earliest date (like: 20150101):")
    except:pass
    if type(earliest) == int:
        break
while (True):
    latest = None
    # make sure that user input a number
    try:
        latest = input("please input latest date (like: 20150101):")
    except:pass
    if type(latest) == int:
        break

# input a range of tolerable temperature
while (True):
    MAX_TEMP = None
    # make sure that user input a number
    try:
        MAX_TEMP = input("please input MAX temperature that you can tolerate (Centigrade):")
    except:pass
    if type(MAX_TEMP) == float or type(MAX_TEMP) == int:
        MAX_TEMP = float(MAX_TEMP)
        break
while (True):
    MIN_TEMP = None
    # make sure that user input a number
    try:
        MIN_TEMP = input("please input MIN temperature that you can tolerate (Centigrade):")
    except:pass
    if type(MIN_TEMP) == float or type(MIN_TEMP) == int:
        MIN_TEMP = float(MIN_TEMP)
        break
        
# count average temperature of cities in the area
AVER_TEMP = get_average_temperature(Range,earliest,latest)

# pick up suitable cities
suitable_cities = get_suitable_cities(AVER_TEMP,MAX_TEMP,MIN_TEMP)

if suitable_cities != None:
    print("\n\nSuitable cities are:")
    for city in suitable_cities:
        print(city)
else:
    print("\n\n There is no suitable city!")

print("\n\n information of cities within this area :\n")
print("|----------------------------------------------------------|")
print("|     Name     | Max_temp in average | Min_temp in average |")
print("|----------------------------------------------------------|")
for item in AVER_TEMP:
    print(item)
