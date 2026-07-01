import json

from langchain_core.documents import Document


DATA_PATH = "data/shl_product_catalog.json"


def load_catalog():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []

    for item in data:
        text = f"""
Name: {item.get('name')}
Description: {item.get('description')}
Job Levels: {item.get('job_levels')}
Duration: {item.get('duration')}
Remote: {item.get('remote')}
Adaptive: {item.get('adaptive')}
Keys: {item.get('keys')}
"""

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "name": item.get("name"),
                    "url": item.get("link"),
                    "entity_id": item.get("entity_id")
                }
            )
        )

    return documents