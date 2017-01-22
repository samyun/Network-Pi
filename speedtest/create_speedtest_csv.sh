#!/bin/bash
echo "Running speedtest"
speedtest --json > /home/pi/speedtest/unfiltered.json

echo "Parsing results"
python3.6 /home/pi/speedtest/parse_speedtest_json.py

# Check for file
echo "Checking file was made"
if [ -e /home/pi/speedtest/filtered.json ]
then
  echo "Importing to MongoDB"
  mongoimport --db SPEEDTEST_DATA --collection data --file /home/pi/speedtest/filtered.json

  echo "Exporting to CSV"
  mongoexport --db SPEEDTEST_DATA --collection data --fields "Date,Download (bps),Upload (bps)" --type=csv | tail -n+2 | sed 's/\"//g' > /home/pi/speedtest/bps.csv
  mongoexport --db SPEEDTEST_DATA --collection data --fields "Date,Download (kbps),Upload (kbps)" --type=csv | tail -n+2 | sed 's/\"//g' > /home/pi/speedtest/kbps.csv
  mongoexport --db SPEEDTEST_DATA --collection data --fields "Date,Download (Mbps),Upload (Mbps)" --type=csv | tail -n+2 | sed 's/\"//g' > /home/pi/speedtest/mbps.csv
  sed -i '1i Date,Download,Upload' /home/pi/speedtest/bps.csv
  sed -i '1i Date,Download,Upload' /home/pi/speedtest/kbps.csv
  sed -i '1i Date,Download,Upload' /home/pi/speedtest/mbps.csv

  echo "Moving CSVs to site"
  mv /home/pi/speedtest/bps.csv /var/www/html/data/bps.csv
  mv /home/pi/speedtest/kbps.csv /var/www/html/data/kbps.csv
  mv /home/pi/speedtest/mbps.csv /var/www/html/data/mbps.csv
fi
