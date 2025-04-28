import os
import requests

# Base URL for downloading data
BASE_URL = "https://www.football-data.co.uk/mmz4281/{}/E0.csv"

# Directory to save the downloaded files
SAVE_DIR = "Data"

# Function to download data for a given season
def download_season_data(season_code, season_year):
    url = BASE_URL.format(season_code)
    response = requests.get(url)
    
    if response.status_code == 200:
        # Add the year range to the file name
        file_path = os.path.join(SAVE_DIR, f"Premier_League_{season_year}.csv")
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {file_path}")
    else:
        print(f"Failed to download data for season {season_year}. URL: {url}")

# Create directory if it doesn't exist
os.makedirs(SAVE_DIR, exist_ok=True)

# Seasons with their respective codes and years
seasons = [
    ("2425", "2024-2025"), ("2324", "2023-2024"), ("2223", "2022-2023"),
    ("2122", "2021-2022"), ("2021", "2020-2021"), ("1920", "2019-2020"),
    ("1819", "2018-2019"), ("1718", "2017-2018"), ("1617", "2016-2017"),
    ("1516", "2015-2016"), ("1415", "2014-2015"), ("1314", "2013-2014"),
    ("1213", "2012-2013"), ("1112", "2011-2012"), ("1011", "2010-2011"),
    ("0910", "2009-2010"), ("0809", "2008-2009"), ("0708", "2007-2008")
]

# Download data for each season
for season_code, season_year in seasons:
    download_season_data(season_code, season_year)
