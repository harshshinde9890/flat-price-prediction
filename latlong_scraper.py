import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL for Google Search
BASE_URL = "https://www.google.com/search?q="

# Headers to simulate a real browser visit
HEADERS = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

# Function to scrape latitude and longitude
def get_coordinates(sector):
    search_term = f"sector {sector} gurgaon longitude & latitude"
    url = BASE_URL + search_term.replace(" ", "+")  # URL encode spaces

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        coordinates_div = soup.find("div", class_="Z0LcW t2b5Cf")
        if coordinates_div:
            return coordinates_div.text.strip()
    return None

# Store results in a list
rows = []

# Iterate over sectors and fetch coordinates
for sector in range(1, 116):
    coordinates = get_coordinates(sector)
    rows.append({"Sector": f"Sector {sector}", "Coordinates": coordinates})


# Convert to DataFrame
df = pd.DataFrame(rows)

# Save to CSV
df.to_csv("gurgaon_sectors_coordinates.csv", index=False)
