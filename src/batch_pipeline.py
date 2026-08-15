import json
import os

from src.crawlers.web_crawler import crawl_page, save_page_data
from src.extraction.entity_extractor import extract_entities
from src.resolution.deduplicator import remove_duplicates


def run_batch():

    with open("data/urls.txt", "r") as file:
        urls = [line.strip() for line in file if line.strip()]

    all_titles = []
    all_results = []

    print("\nStarting batch pipeline...")
    print("Total URLs:", len(urls))

    for url in urls:

        print("\n" + "=" * 50)
        print("Processing:", url)

        try:
            page_data = crawl_page(url)

            save_page_data(url, page_data)

            entities = extract_entities(
                   page_data["text"],
                   page_data["html"]
)

            print("Title:", page_data["title"])
            print("Emails:", entities["emails"])
            print("URLs:", entities["urls"])
            print("Organizations:", entities["organizations"])

            all_titles.append(page_data["title"])

            all_results.append({
                "url": url,
                "title": page_data["title"],
                "emails": entities["emails"],
                "urls": entities["urls"],
                "organizations": entities["organizations"]
            })

        except Exception as e:
            print("Error:", e)

    # Save extracted entities
    os.makedirs("data", exist_ok=True)

    with open("data/entities.json", "w") as file:
        json.dump(all_results, file, indent=4)

    print("\nEntity data saved to data/entities.json")

    # Remove duplicate titles
    unique_titles = remove_duplicates(all_titles)

    print("\nUNIQUE TITLES")

    for title in unique_titles:
        print("-", title)

    print("\nBatch pipeline completed successfully!")


if __name__ == "__main__":
    run_batch()