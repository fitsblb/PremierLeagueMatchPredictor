import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_market_values(start_season, end_season):
    base_url = "https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1/saison_id/"
    market_values = {}

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    for season in range(start_season, end_season + 1):
        url = f"{base_url}{season}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table rows containing market value data
        rows = soup.select('table.items > tbody > tr')
        season_data = []

        for row in rows:
            try:
                club_name = row.select_one('td.hauptlink a').text.strip()
                total_market_value = row.select_one('td.rechts').text.strip()
                season_data.append((club_name, total_market_value))
            except AttributeError:
                continue

        market_values[season] = pd.DataFrame(season_data, columns=['Club', 'Total Market Value'])

    return market_values

# Scrape data from 2004/05 to 2024/25
data = scrape_market_values(2004, 2024)

# Print the results
for season, df in data.items():
    print(f"Season {season}:")
    print(df)

# Save the data to CSV files
for season, df in data.items():
    df.to_csv(f"premier_league_market_values_{season}.csv", index=False)
    print(f"Data for season {season} saved to CSV.")