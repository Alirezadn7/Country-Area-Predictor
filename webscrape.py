import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://www.scrapethissite.com/pages/simple/"

r = requests.get(url, timeout=30)
r.raise_for_status()
soup = BeautifulSoup(r.text , 'html.parser')

countries = soup.find_all('div', class_='country')

data = []

for c in countries:
    country_name = c.find('h3' , class_='country-name').get_text(strip=True)
    population = int(c.find('span' , class_='country-population').get_text(strip=True))
    area = float(c.find('span' , class_='country-area').get_text(strip=True))

    data.append({
        'country' :country_name,
        'population': population,
        'area': area
    })

for d in data:
    print(d)

conn = sqlite3.connect('country.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
    country TEXT,
    population INTEGER,
    area REAL
)''')

for d in data:
    sql = 'INSERT INTO countries(country , population , area) VALUES (? , ? , ?)'
    values = (d['country'] , d['population'] , d['area'])
    cursor.execute(sql , values)

conn.commit()
cursor.close()
conn.close()

