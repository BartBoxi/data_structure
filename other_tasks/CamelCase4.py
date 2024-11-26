def main():
    import sys
    input = sys.stdin.read
    lines = input().splitlines()

    for line in lines:
        process_line(line)


def process_line(line):
    parts = line.split(";")
    operation = parts[0]  # s or c #S (split) or C (combine)
    type_ = parts[1]  # m c or v
    # M indicates method, C indicates class, and V indicates variable
    data = parts[2]  # string to process itself

    if operation == "S":
        handle_split(type_, data)
    elif operation == "C":
        handle_combine(type_, data)


if __name__ == "__main__":
    main()


def handle_split(type_, data):
    if data[-2:] == "()":
        data = data[:-2]
    elif


def handle_combine(type_, data):




