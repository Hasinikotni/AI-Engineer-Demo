import re


def extract_entities(text):

    # Extract email addresses
    emails = re.findall(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        text
    )

    # Extract URLs
    urls = re.findall(
        r'https?://[^\s<>"\']+',
        text
    )

    # Extract organization names
    organization_patterns = [
        r'\b[A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)*\s+(?:Inc\.?|Corporation|Corp\.?|LLC|Ltd\.?|Foundation)\b',
    ]

    organizations = []

    for pattern in organization_patterns:
        matches = re.findall(pattern, text)

        for match in matches:
            match = match.strip()

            if match not in organizations:
                organizations.append(match)

    return {
        "emails": emails,
        "urls": urls,
        "organizations": organizations
    }