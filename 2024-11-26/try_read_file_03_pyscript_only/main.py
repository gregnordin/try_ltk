from js import document, console, FileReader
from pyodide.ffi import create_proxy


def read_file(event):
    try:
        # Get the selected file
        files = event.target.files
        if not files or files.length == 0:
            return

        file = files.item(0)  # Using item() instead of indexing

        def handle_load(e):
            content = e.target.result
            output_div = document.getElementById("output")
            output_div.innerHTML = f"<pre>{content}</pre>"

        # Create a FileReader
        reader = FileReader.new()
        reader.onload = create_proxy(handle_load)

        # Read the file
        reader.readAsText(file)
    except Exception as e:
        console.error(f"Error: {str(e)}")
        output_div = document.getElementById("output")
        output_div.innerHTML = f"<pre>Error reading file: {str(e)}</pre>"


# Add event listener to the file input
file_input = document.getElementById("fileInput")
file_input.addEventListener("change", create_proxy(read_file))
