// we use ai to generate icons for each category, so we can easily identify them at a glance
// icons for each category
var categoryIcons = {
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
}

// get items from localStorage
var items = JSON.parse(localStorage.getItem("listaria_items") || "[]")

// group items by category
var grouped = {}

for (var i = 0; i < items.length; i++) {
    var item = items[i]
    var cat = item.category.toLowerCase()
// if category doesn't exist in grouped, create it
    if (grouped[cat] === undefined) {
        grouped[cat] = []
    }
    // what is three === in js? --- IGNORE ---

    grouped[cat].push(item.name)
}

// build the page
var container = document.getElementById("results-container")



// create a section for each category
for (var category in grouped) {
    var names = grouped[category]

    // get icon and label for category
    var icon = categoryIcons[category] || "🛒"
    var label = category.charAt(0).toUpperCase() + category.slice(1)

    // build section safely using DOM (no innerHTML with user data)
    var section = document.createElement("div")
    section.className = "category-section"

    var header = document.createElement("div")
    header.className = "category-header"

    var iconSpan = document.createElement("span")
    iconSpan.className = "cat-icon"
    iconSpan.textContent = icon  // emojis are safe but use textContent anyway

    var nameSpan = document.createElement("span")
    nameSpan.className = "cat-name"
    nameSpan.textContent = label  // safe: no HTML injection

    header.appendChild(iconSpan)
    header.appendChild(nameSpan)

    var itemsDiv = document.createElement("div")
    itemsDiv.className = "category-items"

    for (var j = 0; j < names.length; j++) {
        var catItem = document.createElement("div")
        catItem.className = "cat-item"
        catItem.textContent = names[j]  // safe: user input never becomes HTML
        itemsDiv.appendChild(catItem)
    }

    section.appendChild(header)
    section.appendChild(itemsDiv)
    container.appendChild(section)
}
