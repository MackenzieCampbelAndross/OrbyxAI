from urls import urls
import requests
from bs4 import BeautifulSoup
import nltk
nltk.download("punkt")
headers = {"User-Agent": "Mozilla/5.0"}
all_paragraphs = []
for url in urls:
    print(f"Scraping: {url}")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, "lxml")
        paragraphs = soup.find_all("p")
        all_paragraphs.extend(p.get_text(strip=True) for p in paragraphs)
    except Exception as e:
        print(f"Error scraping {url}: {e}")

content = "\n\n".join(all_paragraphs)

if not content.strip():
    print("No content scraped. Exiting.")
    exit()

with open("knowledge_base.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("Scraping complete. Data saved to 'knowledge_base.txt'")
