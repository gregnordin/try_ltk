import ltk


@ltk.callback
def loaded_file(file, content):
    ltk.find("#content").html(content)


def create():
    return ltk.VBox(
        ltk.Heading1("Can we read a file?"),
        ltk.File(loaded_file),
        ltk.Label("File contents:"),
        ltk.Preformatted(
            "File contents will be shown here after selecting file.",
            {
                "margin-left": 20,
                "margin-right": 20,
                "padding": 8,
                "background-color": "lightyellow",
                "border": "1px solid gray",
            },
        ).attr("id", "content"),
    )


create().appendTo(ltk.find("body"))
