/**
 * Icons for each category - helps users identify categories at a glance
 */
const categoryIcons = {
    "frozen goods": "❄️",
    "dairy": "🧀",
    "meat": "🥩",
    "produce": "🌾",
    "breakfast foods": "🍳",
    "bakery": "🥐",
    "beverages": "🥤",
    "snacks": "🍿",
    "laundry and cleaning supplies": "🧺",
    "miscellaneous": "📦"
};

/**
 * Get items from localStorage
 */
const items = JSON.parse(localStorage.getItem("listaria_items") || "[]");

/**
 * Group items by category
 */
const grouped = {};

for (let i = 0; i < items.length; i++) {
    const item = items[i];
    const cat = item.category.toLowerCase();
    
    // If category doesn't exist in grouped, create it
    if (grouped[cat] === undefined) {
        grouped[cat] = [];
    }

    grouped[cat].push(item.name);
}

/**
 * Build the results page
 */
const container = document.getElementById("results-container");

// Create a section for each category
for (const category in grouped) {
    const names = grouped[category];

    // Get icon and label for category
    const icon = categoryIcons[category] || "🛒";
    const label = category.charAt(0).toUpperCase() + category.slice(1);

    // Build section safely using DOM (no innerHTML with user data)
    const section = document.createElement("div");
    section.className = "category-section";

    const header = document.createElement("div");
    header.className = "category-header";

    const iconSpan = document.createElement("span");
    iconSpan.className = "cat-icon";
    iconSpan.textContent = icon;

    const nameSpan = document.createElement("span");
    nameSpan.className = "cat-name";
    nameSpan.textContent = label;

    header.appendChild(iconSpan);
    header.appendChild(nameSpan);

    const itemsDiv = document.createElement("div");
    itemsDiv.className = "category-items";

    for (let j = 0; j < names.length; j++) {
        const catItem = document.createElement("div");
        catItem.className = "cat-item";
        catItem.textContent = names[j];
        itemsDiv.appendChild(catItem);
    }

    section.appendChild(header);
    section.appendChild(itemsDiv);
    container.appendChild(section);
}
