"""
GrocerySort - Intelligent Categorization Engine

This module provides keyword-based categorization for grocery items.
It matches items against predefined keywords to determine their category.

Categories:
- frozen goods: Ice cream, frozen vegetables, etc.
- dairy: Milk, cheese, yogurt, etc.
- meat: Chicken, beef, pork, fish, etc.
- produce: Fresh fruits, vegetables, etc.
- breakfast foods: Cereal, eggs, toast, etc.
- bakery: Bread, croissants, cakes, etc.
- beverages: Juice, coffee, tea, soda, etc.
- snacks: Chips, cookies, candy, etc.
- laundry and cleaning supplies: Soap, detergent, etc.
- miscellaneous: Everything else
"""

# List of all categories
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

# Keyword mappings for each category
# Each keyword is checked against the item name (case-insensitive)
category_keywords = {
    "frozen goods": [
        "frozen", "ice cream", "ice", "peas", "broccoli", "frozen pizza",
        "frozen burger", "frozen fries", "popsicle", "gelato"
    ],
    "dairy": [
        "milk", "cheese", "yogurt", "butter", "cream", "sour cream",
        "cottage cheese", "mozzarella", "cheddar", "parmesan", "ricotta",
        "feta", "lactose"
    ],
    "meat": [
        "chicken", "beef", "pork", "fish", "salmon", "tuna", "steak",
        "bacon", "ham", "sausage", "turkey", "lamb", "shrimp", "crab",
        "lobster", "ribeye", "ground beef", "chicken breast"
    ],
    "produce": [
        "apple", "banana", "carrot", "tomato", "lettuce", "broccoli",
        "spinach", "potato", "onion", "garlic", "pepper", "orange", "grape",
        "strawberry", "mango", "avocado", "cucumber", "celery", "kale",
        "zucchini", "squash", "beet", "cabbage", "cauliflower", "radish"
    ],
    "breakfast foods": [
        "cereal", "oatmeal", "eggs", "bacon", "toast", "pancake", "waffle",
        "granola", "muesli", "French toast", "hash brown"
    ],
    "bakery": [
        "bread", "croissant", "cake", "donut", "pastry", "bagel", "muffin",
        "cookie", "brownie", "baguette", "bun", "roll", "rye", "sourdough"
    ],
    "beverages": [
        "juice", "coffee", "tea", "water", "cola", "soda", "milk", "beer",
        "wine", "soda pop", "energy drink", "smoothie", "iced tea",
        "lemonade", "punch", "kombucha", "espresso"
    ],
    "snacks": [
        "chips", "cookie", "candy", "popcorn", "nuts", "granola bar",
        "pretzel", "crackers", "cheeto", "doritos", "pringles", "trail mix",
        "beef jerky", "gummy"
    ],
    "laundry and cleaning supplies": [
        "soap", "detergent", "bleach", "shampoo", "conditioner", "dish soap",
        "laundry detergent", "cleaning", "wipes", "spray", "paper towels",
        "sponge", "broom", "mop", "vacuum", "duster", "sanitizer"
    ]
}


def categorize(item):
    """
    Categorize a grocery item based on keyword matching.
    
    Args:
        item (str): The item name to categorize
        
    Returns:
        str: The category name (or 'miscellaneous' if no match found)
        
    Examples:
        >>> categorize("milk")
        'dairy'
        >>> categorize("chicken breast")
        'meat'
        >>> categorize("random item")
        'miscellaneous'
    """
    item_lower = item.lower()
    
    # Check each category's keywords
    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword in item_lower:
                return category
    
    # If no match found, return miscellaneous
    return "miscellaneous"

