def load_file(filename: str) -> str:
    content = ""

    with open(filename, "r") as file:
        content = file.read()

    return content
