# Network-Pi
Network connectivity tracking tool for the Raspberry Pi
Built for the Boilermake 2017 hackathon.
Created by Sam Yun and Zaheer Hasan

## Requirements
 - Raspberry Pi with network connectivity. 
 - Apache or other webserver
 - MongoDB v3.0.9
 - Python 3.6 w/ pytz module (install with pip3.6)
 - speedtest-cli

## Instructions
 NB: Note that MongoDB v3.0.9 and Python 3.6 aren't available through apt-get, as of 1/22/17. Manually install them. Shell script has 'python3.6' hardcoded. Update if needed.
 1. Download contents of speedtest/ folder to /home/pi/speedtest/. Update shell file and Python parsing file if location is changed.
 2. Download contents of html/ folder to /var/www/html/. Update shell file if location is changed.
 3. In MongoDB, create 'SPEEDTEST_DATA' database with 'data' collection. Update shell file if names are changed.
 4. Run shell script with: './create_speedtest_csv.sh', and verify /var/www/html/data/ contains the following files and values are expected:
    - bps.csv
    - kbps.csv
    - mbps.csv
 5. Add contents of crontab to Pi's cronetab at the bottom, by using the 'crontab -e' command.
 6. Every minute, the Pi should run a speedtest and add it to the CSVs in /var/www/html/data. Navigate to {pi's ip address} which should have the three graphs, which pull from the three CSVs.


