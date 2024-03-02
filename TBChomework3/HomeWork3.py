import threading
import requests
import json


def make_request(url, filename):
    response = requests.get(url)
    data = response.json()
    with open("Products.json", 'a') as f:
        json.dump(data, f)
        f.write('\n')
    print(f"Response from {url} added")


base_URL = "https://dummyjson.com/products/"
product_URLs = [f"{base_URL}{i}" for i in range(1, 101)]

threads = []

for url in product_URLs:
    thread = threading.Thread(target=make_request, args=(url, "products.json"))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("All requests completed")