# First, import LTK in your HTML
"""
<head>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- Import LTK -->
    <py-script src="https://raw.githubusercontent.com/pyscript/ltk/main/src/ltk/__init__.py"></py-script>
</head>
"""

# Python code using LTK
from ltk import $

# jQuery-like selector to find elements
# Select by ID
button = $("#my-button")

# Select by class
items = $(".item")

# Select by tag
paragraphs = $("p")

# Chaining operations (jQuery-style)
$("#my-div").html("New content").addClass("highlighted")

# Event handling
def handle_click(event):
    print("Button clicked!")
    $("#result").text("Button was clicked!")

$("#my-button").on("click", handle_click)

# DOM manipulation
# Create new element
new_div = $("<div>").html("Dynamic content").addClass("new-class")
$("#container").append(new_div)

# Modify styles
$("#my-element").css({
    "color": "blue",
    "font-size": "16px",
    "background-color": "#f0f0f0"
})

# Working with forms
def handle_submit(event):
    event.preventDefault()
    name = $("#name-input").val()
    email = $("#email-input").val()
    $("#form-result").html(f"Submitted: {name}, {email}")

$("#my-form").on("submit", handle_submit)

# Ajax-like functionality for loading content
async def load_content():
    response = await fetch("https://api.example.com/data")
    data = await response.json()
    $("#content").html(str(data))

# Traversing the DOM
parent = $("#child").parent()
next_sibling = $("#element").next()
prev_sibling = $("#element").prev()
children = $("#parent").children()

# Example HTML structure
"""
<body>
    <div id="container">
        <button id="my-button">Click me</button>
        <div id="result"></div>
        
        <form id="my-form">
            <input type="text" id="name-input" placeholder="Name">
            <input type="email" id="email-input" placeholder="Email">
            <button type="submit">Submit</button>
        </form>
        <div id="form-result"></div>
        
        <div id="content"></div>
    </div>
    
    <py-script>
        # Your Python/LTK code goes here
    </py-script>
</body>
"""