import re
import urllib.request
from bs4 import BeautifulSoup

def crawl(start_page, distance, action):
    visited = set()
    queue = [(start_page, 0)]

    while queue:
        current_page, current_distance = queue.pop(0)

        if current_page not in visited:
            try:
                with urllib.request.urlopen(current_page) as response:
                    page_content = response.read().decode('utf-8')
                
                soup = BeautifulSoup(page_content, 'html.parser')
                cleaned_content = soup.get_text()

                result = action(cleaned_content.replace('\n', ""))

                yield (current_page, result)

                visited.add(current_page)

                if current_distance < distance:
                    links = [link.get('href') for link in soup.find_all('a')]
                    queue.extend((link, current_distance + 1) for link in links)

            except Exception as e:
                print(f"Error processing {current_page}: {e}")
                # continue

for url, result in crawl("http://www.ii.uni.wroc.pl", 1, lambda text: re.findall(r"([^.]*?Python[^.]*\.)", text)):
    if result != []:
        print(f"{url}: {result}")        