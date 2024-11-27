import sys
import re


def main():
    input = sys.stdin.read  # Read all input at once
    lines = input().splitlines()  # Split into individual lines

    for line in lines:
        process_line(line)  # Process each line


def process_line(line):
    parts = line.split(";")
    operation = parts[0]  # 'S' for split or 'C' for combine
    type_ = parts[1]  # 'M' (method), 'C' (class), or 'V' (variable)
    data = parts[2]  # The actual string to process

    if operation == "S":
        handle_split(type_, data)
    elif operation == "C":
        handle_combine(type_, data)


def handle_split(type_, data):
    if type_ == "M" and data.endswith("()"):
        data = data[:-2]  # Remove the trailing "()"

    # Adjust regex to split words correctly for variables too
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?![a-z])', data)

    # Convert the words to lowercase and join with spaces
    result = ' '.join(word.lower() for word in words)
    print(result)


def handle_combine(type_, data):
    words = data.split()  # Split the input into separate words

    if type_ == "C":  # Class
        result = ''.join(word.capitalize() for word in words)
    elif type_ == "V":  # Variable
        result = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    elif type_ == "M":  # Method
        result = words[0].lower() + ''.join(word.capitalize() for word in words[1:]) + "()"

    print(result)


if __name__ == "__main__":
    main()
