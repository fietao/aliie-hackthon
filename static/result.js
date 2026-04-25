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
    var icon = categoryIcons[category] || "🛒"
    var label = category.charAt(0).toUpperCase() + category.slice(1)

    // build the items list html
    var itemsHtml = ""
    for (var j = 0; j < names.length; j++) {
        itemsHtml += '<div class="cat-item">' + names[j] + '</div>'
    }

    // build the section html
    var section = document.createElement("div")
    section.className = "category-section"
    section.innerHTML = '<div class="category-header">' +
                            '<span class="cat-icon">' + icon + '</span>' +
                            '<span class="cat-name">' + label + '</span>' +
                        '</div>' +
                        '<div class="category-items">' + itemsHtml + '</div>'

    container.appendChild(section)
}
