# SQLAlchemy Homework - Surfs Up!

## Climate-Analysis_SQLAlchemy_Challenge

This challenge requires a climate analysis to help plan a trip to Honolulu, Hawaii.

## Climate Analysis and Exploration
Performed a basic climate analysis and data exploration of the climate databse using Python and SQLAlchemy in a [Jupyter Notebook](https://github.com/SusanCThomas/Climate-Analysis_SQLAlchemy_Challenge/blob/main/climate_starter.ipynb). All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib:

* Used the provided starter notebook and hawaii.sqlite files to complete climate analysis and data exploration

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
