from geopy.distance import vincenty

event_file = open("89_earthquakes.csv","r")
events = event_file.readlines()

station_file = open("station_info.csv","r")
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

    # print("For event " + event[0] + ", Nearest station: " + nearest_station + ", Distance: " + `min_distance` + " miles.")
    print(nearest_station)
