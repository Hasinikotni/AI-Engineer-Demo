# Web Data Extraction & Entity Resolution Pipeline

A modular Python-based pipeline for extracting structured information from webpages, identifying entities, resolving duplicate records, and generating structured JSON output.

## Overview

Web data is often unstructured and may contain duplicate or inconsistent information. This project automates the process of collecting webpage content, extracting useful information, identifying entities, and performing basic entity resolution and deduplication.

The pipeline processes multiple URLs in batch and stores the extracted results in JSON format for further analysis or processing.

## Key Features

- Webpage crawling and content collection
- Page title and text extraction
- Email and URL extraction
- Organization entity extraction
- Entity name normalization
- Similarity-based entity comparison
- Entity resolution
- Duplicate removal
- Batch processing of multiple webpages
- Structured JSON output
- Modular Python project architecture

## Project Workflow

Input URLs
    ↓
Web Crawling
    ↓
Data Extraction
    ↓
Data Cleaning
    ↓
Entity Extraction
    ↓
Entity Resolution
    ↓
Deduplication
    ↓
Structured JSON Output

## Project Structure

AI-Engineer-Demo/
│
├── data/
│   ├── urls.txt
│   ├── pages.json
│   └── entities.json
│
├── src/
│   ├── crawlers/
│   │   └── web_crawler.py
│   │
│   ├── extraction/
│   │   ├── extractor.py
│   │   ├── data_cleaner.py
│   │   └── entity_extractor.py
│   │
│   ├── resolution/
│   │   ├── resolver.py
│   │   └── deduplicator.py
│   │
│   ├── pipeline.py
│   └── batch_pipeline.py
│
├── tests/
├── .gitignore
└── README.md

## Input

Website URLs are provided through:

data/urls.txt

The pipeline reads the URLs and processes them one by one.

## Output

The pipeline generates structured JSON files inside the data/ directory.

### pages.json

Contains webpage-level information collected during crawling and extraction.

### entities.json

Contains extracted entity information associated with the processed webpages, including organizations, emails, and URLs.

## Entity Resolution

The entity resolution component normalizes entity names and compares them to identify records that may refer to the same entity.

This helps reduce duplicate entity records and produces cleaner structured data.

## How to Run

### 1. Create a virtual environment

python -m venv .venv

### 2. Activate the virtual environment

macOS/Linux:

source .venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the batch pipeline

python -m src.batch_pipeline

The processed results will be saved in:

data/pages.json
data/entities.json

## Example Output

Starting batch pipeline...
Total URLs: 3

Processing webpages...

UNIQUE TITLES

- Example Domain
- Welcome to Python.org
- Wikipedia

Batch pipeline completed successfully!

## Technologies Used

- Python
- Web Crawling
- Data Extraction
- Data Cleaning
- Entity Extraction
- Entity Resolution
- String Similarity
- Deduplication
- JSON
- Git
- GitHub

## Future Enhancements

- Improve entity matching using advanced NLP techniques
- Add entity similarity confidence scores
- Support larger-scale web crawling
- Add database storage for extracted entities
- Introduce parallel processing
- Expand automated testing
- Add logging and monitoring

## Author

Hasini Kotni

B.Tech – Computer Science & Engineering (AI)

GitHub: https://github.com/Hasinikotni
