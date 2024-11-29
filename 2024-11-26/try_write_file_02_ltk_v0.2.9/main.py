import ltk


@ltk.callback
def save_to_file(event):
    ltk.File().download("example.txt", ltk.find("#content").val())


def create():
    margin_left = ("margin-left", 10)
    # Example string
    my_string = """This is an example string
with multiple lines
of text content."""

    return ltk.VBox(
        ltk.Heading1("Save text to a file").css(*margin_left),
        ltk.Label("Text to save to file:").css(*margin_left),
        ltk.TextArea(
            my_string,
            {
                "height": 200,
                "margin-left": margin_left[1] + 20,
                "margin-right": 20,
                "padding": 8,
                "background-color": "lightyellow",
                "border": "1px solid gray",
            },
        ).attr("id", "content"),
        ltk.Button("Save text to file", save_to_file)
            .css("margin-top", 5)
            .css(*margin_left),
    )

create().appendTo(ltk.find("body"))
