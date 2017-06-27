# @author Ashraf
# This python code takes earthquake events catalog and station info from file and
# prints nearest station for each event based on latitude and longitude.
# For the events (csv-text) file, make sure lat and long values are in column 2 and 3.
# For the stations (csv-text) file, make sure station name, lat and long values are in column 1, 2, 3
# Place the files in current directory and update the values of event_file_name and station_file_name before running


from geopy.distance import vincenty

event_file_name = "89_earthquakes.csv"
station_file_name = "station_info.csv"

event_file = open(event_file_name,"r")
events = event_file.readlines()

station_file = open(station_file_name,"r")
stations = station_file.readlines()

event_row_one = True
for event in events:
    if event_row_one == True:
        event_row_one = False
        continue
    event = event.split(",")

    station_row_one = True
    min_distance = 99999999999999999
    nearest_station = ''
    for station in stations:
        if station_row_one == True:
            station_row_one = False
            continue
        station = station.split(",")

        event_loc = (float(event[1]),float(event[2]))
        station_loc = (float(station[1]),float(station[2]))
        distance = vincenty(event_loc, station_loc).miles
        # print(station[0] + " " + `distance`)
        if distance < min_distance:
            min_distance = distance
            nearest_station = station[0]

    print("For event " + event[0] + ", Nearest station: " + nearest_station + ", Distance: " + `min_distance` + " miles.")
    # print(nearest_station)
