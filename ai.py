import ollama
import os

# list of all categories the AI can choose from
categories = [
    "frozen goods",
    "dairy",
    "meat",
    "produce",
    "breakfast foods",
    "bakery",
    "beverages",
    "snacks",
    "laundry and cleaning supplies",
    "miscellaneous"
]

OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3:latest")

def categorize(item):
    # ask ollama to categorize the item
    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": "You are a grocery categorizer. "
                           "Pick one category for this item: " + item + ". "
                           "Categories: frozen goods, dairy, meat, produce, breakfast foods, bakery, beverages, snacks, laundry and cleaning supplies, miscellaneous. "
                           "Reply with only the category name."
            }
        ]
    )

    # get the result and clean it up
    result = response.message.content.strip().lower()

    # if the result is not in our list, use miscellaneous
    if result not in categories:
        result = "miscellaneous"

    return result
