import re


def clean_text(text):
    if not text:
        return ""

    # Replace multiple spaces/newlines with one space
    text = re.sub(r"\s+", " ", text)

    # Remove leading and trailing spaces
    text = text.strip()

    return text


def clean_page_data(page_data):
    return {
        "title": clean_text(page_data.get("title", "")),
        "description": clean_text(page_data.get("description", "")),
        "text": clean_text(page_data.get("text", ""))
    }


if __name__ == "__main__":
    sample_data = {
        "title": "   Example    Website   ",
        "description": "This is   a test description.",
        "text": "Hello\n\n\nWorld     of   AI"
    }

    cleaned = clean_page_data(sample_data)

    print("Cleaned data:")
    print(cleaned)