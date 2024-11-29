import ltk


@ltk.callback
def loaded_file(file, content):
    ltk.find("#content").html(content)


def create():
    return ltk.VBox(
        ltk.Heading1("Can we read a file?"),
        ltk.File(loaded_file),
        ltk.Label("File contents:"),
        ltk.Code(
            "Plaintext",
            "File contents will be shown here after selecting file.",
            style={
                "width": "90%",
                "margin-left": 20,
            },
        ).attr("id", "content"),
    )


create().appendTo(ltk.find("body"))
