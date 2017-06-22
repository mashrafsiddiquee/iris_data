# @author Ashraf
# This code downloads data from the iris site
# Current configuration downloads all data of ZH network except the SM series (+SM125).
# Current configuration downloads all data of the month of April, 2010.
# To change the timing, change the starting date in the function date_init() and number_of_days()

import datetime
import ssl
import wget
import os
import sys

file = open("LOGFILE_SM.txt","w")

def date_init():
    return datetime.datetime(2010, 4, 1)

def number_of_days():
    return 30

def url_builder(network, station, chanel, date):

    url_part1 = 'https://service.iris.edu/irisws/timeseries/1/query?net='
    url_part2 = '&sta='
    url_part3 = '&cha='
    url_part4 = '&start='
    url_part5 = 'T00:00:00&end='
    url_part6 = 'T00:00:00&output=sacbl&loc=--'

    curr_date_str = date.strftime('%Y-%m-%d')
    date += datetime.timedelta(days=1)
    next_date_str = date.strftime('%Y-%m-%d')

    url = url_part1 + network + url_part2 + station + url_part3 + chanel + url_part4 + curr_date_str + url_part5 + next_date_str + url_part6
    return url


def filename_builder(network, station, chanel, date):

    curr_date_str = date.strftime('%Y.%m.%d')
    date += datetime.timedelta(days=1)
    next_date_str = date.strftime('%Y.%m.%d')

    filename = station + '.' + network + '..' + chanel + '.' + curr_date_str + '-' + next_date_str + '.SAC'
    return filename

def download(network, station, chanel, date):
    url = url_builder(network, station, chanel, date)
    filename = filename_builder(network, station, chanel, date)

    print(url)
    print(filename)
    print('\n')

    result = 0

    try:
        wget.download(url)
        os.rename('query', filename)
        print_str = "SUCCESS FOR STATION NO: " + `station` + ", ON DATE: " + `date` + "\n"
        file.write(print_str)
        result = 1
        print(" --> SUCCESS")
    except:
        print(sys.exc_info()[0])
        print_str = "EXCEPTION ON OCCURED STATION NO: " + `station` + ", ON DATE: " + `date` + "\n"
        file.write(print_str)

    return result

ssl._create_default_https_context = ssl._create_unverified_context          # This line is to bypass the certificate verification of the SSL.

# stations = ['GBCN', 'GBCS', 'GBNO', 'GBSE', 'GBSW', 'RCCE', 'RCEA', 'RCNW', 'RCSW', 'RPCE', 'RPCW', 'RPNE', 'RPSE', 'RPWE', 'SE01', 'SE04', 'SE05', 'SE06', 'SE07', 'SE08', 'SE09', 'SE10', 'SE12', 'SE13', 'SE14', 'SE15', 'SE16', 'SE17', 'SE18', 'SE19', 'SE20', 'SE21', 'SE22', 'SM01', 'SM03', 'SM04', 'SM05', 'SM06', 'SM07', 'SM08', 'SM09', 'SM10', 'SM11', 'SM12', 'SM125', 'SM13', 'SM14', 'SM15', 'SM16', 'SM18', 'SM19', 'SM20', 'SM22', 'SM24', 'SM27', 'SM28', 'SM29', 'SM30', 'SM31', 'SM32', 'SM33', 'SM34', 'SM35', 'SM36', 'SM37', 'SM38', 'SM39', 'SM40', 'SM41', 'SM42', 'SM43', 'SM44', 'SM45', 'SM46', 'SM47', 'SM48', 'SM49', 'SM50', 'SM51', 'SM52', 'SM53', 'SM54', 'SM55', 'SM56', 'SM57', 'SM58', 'SM59', 'SM60', 'SM61', 'SM62', 'SM63', 'SM64', 'SM65', 'SM66', 'SN05', 'SN06', 'SN07', 'SN08', 'SN09', 'SN10', 'SN105', 'SN11', 'SN12', 'SN125', 'SN13', 'SN14', 'SN15', 'SN16', 'SN17', 'SN18', 'SN19', 'SN20', 'SN21', 'SN22', 'SN23', 'SN24', 'SN25', 'SN26', 'SN27', 'SN28', 'SN29', 'SN30', 'SN31', 'SN32', 'SN33', 'SN35', 'SN36', 'SS02', 'SS03', 'SS04', 'SS05', 'SS06', 'SS07', 'SS08', 'SS09', 'SS11', 'SS12', 'SS13', 'SS14', 'SS16', 'SS17', 'SS18', 'SS182', 'SS185', 'SS19', 'SW03', 'SW04', 'SW05', 'SW06', 'SW07', 'SW08', 'SW09', 'SW10', 'SW11', 'SW12', 'SW13', 'SW14', 'SW15', 'SW16', 'SW17', 'SW18', 'SW19', 'SW20', 'SW205', 'SW21', 'SW22', 'SW23', 'SW235', 'SW25', 'SW26', 'SW27', 'SW28']
stations = ['GBCN', 'GBCS', 'GBNO', 'GBSE', 'GBSW', 'RCCE', 'RCEA', 'RCNW', 'RCSW', 'RPCE', 'RPCW', 'RPNE', 'RPSE', 'RPWE', 'SE01', 'SE04', 'SE05', 'SE06', 'SE07', 'SE08', 'SE09', 'SE10', 'SE12', 'SE13', 'SE14', 'SE15', 'SE16', 'SE17', 'SE18', 'SE19', 'SE20', 'SE21', 'SE22', 'SM125', 'SN05', 'SN06', 'SN07', 'SN08', 'SN09', 'SN10', 'SN105', 'SN11', 'SN12', 'SN125', 'SN13', 'SN14', 'SN15', 'SN16', 'SN17', 'SN18', 'SN19', 'SN20', 'SN21', 'SN22', 'SN23', 'SN24', 'SN25', 'SN26', 'SN27', 'SN28', 'SN29', 'SN30', 'SN31', 'SN32', 'SN33', 'SN35', 'SN36', 'SS02', 'SS03', 'SS04', 'SS05', 'SS06', 'SS07', 'SS08', 'SS09', 'SS11', 'SS12', 'SS13', 'SS14', 'SS16', 'SS17', 'SS18', 'SS182', 'SS185', 'SS19', 'SW03', 'SW04', 'SW05', 'SW06', 'SW07', 'SW08', 'SW09', 'SW10', 'SW11', 'SW12', 'SW13', 'SW14', 'SW15', 'SW16', 'SW17', 'SW18', 'SW19', 'SW20', 'SW205', 'SW21', 'SW22', 'SW23', 'SW235', 'SW25', 'SW26', 'SW27', 'SW28']
network = 'ZH'
chanel = 'EHZ'
success_count = 0
failure_count = 0
for station in stations:
    date = date_init()
    for i in range(1, number_of_days() + 1):
        curr_result = download(network, station, chanel, date)
        if curr_result == 1:
            success_count += 1
        else:
            failure_count += 1
        date += datetime.timedelta(days=1)

print_str = "TOTAL SUCCESS: " + `success_count` + "\n" + "TOTAL FAILURE: " + `failure_count` + "\n"
print(print_str)
print("DONE!!!")
file.write(print_str)
file.write("DONE!!!")
file.close()