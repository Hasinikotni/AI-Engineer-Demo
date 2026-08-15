from bs4 import BeautifulSoup


def extract_page_data(html):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )


    # =========================================
    # PAGE TITLE
    # =========================================

    title = ""

    if soup.title:

        title = soup.title.get_text(
            strip=True
        )


    # =========================================
    # META DESCRIPTION
    # =========================================

    description_tag = soup.find(
        "meta",
        attrs={
            "name": "description"
        }
    )

    description = ""

    if description_tag:

        description = description_tag.get(
            "content",
            ""
        ).strip()


    # =========================================
    # REMOVE UNNECESSARY HTML
    # =========================================

    for element in soup(
        [
            "script",
            "style",
            "noscript"
        ]
    ):

        element.decompose()


    # =========================================
    # EXTRACT CLEAN TEXT
    # =========================================

    text = soup.get_text(
        " ",
        strip=True
    )


    # =========================================
    # RETURN DATA
    # =========================================

    return {

        "title": title,

        "description": description,

        "text": text,

        "html": html

    }