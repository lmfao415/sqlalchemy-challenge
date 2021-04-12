# sqlalchemy-challenge

This repository uses SQLAlchemy ORM queries, Pandas, and Matplotlib to explore and analyze the [Hawaii weather](https://github.com/lmfao415/sqlalchemy-challenge/blob/main/Resources/hawaii.sqlite) sqlite database.

The [climate_starter](https://github.com/lmfao415/sqlalchemy-challenge/blob/main/climate_starter.ipynb) Jupyter Notebook contains the queries and plots for this project. 
Using SQLalchemy, the database is queried and then Pandas used to organize and then plot the daily precipitation values:

![q](https://github.com/lmfao415/sqlalchemy-challenge/blob/main/Resources/query.png?raw=true)
![sample](https://github.com/lmfao415/sqlalchemy-challenge/blob/main/Resources/precp.png?raw=true)

Querying is further used to return a histogram of recorded temperatures from the most active weather station:

![sample](https://github.com/lmfao415/sqlalchemy-challenge/blob/main/Resources/tempfreq.png)

More plots and analysis are also included in the Notebook based on temperature and rainfall amounts over specified periods of time.

This project also includes a created **flask app** [app.py](https://github.com/lmfao415/sqlalchemy-challenge/blob/main/app.py) file featuring the following routes that return queried information from the dataset:

* `/`

  * Home page.

  * Lists all routes that are available.

* `/api/v1.0/precipitation`

  * Converts the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Returns the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Queries the dates and temperature observations of the most active station for the last year of data.
  
  * Returns a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculates `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculates the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
  
 For instance, here is an example of the /station route:
 
 ![app](https://github.com/lmfao415/sqlalchemy-challenge/blob/main/Resources/app2.png?raw=true)
 
 With the returned values:
 
 ![app](https://github.com/lmfao415/sqlalchemy-challenge/blob/main/Resources/app.png?raw=true)
