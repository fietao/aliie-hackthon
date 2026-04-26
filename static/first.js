
// // colors for each category
var categoryColors = {
    "frozen goods": "#A8D8EA",
    "dairy": "#FFF3B0",
    "meat": "#FFCDD2",
    "produce": "#C8E6C9",
    "breakfast foods": "#FFD180",
    "bakery": "#D7B899",
    "beverages": "#80DEEA",
    "snacks": "#CE93D8",
    "laundry and cleaning supplies": "#B3E5FC",
    "miscellaneous": "#CFD8DC"
}

// add item to the list
function addItem() {
    var input = document.getElementById("item-input")
    var value = input.value.trim()

    if (value === "") return

    renderItem(value)
    input.value = ""
}

// create an item card and add it to the page
function renderItem(name) {
    var listSection = document.getElementById("list-section")

    var div = document.createElement("div")
    div.className = "item"

    var nameSpan = document.createElement("span")
    nameSpan.className = "name"
    nameSpan.textContent = name  // safe: textContent never executes HTML

    var categorySpan = document.createElement("span")
    categorySpan.className = "category"

    var removeBtn = document.createElement("button")
    removeBtn.className = "remove-btn"
    removeBtn.textContent = "✕"
    removeBtn.addEventListener("click", function() { div.remove() })

    div.appendChild(nameSpan)
    div.appendChild(categorySpan)
    div.appendChild(removeBtn)

    listSection.appendChild(div)
}

// send all items to the server and get categories back
async function categorizeAll() {
    var items = document.querySelectorAll(".item")

    if (items.length === 0) {
        alert("Please add some items first!")
        return
    }

    var results = []

    for (var i = 0; i < items.length; i++) {
        var name = items[i].querySelector(".name").textContent
        // send item to server
        var response = await fetch("/add", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ item: name })
        })

        var data = await response.json()
        results.push({ name: data.item, category: data.category })
    }

    // save results and go to results page
    localStorage.setItem("listaria_items", JSON.stringify(results))
    window.location.href = "/results"
}

// allow pressing Enter to add item
document.getElementById("item-input").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        addItem()
    }
})
