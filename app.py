from flask import Flask, render_template, request

from src.crawlers.web_crawler import crawl_page
from src.extraction.entity_extractor import extract_entities
from src.resolution.deduplicator import remove_duplicates


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        url = request.form.get("url", "").strip()

        if not url:
            error = "Please enter a website URL."

        else:

            # Add https:// automatically if missing
            if not url.startswith(("http://", "https://")):
                url = "https://" + url

            try:

                # -----------------------------
                # Crawl website
                # -----------------------------

                page_data = crawl_page(url)

                # -----------------------------
                # Extract entities
                # -----------------------------

                entities = extract_entities(
                    page_data.get("text", ""),
                    page_data.get("html", "")
                )

                # -----------------------------
                # Unique page title
                # -----------------------------

                unique_titles = remove_duplicates(
                    [page_data.get("title", "")]
                )

                # -----------------------------
                # Final result
                # -----------------------------

                result = {

                    "url": url,

                    "title": page_data.get(
                        "title",
                        ""
                    ),

                    "description": page_data.get(
                        "description",
                        ""
                    ),

                    "emails": entities.get(
                        "emails",
                        []
                    ),

                    "urls": entities.get(
                        "urls",
                        []
                    ),

                    "organizations": entities.get(
                        "organizations",
                        []
                    ),

                    "locations": entities.get(
                        "locations",
                        []
                    ),

                    "unique_titles": unique_titles,

                    "text": page_data.get(
                        "text",
                        ""
                    )
                }

            except Exception as e:

                error = f"Unable to analyze website: {str(e)}"


    return render_template(
        "index.html",
        result=result,
        error=error
    )


# =========================================
# START FLASK APPLICATION
# =========================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=8000
    )