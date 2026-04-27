
// Color map for each category (CSS gradient friendly)
const categoryColors = {
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
};

/**
 * Add item to the shopping list
 */
function addItem() {
    const input = document.getElementById("item-input");
    const value = input.value.trim();

    if (value === "") {
        alert("Please enter an item name");
        return;
    }

    renderItem(value);
    input.value = "";
    input.focus();
}

/**
 * Create an item card and add it to the page
 */
function renderItem(name) {
    const listSection = document.getElementById("list-section");

    const div = document.createElement("div");
    div.className = "item";

    const nameSpan = document.createElement("span");
    nameSpan.className = "name";
    nameSpan.textContent = name;

    const categorySpan = document.createElement("span");
    categorySpan.className = "category";

    const removeBtn = document.createElement("button");
    removeBtn.className = "remove-btn";
    removeBtn.textContent = "✕";
    removeBtn.setAttribute("aria-label", `Remove ${name}`);
    removeBtn.addEventListener("click", function() {
        div.remove();
        updateCategorizeButton();
    });

    div.appendChild(nameSpan);
    div.appendChild(categorySpan);
    div.appendChild(removeBtn);

    listSection.appendChild(div);
    updateCategorizeButton();
}

/**
 * Update categorize button state
 */
function updateCategorizeButton() {
    const btn = document.getElementById("categorize-btn");
    const items = document.querySelectorAll(".item");
    btn.disabled = items.length === 0;
}

/**
 * Send all items to the server and categorize them
 */
async function categorizeAll() {
    const items = document.querySelectorAll(".item");

    if (items.length === 0) {
        alert("Please add some items first!");
        return;
    }

    const categorizeBtn = document.getElementById("categorize-btn");
    categorizeBtn.disabled = true;
    categorizeBtn.textContent = "CATEGORIZING...";

    const results = [];
    let errorCount = 0;

    for (let i = 0; i < items.length; i++) {
        const name = items[i].querySelector(".name").textContent;
        const categorySpan = items[i].querySelector(".category");

        try {
            // Send item to server
            const response = await fetch("/api/categorize", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ item: name })
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const data = await response.json();
            
            if (data.success) {
                results.push({ name: data.item, category: data.category });
                categorySpan.textContent = data.category;
                categorySpan.style.backgroundColor = categoryColors[data.category] || "#CFD8DC";
            } else {
                throw new Error(data.error || "Unknown error");
            }
        } catch (error) {
            console.error(`Error categorizing "${name}":`, error);
            categorySpan.textContent = "Error";
            categorySpan.style.backgroundColor = "#FFCDD2";
            errorCount++;
        }
    }

    // Save results and navigate
    localStorage.setItem("listaria_items", JSON.stringify(results));
    
    if (errorCount > 0) {
        alert(`Categorized ${results.length}/${items.length} items. Some items failed.`);
    }
    
    window.location.href = "/results";
}
// Allow pressing Enter to add item
document.getElementById("item-input").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        e.preventDefault();
        addItem();
    }
});

// Initialize button state
updateCategorizeButton();