PADDING = 5


def text_formatter(data):
    column_width = max(len(word) for row in data for word in row) + PADDING
    with open("./report/aliens_report.txt", "w") as f:
        f.write("ALIENS DATABASE\n")
        f.write("\n\n")
        for row in data:
            f.write("".join(word.center(column_width) for word in row) + "\n")
