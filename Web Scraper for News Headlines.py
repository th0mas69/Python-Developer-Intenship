import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the HTML contents
url = 'https://www.bbc.com/news'
response = requests.get(url)
html = response.text

# Step 2: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Step 3: Extract <h2> and <title> tags
headlines = []

# Extract from <title>
page_title = soup.title.string.strip() if soup.title else 'No Title Found'
headlines.append(page_title)

# Extract from <h2>
for h2 in soup.find_all('h2'):
    text = h2.get_text(strip=True)
    if text:
        headlines.append(text)

# Step 4: Save headlines to a .txt file
with open('headlines.txt', 'w', encoding='utf-8') as file:
    for line in headlines:
        file.write(line + '\n')

print(f"Saved {len(headlines)} headlines to 'headlines.txt'")
