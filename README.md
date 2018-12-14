# homedata

## Included Within Dataset

- 4 months of door open / close data for our front and back door
- 2.5 years of temperature and humidity data for second floor of our house
- 19 months of temperature and humidity data for the first floor
- 9 months of tVOC data for the first floor
- 9 months of temperature and humidity for the basement
- 9 months of temperature data for the attic space behind our knee wall (to help correlate with ice dams).

## Description of Data Files

home-data_2018.dump

This is the main file we are going to want to use.  This includes all of the above described data.

## Environmental Parameters Description

### House Description

* This data is from a house located in the 13th Ward of Minneapolis, Minnesota.
* This is a one and a half story house with about 1,200 square feet of finished area and an unfinished basement.

#### Illustration

![house](https://github.com/LinkNLearn/homedata/blob/master/img/house.png?raw=true)

### Sensors

All sensors are a few inches away from the microprocessor to avoid picking up ambient heat. Sensors are all located at approximately waist level.

#### Upstairs & Basement

HTU21D - Digital Relative Humidity sensor with Temperature output

[HTU21D Datasheet](https://github.com/LinkNLearn/homedata/blob/master/sensor-datasheets/HTU21D.pdf?raw=true)

#### Main Floor (First Floor)

DHT22 - Capacitive-type humidity and temperature module/sensor

[DHT22 Datasheet](https://github.com/LinkNLearn/homedata/blob/master/sensor-datasheets/DHT22.pdf?raw=true)

* Power supply 3.3-6V DC
* Output signal digital signal via single-bus
* Sensing element Polymer capacitor
* Operating range humidity 0-100%RH; temperature -40~80Celsius
* Accuracy humidity +-2%RH(Max +-5%RH); temperature <+-0.5Celsius
* Resolution or sensitivity humidity 0.1%RH; temperature 0.1Celsius
* Repeatability humidity +-1%RH; temperature +-0.2Celsius
* Humidity hysteresis +-0.3%RH
* Long-term Stability +-0.5%RH/year
* Sensing period Average: 2s

CCS811 - Ultra-Low Power Digital Gas Sensor for Monitoring Indoor Air Quality

[CCS811 Datasheet](https://github.com/LinkNLearn/homedata/blob/master/sensor-datasheets/CCS811.pdf?raw=true)


#### Knee Wall (Attic)

Waterproof DS18B20 that records temperature only. It's mounted a few inches from the roof decking on the north side of the house.

[DS18B20 Datasheet](https://github.com/LinkNLearn/homedata/blob/master/sensor-datasheets/DS18B20.pdf?raw=true)

#### Notes from Homeowner on tVOC Measurements

VOC measures total volatile organic compounds (tVOC). CO2 is actually just eCO2 which is calculated based on H2 concentration, it is not a 'true' CO2 sensor for laboratory use. You can pretty much ignore the CO2 as it directly correlates to the tVOC measurement. This sensor requires a warm up period where it creates a baseline measurement. I've found that it's more of a relative measure since the sensor reestablishes a baseline at regular intervals. tVOC data should be ignored while warm_up is one (true).

tVOC spikes if we are cooking food, painting inside the house, spraying hair spray and other activities that generate VOCs. The sensor does not distinguish between harmful and non-harmful VOCs. It's more of an early indicator for potential problems. I would be interested to know if the AC unit being on (decreases in household temperature when it's warm outside) correlates to increases in tVOCs. The refrigerant used in AC units is a VOC that should be a closed system. You could probably use the VOC number to determine if we had people over (frequent door open / close events following by a steady increase in tVOC). The individual data points aren't as accurate as the temperature data but the trends over a period of hours should be relevant.

We painted our living room in the time period of data you have. That should show up as a multi-day increase in tVOC.

## Initial Data Exploration

The first thing we accomplished in terms of data analysis, was to simply look at the graph of the house temperature over time.
As we can clearly see below, there are some outlier temperatures well over 1000 degrees.

![early graph](https://github.com/LinkNLearn/homedata/blob/master/img/original_temp.png?raw=true)

Obviously these are anomalies as the house would have been burned into vapor at the temperatures shown in the above picture.  So, we need to clean these by eliminating these data points.

Further, this graph conflates both two different temperature sensors:

* "room_id":0
* "room_id":1

We need to separate these out into two different data streams.

## Looking Closer At Temperature Data After Separation

![Separated Room by IDs](https://github.com/LinkNLearn/homedata/blob/master/img/separatesensors.png?raw=true)

![Separated Room on Two Plots](https://github.com/LinkNLearn/homedata/blob/master/img/seperatedareas.png?raw=true)

# Adding Weather Dataset

## Hourly Averages

* We added weather data by looking at public datasets available online for areas nearby where the data was collected.
* We selected a weather station at the MSP airport, and then requested a CSV download of daily averages for the time period in question.

https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USW00014922/detail

## Averages By the Minute

* Minute station data can be accessed at this site:

https://www.ncdc.noaa.gov/data-access/land-based-station-data

* 1-Minute Data

ftp://ftp.ncdc.noaa.gov/pub/data/asos-onemin/

From the documentation:

DSI 6405 files (page one data): Each data file contains data for one station-month.
The files names for the page one data begin with 64050 (for data set name), followed
by the 4 character call letter identifier (e.g. KNYC = New York Central Park, NY),
the 4 digit year and two digit month. The file extensions are ".dat".
The format documentation for these files are available at

https://www1.ncdc.noaa.gov/pub/data/documentlibrary/tddoc/td6405.pdf

Weather Station Identifiers:

http://www.weathergraphics.com/identifiers/

ASOS Weather Station Identifiers

https://www.faa.gov/air_traffic/weather/asos/

MSP ASOS Data - KMSP

https://www.aviationweather.gov/metar/data?ids=KMSP&format=raw&date=0&hours=36

# Handling Timestamps

https://pythonprogramming.net/unix-time-matplotlib-tutorial/
