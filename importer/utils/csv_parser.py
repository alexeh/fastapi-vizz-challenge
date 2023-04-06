import csv
from typing import List

from models.emissions_model import Sector, Value

def parse_csv_file(file_path: str) -> List[Sector]:
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        sectors = []
        # create empty list to store year-value pairs
        for row in reader:
            values_per_year = []
            for key in row:
                if key.isnumeric():  # check if key is a year
                    year = int(key)
                    value = float(row[key])
                    values_per_year.append(Value(year=year, value=value))
            sector_data = Sector(country=row['Country'], sector=row['Sector'], parentSector=row['Parent sector'], valuesPerYear=values_per_year)
            sectors.append(sector_data.dict())
        return sectors

