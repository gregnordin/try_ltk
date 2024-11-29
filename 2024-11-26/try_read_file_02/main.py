import ltk


def read_file(file):
    with open(file, encoding="utf-8") as fp:
        file_text = ltk.create("<script>").text(fp.read())

    return file_text


def feedback(text):
    ltk.find("#feedback").html(text).css("text-align", "left")


@ltk.callback
def handle_file(event):
    element = ltk.find(event.target)
    kind = element.prop("type")
    feedback(f"{kind}: {element.val()}")
    ltk.Paragraph(f"event: {str(type(event))}").appendTo(ltk.find("body"))
    file = event.target.files.to_py()  # [0]
    ltk.Paragraph(f"file: {file}").appendTo(ltk.find("body"))
    ltk.Paragraph(f"element: {str(type(element))}").appendTo(ltk.find("body"))
    ltk.Paragraph(f"element.val(): {element.val()}").appendTo(ltk.find("body"))
    ltk.Paragraph(f"element.text(): {element.text()}").appendTo(ltk.find("body"))
    # This returns all attributes, including built-in ones
    for attribute in dir(element):
        # Skip built-in attributes (those starting with __)
        if not attribute.startswith("__"):
            value = getattr(element, attribute)
            ltk.Paragraph(f"{attribute}: {value}").appendTo(ltk.find("body"))

    # file_text = read_file(element.val())
    # ltk.html(file_text).appendTo(ltk.find("body"))
    # ltk.find("body").html(file_text)


def create():
    return ltk.VBox(
        ltk.Heading1("Can we read a file?"),
        ltk.File().on("change", handle_file),
        ltk.Text("File name goes here").attr("id", "feedback"),
    )


create().appendTo(ltk.find("body"))
