from src.crawlers.web_crawler import crawl_page, save_page_data
from src.resolution.deduplicator import remove_duplicates
from src.extraction.entity_extractor import extract_entities


def run_pipeline(url):
    print("\nStarting pipeline...")
    print("URL:", url)

    page_data = crawl_page(url)
    print("✓ Website crawled")

    save_page_data(url, page_data)
    print("✓ Data extracted and saved")

    print("\nExtracted data:")
    print("Title:", page_data["title"])
    print("Description:", page_data["description"])

    entities = extract_entities(page_data["text"])

    print("\nExtracted entities:")
    print("Emails:", entities["emails"])
    print("URLs:", entities["urls"])
    print("Organizations:", entities["organizations"])

    unique_titles = remove_duplicates([page_data["title"]])

    print("\nUnique titles:")
    for title in unique_titles:
        print("-", title)

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    url = input("Enter website URL: ")
    run_pipeline(url)