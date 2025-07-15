import textwrap

def wrap(string, max_width):
    result = []
    for i in range(0, len(string), max_width):
        result.append(string[i:i+max_width])
    return '\n'.join(result )