# @author Ashraf
# This python code finds the nearest station for each of the stations
# prints nearest station and the distance with nearest station in miles.
# For the stations (csv-text) file, make sure station name, lat and long values are in column 1, 2, 3
# Place the files in current directory and update the values of event_file_name and station_file_name before running
# Recommended python version 2.7.*

from geopy.distance import vincenty

station_file_name = "station_info.csv"
station_file = open(station_file_name,"r")
stations = station_file.readlines()

event_row_one = True
for station_1 in stations:
    if event_row_one == True:
        event_row_one = False
        continue

    station_1 = station_1.split(",")

    station_row_one = True
    min_distance = 99999999999999999
    nearest_station = ''
    for station_2 in stations:
        if station_row_one == True:
            station_row_one = False
            continue
        station_2 = station_2.split(",")

        station1_loc = (float(station_1[1]),float(station_1[2]))
        station2_loc = (float(station_2[1]),float(station_2[2]))
        distance = vincenty(station1_loc, station2_loc).miles
        # print(station[0] + " " + `distance`)
        if distance < min_distance and station_1[0] != station_2[0]:
            min_distance = distance
            nearest_station = station_2[0]

    print(station_1[0] + " and " + nearest_station + ", Distance: " + `min_distance` + " miles.")
    # print(nearest_station)
