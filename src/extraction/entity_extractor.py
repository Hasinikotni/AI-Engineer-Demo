import re
import spacy
from bs4 import BeautifulSoup

# Load English NLP model
nlp = spacy.load("en_core_web_sm")


def clean_entity(name):
    """Clean unnecessary spaces and punctuation."""

    name = re.sub(r"\s+", " ", name)

    return name.strip(" ,.;:!?-_\"'")


def is_valid_entity(name):
    """Remove obviously invalid NLP predictions."""

    if len(name) < 3:
        return False

    # Avoid very long noisy predictions
    if len(name.split()) > 5:
        return False

    # Must contain letters
    if not re.search(r"[A-Za-z]", name):
        return False

    return True


def extract_entities(text, html=""):

    # =====================================================
    # 1. EMAIL EXTRACTION
    # =====================================================

    email_source = text + " " + html

    emails = re.findall(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        email_source
    )

    emails = list(dict.fromkeys(emails))


    # =====================================================
    # 2. URL EXTRACTION FROM TEXT
    # =====================================================

    text_urls = re.findall(
        r'https?://[^\s<>"\']+',
        text
    )


    # =====================================================
    # 3. URL EXTRACTION FROM HTML
    # =====================================================

    html_urls = []

    if html:

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        for link in soup.find_all("a", href=True):

            href = link.get("href", "").strip()

            if href.startswith(("http://", "https://")):

                html_urls.append(href)


    # Remove duplicates
    urls = list(
        dict.fromkeys(
            text_urls + html_urls
        )
    )


    # =====================================================
    # 4. NLP ENTITY EXTRACTION
    # =====================================================

    doc = nlp(text)

    organizations = []
    locations = []


    for entity in doc.ents:

        name = clean_entity(entity.text)

        if not is_valid_entity(name):
            continue


        # ---------------------------------------------
        # ORGANIZATIONS
        # ---------------------------------------------

        if entity.label_ == "ORG":

            if name not in organizations:

                organizations.append(name)


        # ---------------------------------------------
        # LOCATIONS
        # ---------------------------------------------

        elif entity.label_ in ["GPE", "LOC"]:

            if name not in locations:

                locations.append(name)


    # =====================================================
    # 5. REMOVE OBVIOUS NLP NOISE
    # =====================================================

    # These are common words that spaCy may incorrectly
    # classify as organizations on webpages.

    organization_noise = {
        "JavaScript",
        "Java",
        "Python",
        "Apple",
        "APPLE",
        "IRC",
        "Guide FAQ Non-English Docs PEP",
        "Intuitive Interpretation Calculations",
        "Quick Easy",
        "Learn Experienced",
        "Beginner Guide Download Python",
        "Latest News",
        "SEO",
        "AI",
        "Software",
        "Machine Learning",
        "Scientific",
        "Tracker",
        "List",
        "Input",
        "Banana",
        "PyQt",
        "PySide",
        "Kivy",
        "Buildbot",
        "Trac"
    }

    organizations = [
        org for org in organizations
        if org not in organization_noise
    ]


    # Remove duplicate locations
    locations = list(dict.fromkeys(locations))


    return {

        "emails": emails,

        "urls": urls,

        "organizations": organizations,

        "locations": locations

    }