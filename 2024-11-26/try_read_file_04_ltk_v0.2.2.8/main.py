import ltk


def feedback(text):
    ltk.find("#feedback").html(text).css("text-align", "left")


@ltk.callback
def loaded_file(file, content):
    feedback(f"File name: {file.name}")
    output_div = ltk.find("#content")
    output_div.html(content)


def create():
    return ltk.VBox(
        ltk.Heading1("Can we read a file?"),
        ltk.File(loaded_file),
        ltk.Text("File name goes here").attr("id", "feedback"),
        ltk.Label("File contents:"),
        ltk.TextArea(
            "File contents go here",
            {"height": 120, "width": "90%", "margin-left": 20, "fontsize": 10},
        ).attr("id", "content"),
    )


create().appendTo(ltk.find("body"))
