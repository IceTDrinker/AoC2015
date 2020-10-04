content = None
with open("exercise_and_input/05/input.txt", "r") as f:
    content = f.readlines()

bad_strings = ["ab", "cd", "pq", "xy"]
vowels = ["a", "e", "i", "o", "u"]

nice_strings_count = 0
naugthy_strings_count = 0

for line in content:
    line = line.strip()

    if any(bad_string in line for bad_string in bad_strings):
        naugthy_strings_count += 1
        continue

    vowel_counts = 0
    for vowel in vowels:
        vowel_counts += line.count(vowel)

    if vowel_counts < 3:
        naugthy_strings_count += 1
        continue

    was_nice = False
    for idx, char in enumerate(line[:-1]):
        if char == line[idx + 1]:
            was_nice = True
            break

    if was_nice:
        nice_strings_count += 1
    else:
        naugthy_strings_count += 1

print(f"Nice strings : {nice_strings_count}")
print(f"Naughty strings : {naugthy_strings_count}")

nice_strings_count = 0
naugthy_strings_count = 0

for line in content:
    line = line.strip()

    was_naughty = True
    for idx in range(len(line[:-2])):
        bigram = line[idx:idx + 2]
        rem_line = line[idx + 2:]
        if bigram in rem_line:
            was_naughty = False
            break

    if was_naughty:
        naugthy_strings_count += 1
        continue

    was_naughty = True
    for idx, char in enumerate(line[:-2]):
        if char == line[idx + 2]:
            was_naughty = False
            break

    if was_naughty:
        naugthy_strings_count += 1
    else:
        nice_strings_count += 1

print(f"Nice strings : {nice_strings_count}")
print(f"Naughty strings : {naugthy_strings_count}")
