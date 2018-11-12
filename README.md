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

![house](https://github.com/LinkNLearn/homedata/img/house.png)

### Sensors

All sensors are a few inches away from the microprocessor to avoid picking up ambient heat. Sensors are all located at approximately waist level.

#### Upstairs & Basement

HTU21D

#### Main Floor

DHT22

#### Knee Wall (Attic)

Waterproof DS18B20 that records temperature only. It's mounted a few inches from the roof decking on the north side of the house.
