from pathlib import Path

content = None
with open(f"exercise_and_input/{Path(__file__).with_suffix('').name}/input.txt", "r") as f:
    content = f.readlines()

# This is hackish, it's not a proper de-escapation of the string
# Plus apparently python has an eval function to evaluate escaped sequences to strings
num_of_code_characters = 0
delta_to_represented_char = 0
for line in content:
    line = line.strip()

    num_of_code_characters += len(line)
    delta_to_represented_char += 2

    num_of_escaped_backslashes = line.count(r"\\")
    delta_to_represented_char += num_of_escaped_backslashes

    line = line.replace(r"\\", "")

    num_of_escaped_quotes = line.count(r"\"")
    delta_to_represented_char += num_of_escaped_quotes

    num_of_hex_escapes = line.count(r"\x")
    delta_to_represented_char += 3 * num_of_hex_escapes

print(f"Delta : {delta_to_represented_char}")

delta_to_escape_string = 0
for line in content:
    line = line.strip()

    delta_to_escape_string += 4

    line = line[1:-1]

    num_quotes = line.count(r'"')
    delta_to_escape_string += num_quotes

    num_backslahes = line.count("\\")
    delta_to_escape_string += num_backslahes

print(f"Delta : {delta_to_escape_string}")
