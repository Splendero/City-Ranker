import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.numbeo.com/cost-of-living/region_rankings_current.jsp?region=021"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table
table = soup.find('table', {'id': 't2'})

# Extract headers
headers = [th.text.strip() for th in table.find('thead').find_all('th')]

# Extract rows
rows = []
for row in table.find('tbody').find_all('tr'):
    cols = row.find_all('td')
    rows.append([col.text.strip() for col in cols])

# Save to CSV
with open('numbeo_cost_of_living.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print("Data saved to numbeo_cost_of_living.csv")