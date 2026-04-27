"""
Listaria - Intelligent Categorization Engine
Built by: YusufTari, Olga, Steven, Jet

This module provides keyword-based categorization for grocery items.
Improved algorithm with extensive keywords for better accuracy and reliability.

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

# Comprehensive keyword mappings for each category
# More keywords and better matching = more reliable categorization
category_keywords = {
    "frozen goods": [
        "frozen", "ice cream", "ice", "peas", "broccoli", "pizza", "burger", 
        "fries", "popsicle", "gelato", "ice pop", "frozen vegetable", "frozen meal",
        "frozen dinner", "frozen lasagna", "frozen pasta", "tilapia", "frozen fish",
        "frozen chicken", "frozen beef", "frozen shrimp", "frozen crab", "frozen mozzarella",
        "frozen mixture", "vegetables frozen", "spinach frozen"
    ],
    "dairy": [
        "milk", "cheese", "yogurt", "butter", "cream", "sour cream",
        "cottage cheese", "mozzarella", "cheddar", "parmesan", "ricotta",
        "feta", "lactose", "whipped cream", "greek yogurt", "string cheese",
        "swiss cheese", "american cheese", "provolone", "gouda", "brie",
        "cream cheese", "camembert", "muenster", "edam",
        "halloumi", "paneer", "mascarpone", "pudding",
        "custard", "whey", "milk powder", "condensed milk", "evaporated milk"
    ],
    "meat": [
        "chicken", "beef", "pork", "fish", "salmon", "tuna", "steak",
        "bacon", "ham", "sausage", "turkey", "lamb", "shrimp", "crab",
        "lobster", "ribeye", "ground beef", "chicken breast", "ground turkey",
        "ground pork", "ground lamb", "chuck", "sirloin", "filet",
        "t-bone", "porterhouse", "flank", "skirt", "brisket", "roast",
        "tenderloin", "loin", "chops", "cutlet", "escalope", "schnitzel",
        "meatball", "meat sauce", "beef jerky", "salami", "pepperoni",
        "prosciutto", "pancetta", "anchovy", "cod", "halibut", "trout",
        "catfish", "clam", "mussel", "oyster", "scallop", "squid", "octopus"
    ],
    "produce": [
        "apple", "banana", "carrot", "tomato", "lettuce", "broccoli",
        "spinach", "potato", "onion", "garlic", "pepper", "orange", "grape",
        "strawberry", "mango", "avocado", "cucumber", "celery", "kale",
        "zucchini", "squash", "beet", "cabbage", "cauliflower", "radish",
        "lime", "lemon", "coconut", "pineapple", "peach",
        "pear", "plum", "kiwi", "blueberry", "raspberry", "blackberry",
        "watermelon", "cantaloupe", "melon", "papaya", "guava", "pomegranate",
        "cherry", "date", "fig", "raisin", "prune", "dried fruit",
        "artichoke", "asparagus", "bean sprout", "brussels sprout", "chard",
        "collard", "endive", "escarole", "radicchio", "parsnip", "turnip",
        "rutabaga", "kohlrabi", "okra", "eggplant", "corn", "mushroom",
        "sun-dried tomato", "vegetable", "greens", "mixed greens"
    ],
    "breakfast foods": [
        "cereal", "oatmeal", "eggs", "bacon", "toast", "pancake", "waffle",
        "granola", "muesli", "french toast", "hash brown", "egg", "scrambled",
        "omelet", "sausage", "breakfast", "sausage patty", "sausage link",
        "english muffin", "crumpet", "scone", "biscuit", "jam", "jelly",
        "peanut butter", "honey", "maple syrup", "powdered sugar"
    ],
    "bakery": [
        "bread", "croissant", "cake", "donut", "pastry", "bagel", "muffin",
        "cookie", "brownie", "baguette", "bun", "roll", "rye", "sourdough",
        "flatbread", "pita", "naan", "tortilla", "focaccia", "ciabatta",
        "pumpernickel", "multigrain", "whole wheat", "white bread", "rye bread",
        "french bread", "italian bread", "english muffin", "crumpet", "scone",
        "danish", "turnover", "pie", "tart", "biscotti", "shortbread",
        "gingerbread", "cupcake", "cheesecake", "tiramisu", "mousse", "dessert",
        "eclair", "choux", "cream puff", "doughnut"
    ],
    "beverages": [
        "juice", "coffee", "tea", "water", "cola", "soda", "milk", "beer",
        "wine", "soda pop", "energy drink", "smoothie", "iced tea",
        "lemonade", "punch", "kombucha", "espresso", "latte", "cappuccino",
        "mocha", "macchiato", "americano", "iced coffee", "cold brew",
        "herbal tea", "green tea", "black tea", "white tea", "oolong",
        "sparkling water", "tonic water", "ginger ale", "root beer",
        "orange juice", "apple juice", "cranberry juice", "grape juice",
        "tomato juice", "lemon juice", "lime juice", "coconut water",
        "almond milk", "soy milk", "oat milk", "rice milk", "coconut milk",
        "vodka", "whiskey", "rum", "gin", "tequila", "brandy", "sake",
        "champagne", "sparkling wine", "cider", "mead", "liqueur"
    ],
    "snacks": [
        "chips", "cookie", "candy", "popcorn", "nuts", "granola bar",
        "pretzel", "crackers", "cheeto", "doritos", "pringles", "trail mix",
        "beef jerky", "gummy", "gummy bear", "licorice", "chocolate",
        "peanut", "almond", "cashew", "walnut", "pistachio", "pecan",
        "sunflower seed", "pumpkin seed", "sesame seed", "flax seed",
        "mixed nuts", "roasted nuts", "salted nuts", "honey roasted",
        "flavored popcorn", "caramel popcorn", "cheese popcorn", "butter popcorn",
        "animal cracker", "graham cracker", "rice cracker", "tortilla chip",
        "corn chip", "pita chip", "vegetable chip", "fruit chip",
        "protein bar", "cereal bar", "breakfast bar", "energy bar",
        "fruit snack", "fruit roll", "fruit leather", "dried fruit",
        "jerky", "pork jerky", "turkey jerky", "salmon jerky"
    ],
    "laundry and cleaning supplies": [
        "soap", "detergent", "bleach", "shampoo", "conditioner", "dish soap",
        "laundry detergent", "cleaning", "wipes", "spray", "paper towels",
        "sponge", "broom", "mop", "vacuum", "duster", "sanitizer",
        "disinfectant", "antibacterial", "laundry stain remover", "fabric softener",
        "dryer sheet", "washing machine cleaner", "drain cleaner", "toilet cleaner",
        "bathroom cleaner", "kitchen cleaner", "floor cleaner", "glass cleaner",
        "polish", "furniture polish", "wood cleaner", "carpet cleaner",
        "air freshener", "odor eliminator", "deodorant", "body wash",
        "face wash", "body lotion", "hand cream", "lip balm",
        "toothpaste", "toothbrush", "mouthwash", "dental floss",
        "tissue", "napkin", "paper", "aluminum foil", "plastic wrap",
        "trash bag", "recycling bag", "compost bag", "storage bag",
        "gloves", "apron", "towel", "cloth", "rag", "scrub brush"
    ]
}


def categorize(item):
    """
    Categorize a grocery item based on improved keyword matching.
    Uses scoring to handle items with multiple keywords more reliably.
    
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
    if not item or not isinstance(item, str):
        return "miscellaneous"
    
    item_lower = item.lower().strip()
    
    # Score each category based on keyword matches
    # Longer keyword matches get higher scores (more specific matches)
    category_scores = {cat: 0 for cat in categories}
    
    for category, keywords in category_keywords.items():
        for keyword in keywords:
            # Check if keyword is in the item (substring matching)
            if keyword.lower() in item_lower:
                # Higher score for longer keyword matches (more specific)
                category_scores[category] += len(keyword)
    
    # Find category with highest score
    best_category = None
    best_score = 0
    
    for category, score in category_scores.items():
        if score > best_score:
            best_score = score
            best_category = category
    
    # Return best match if found, otherwise miscellaneous
    return best_category if best_category else "miscellaneous"

