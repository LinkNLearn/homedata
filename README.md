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

We created the following graphs within the plottemp.py file using the library matplotlib.

![Separated Room by IDs](https://github.com/LinkNLearn/homedata/blob/master/img/separatesensors.png?raw=true)

![Separated Room on Two Plots](https://github.com/LinkNLearn/homedata/blob/master/img/seperatedareas.png?raw=true)

# Deploying an App on Flask

One of the main goals of this project is to be able to deploy an app based off of data analysis and explore what that means.  In order to accomplish this, we're going to take the simplest route possible toward actually deploying said app on the web via a free hosting service which abstracts away the need to actually build and manage a server - called Heroku.

We're also going to use a Python-based library which allows us to quickly and easily create a web framework, known as Flask.  This will allow us to deploy a, "minimum viable product," and understand more about deployment.  Optionally we can also set up a deployment pipeline such that we can improve and modify the app over time and see what that looks like in, "production" on the web itself.

## Sketching Out & Designing The app

Below we have created a super simple sketch of what we think the app would look like and the various pieces involved.  This is a typical first step when designing an app - create a prototype on paper or on a whiteboard which describes the parts and pieces that you wish to build.

![App Sketch](https://raw.githubusercontent.com/LinkNLearn/homedata/master/img/appdraft.jpg)

## Visualizing the Data in html

We use a plugin known as mpld3.  This is basically an extension of our main graphing library, known as matplotlib.  Basically we spit the matplotlib object into a variable, and then mpld3 converts that variable into various possible formats, including:

* a string of html
* an html file, e.g. 'file.html'
* a json object, which can be used to create a plot via javascript plugins.
* an svg image, which can be displayed on a page

There are various trade off to the options above.  In using static files, we would hypothetically require less processing power and time and more storage as they would be stored as files on a particular machine to be later recalled, however they are not as instant in terms of what a particular user may be asking for at a given time.

From the [mpld3 FAQ](https://mpld3.github.io/faq.html) we see that mpld3 is only designed for datasets under a thousand points.  Hence, for our purposes this will be for demo only and to get our application up and running.

Now that we know more about how this particular app works, we may wish to change our drawing to better reflect the reality and limitations of the design itself.  For example, since we can only use 1000 data points at a time, we may only wish to show about 6 hour's worth of data from our temperature data set (assuming two sensors), which roughly equates to around 1000 data points.

Other larger dataset python projects include:

* https://bokeh.pydata.org/en/latest/
* http://vispy.org/


## Building the Flask app

We have placed an app within homedata/flask with links to documentation within the comments.

To run the flask app, navigate to that folder on your machine via your terminal, and do:

$ export FLASK_APP=hello.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/

 Visit https://127.0.0.1:5000/ to see the app being hosted on your browser.

 If you wish to debug, then use development mode as follows...

$ export FLASK_ENV=development
$ flask run

## Putting the Flask App Into Production

We have put an app into production at this endpoint:

https://homedataflask.herokuapp.com/

Building and placing the app into production is a complicated process, which deserves its own repo - so we started a new repo at https://github.com/LinkNLearn/homedataflask

Whereas the regular /LinkNLearn/homedata repo can be used for the actual empirical data science experiments and configuration, the /LinkNLearn/homedataflask repo can be used to put that practice into service.

Having built the app, we obtained a better understanding of what the actual architecture looks like and so can draw a better sketch:

![App Architecture](https://github.com/LinkNLearn/homedata/blob/master/img/homedataflask_arch.png?raw=true)


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
