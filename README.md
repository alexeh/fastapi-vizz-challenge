# Emissions Data Microservices

This application consists of two microservices that handle the import and export of emissions data. Both microservices are implemented in Python using the FastAPI framework.

## Importer Microservice

The importer microservice is responsible for parsing and storing emissions data from CSV files into a MongoDB database. The main functionality of the importer microservice is exposed through an endpoint that accepts a CSV file, processes it, and saves the parsed data into the MongoDB collection.

### Endpoint

- `/upload` (POST): Accepts a CSV file containing emissions data, parses the file, and stores the data into a MongoDB collection.

### CSV File Format

The CSV file should have the following columns:
- Country
- Sector
- Parent sector
- Years (1850, 1851, 1852, ...)

Example:


Country,Sector,Parent sector,1850,1851,1852,1853
ABW,Total including LULUCF,,0.0419,0.0441,0.0465,0.049
AFG,Total including LULUCF,,0.0803,0.0803,0.0803,0.0803


### Data Model

The data model used for storing the emissions data in MongoDB is defined in `models/emissions_model.py`. The model includes the following fields:
- `country`: The country code (string)
- `sector`: The sector name (string)
- `parentSector`: The parent sector name, if any (string, optional)
- `valuesPerYear`: A list of `Value` objects, each containing a year (integer) and the corresponding value (float)

### Setup and Usage

1. Ensure Python and MongoDB are installed on your system.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Start the FastAPI server using the command `uvicorn main:app --reload`.
4. Use a tool like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to send a POST request to `http://localhost:8000/upload` with a CSV file containing emissions data.

## Exporter Microservice

*To be documented.*