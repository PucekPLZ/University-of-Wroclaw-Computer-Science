import re
import urllib.request
from bs4 import BeautifulSoup
import threading
import queue

def worker(shared_queue, distance, action, results):
    visited = set()

    while True:
        item = shared_queue.get()
        if item is None:
            break

        current_page, current_distance = item

        if current_page not in visited:
            try:
                with urllib.request.urlopen(current_page) as response:
                    page_content = response.read().decode('utf-8')

                soup = BeautifulSoup(page_content, 'html.parser')
                cleaned_content = soup.get_text().replace('\n', "")

                result = action(cleaned_content)

                results[(action, cleaned_content)] = (current_page, result)

                visited.add(current_page)

                if current_distance < distance:
                    links = [link.get('href') for link in soup.find_all('a')]
                    for link in links:
                        shared_queue.put((link, current_distance + 1))

            except Exception as e:
                print(f"Error processing {current_page}: {e}")
            
def crawl(start_page, distance, action):
    results = {}
    shared_queue = queue.Queue()
    shared_queue.put((start_page, 0))

    threads = [threading.Thread(target=worker, args=(shared_queue, distance, action, results)) for _ in range(4)]

    [t.start() for t in threads]
    [shared_queue.put(None) for t in range(4)]
    [t.join() for t in threads]

    print(results)

crawl("http://www.ii.uni.wroc.pl", 1, lambda text: re.findall(r"([^.]*?Python[^.]*\.)", text))