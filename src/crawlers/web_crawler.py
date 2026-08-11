import json
import os
import requests

from src.extraction.extractor import extract_page_data


def crawl_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    return extract_page_data(response.text)


def save_page_data(url, page_data):
    os.makedirs("data", exist_ok=True)

    file_path = "data/pages.json"

    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                data = {}

        except json.JSONDecodeError:
            data = {}
    else:
        data = {}

    data[url] = page_data

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved to data/pages.json")