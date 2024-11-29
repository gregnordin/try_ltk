import ltk

colors = ["#E40303", "#FF8C00", "#FFED00", "#008026", "#24408E", "#732982"]


def getsource(file="testfile.txt"):
    def setsource(src):
        src = "\n".join(src.split("\n")[2:])
        print(src)
        ltk.find(f'code[file="{file}"]').empty().text(src)

    ltk.get(file, setsource, "html")
    return f"Loading {file}..."


def read_file(file="testfile.txt"):
    with open(file, encoding="utf-8") as fp:
        file_text = ltk.create("<script>").text(fp.read())

    return file_text


def create():
    return ltk.VBox(
        ltk.Heading1("Can we read a file?"),
        ltk.Text("Click button to read 'testfile.txt':"),
        ltk.Button("Read file", read_file),
        ltk.Text("some text"),
    )


print("testing...")
create().appendTo(ltk.find("body"))
