# SQLAlchemy Homework - Surfs Up!

## Climate-Analysis_SQLAlchemy_Challenge

This challenge requires a climate analysis to help plan a trip to Honolulu, Hawaii.

## Climate Analysis and Exploration
Performed a basic climate analysis and data exploration of the climate databse using Python and SQLAlchemy in a [Jupyter Notebook](https://github.com/SusanCThomas/Climate-Analysis_SQLAlchemy_Challenge/blob/main/climate_starter.ipynb). All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib:

* Used the provided starter notebook and [hawaii.sqlite](https://github.com/SusanCThomas/Climate-Analysis_SQLAlchemy_Challenge/tree/main/Resources) files to complete climate analysis and data exploration

* Chose a start date and end date for the trip. Made sure that the vacation range is approximately 3-15 days total

* Used SQLAlchemy `create_engine` to connect to the sqlite database

* Used SQLAlchemy `automap_base()` to reflect the tables into classes and saved a reference to those classes called `Station` and `Measurement`

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data

* Selected only the `date` and `prcp` values

* Loaded the query results into a Pandas DataFrame and set the index to the date column

* Sorted the DataFrame values by `date`

* [Plotted](https://github.com/SusanCThomas/Climate-Analysis_SQLAlchemy_Challenge/blob/main/Images/12_Months_Precip.png) the results using the DataFrame `plot` method.


* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designed a query to calculate the total number of stations

* Designed a query to find the most active stations

* Listed the stations and observation counts in descending order

* Determined which station had the highest number of observations

* Designed a query to retrieve the last 12 months of temperature observation data (TOBS)

* Filtered by the station with the highest number of observations

* [Plotted](https://github.com/SusanCThomas/Climate-Analysis_SQLAlchemy_Challenge/blob/main/Images/temp_observe.png)the results as a histogram with `bins=12`

## Climate App - Flask API
Designed a [Flask API](https://github.com/SusanCThomas/Climate-Analysis_SQLAlchemy_Challenge/blob/main/climate.py) based on the queries that were just developed. 

Created Routes using Flask:
* /
    * Home Page
    * Listed all routes available
    
* /api/v1.0/precipitation
    * Converted the query results to a dictionary using the date as the key and prcp as the value
    * Returned the JSON representation of the dictionary
    
* /api/v1.0/stations
    * Return a JSON list of stations from the dataset.
    
* /api/v1.0/tobs
    * Query the dates and temperature observations of the most active station for the last year of data.
    * Return a JSON list of temperature observations (TOBS) for the previous year.

## Bonus Analysis

### Temperature Analysis 

* The [starter notebook](https://github.com/SusanCThomas/Climate-Analysis_SQLAlchemy_Challenge/blob/main/climate_starter.ipynb) contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will returned the minimum, average, and maximum temperatures for that range of dates. Calculated the min, avg, and max temperatures for the trip using the matching dates from the previous year.

* [Plotted](https://github.com/SusanCThomas/Climate-Analysis_SQLAlchemy_Challenge/blob/main/Images/avg_trip_temp.png) the min, avg, and max temperature from your previous query as a bar chart

### Daily Rainfall Average

* Calculated the rainfall per weather station using the previous year's matching dates

* Calculated the daily normals. Normals are the averages for the min, avg, and max temperatures.

* Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date

* Used Pandas to plot an [area plot](https://github.com/SusanCThomas/Climate-Analysis_SQLAlchemy_Challenge/blob/main/Images/daily_normals.png) (`stacked=False`) for the daily normals.
