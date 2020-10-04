current_floor = 0

with open("exercise_and_input/01/input.txt", "r") as f:
    content = f.readlines()

parens = content[0].strip()

current_floor += parens.count("(")
current_floor -= parens.count(")")

print(f"Last floor : {current_floor}")

# Now we go one by one to find when santa gets in the basement

current_floor = 0
for idx, char in enumerate(parens):
    if char == "(":
        current_floor += 1
    elif char == ")":
        current_floor -= 1

    if current_floor < 0:
        break

print(f"Position when Santa gets in the basement : {idx + 1}")
