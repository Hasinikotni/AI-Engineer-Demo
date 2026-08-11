import json

from src.resolution.resolver import is_same_entity


def remove_duplicates(names):
    unique_names = []

    for name in names:
        duplicate = False

        for existing_name in unique_names:
            if is_same_entity(name, existing_name):
                duplicate = True
                break

        if not duplicate:
            unique_names.append(name)

    return unique_names


def load_page_data():
    with open("data/pages.json", "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":

    pages = load_page_data()

    titles = [page["title"] for page in pages if page["title"]]

    unique_titles = remove_duplicates(titles)

    print("Titles found:")
    for title in titles:
        print("-", title)

    print("\nUnique titles:")
    for title in unique_titles:
        print("-", title)