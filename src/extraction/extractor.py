from bs4 import BeautifulSoup


def extract_page_data(html):
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.get_text(strip=True) if soup.title else ""

    description_tag = soup.find("meta", attrs={"name": "description"})
    description = (
        description_tag.get("content", "").strip()
        if description_tag
        else ""
    )

    text = soup.get_text(" ", strip=True)

    return {
        "title": title,
        "description": description,
        "text": text
    }