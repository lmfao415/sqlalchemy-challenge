# sqlalchemy-challenge

This repository uses SQLAlchemy ORM queries, Pandas, and Matplotlib to explore and analyze the [Hawaii weather](https://github.com/lmfao415/sqlalchemy-challenge/blob/main/Resources/hawaii.sqlite) sqlite database.

Using SQLalchemy, the database is queried and then Pandas used to organize and then plot the daily precipitation values:

![q](https://github.com/lmfao415/sqlalchemy-challenge/blob/main/Resources/query.png?raw=true)
![sample](https://github.com/lmfao415/sqlalchemy-challenge/blob/main/Resources/precp.png?raw=true)

Querying is further used to return the most active weather station and a histogram of recorder temperatures plotted:

![sample](https://github.com/lmfao415/sqlalchemy-challenge/blob/main/Resources/tempfreq.png)


This project also includes a created flask app featuring the following routes:

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.
  
  * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
