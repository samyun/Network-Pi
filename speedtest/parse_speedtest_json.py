#!/usr/local/bin/python
import json
import datetime
from pytz import timezone
import pytz

utc = pytz.utc
eastern = timezone('US/Eastern')

fmt = '%Y-%m-%d %H:%M:%S'

failed_speedtest = False

with open('/home/pi/speedtest/unfiltered.json', 'r') as json_file:
    data_json = json_file.read()
    if len(data_json) == 0:
      failed_speedtest = True
    else:
      data = json.loads(data_json)
    json_file.close()

formatted_dict = {}
if not failed_speedtest:
  dt = datetime.datetime.strptime(data["timestamp"]+"UTC","%Y-%m-%dT%H:%M:%S.%f%Z")
  loc_dt = dt.astimezone(eastern)
  formatted_dict["Date"] = loc_dt.strftime(fmt)
  formatted_dict["Upload (bps)"] = round(data["upload"])
  formatted_dict["Upload (kbps)"] = round(data["upload"]/1024)
  formatted_dict["Upload (Mbps)"] = round(data["upload"]/1048576, 2)
  formatted_dict["Download (bps)"] = round(data["download"])
  formatted_dict["Download (kbps)"] = round(data["download"]/1024)
  formatted_dict["Download (Mbps)"] = round(data["download"]/1048576, 2)
else:
  formatted_dict["Date"] = datetime.datetime.now().astimezone(eastern).strftime(fmt)
  formatted_dict["Upload (bps)"] = 0
  formatted_dict["Upload (kbps)"] = 0
  formatted_dict["Upload (Mbps)"] = 0
  formatted_dict["Download (bps)"] = 0
  formatted_dict["Download (kbps)"] = 0
  formatted_dict["Download (Mbps)"] = 0

with open('/home/pi/speedtest/filtered.json', 'w') as outfile:
    json.dump(formatted_dict, outfile)
