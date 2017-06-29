# @author Ashraf

from obspy import read
import matplotlib.pyplot as plt
import os.path

event_file_name = "89_earthquakes.csv"
event_file = open(event_file_name,"r")
events = event_file.readlines()

event_row_one = True
for event in events:
    if event_row_one == True:
        event_row_one = False
        continue
    event = event.split(",")

    sac_filename = event[0] + '.SAC'
    if os.path.exists(sac_filename) == False:
        print(sac_filename + " NOT FOUND")
        continue

    time = event[6].split(":")
    hour = float(time[0])
    min = float(time[1])
    sec = float(time[2])

    # print("for " + event[0] + " hour: " + `hour` + " minute: " + `min` + " sec: " + `sec`)

    sampling_rate = 100


    event_time = sampling_rate * (hour * 3600 + min * 60 + sec)
    start_time = event_time - (sampling_rate * 60)
    end_time = event_time + (sampling_rate * 60 * 7)

    st = read(sac_filename)
    extraced_series = st[0].data[start_time:end_time:]

    ts_file = open(event[0] + ".txt", "w")

    for amplitude in extraced_series:
        ts_file.write(`amplitude`)
        ts_file.write("\n")

    ts_file.close()

    plt.plot(extraced_series)
    plt.show()