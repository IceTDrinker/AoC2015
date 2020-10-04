from itertools import groupby
from pathlib import Path

content = None
with open(f"exercise_and_input/{Path(__file__).with_suffix('').name}/input.txt", "r") as f:
    content = f.readlines()

work_str = content[0].strip()

for _ in range(40):
    counts = []
    curr_char = None
    curr_char_count = 0
    for char in work_str:
        if char != curr_char:
            if curr_char is not None:
                counts.append((curr_char, curr_char_count))

            curr_char = char
            curr_char_count = 1
        else:
            curr_char_count +=1

    counts.append((curr_char, curr_char_count))

    work_str = ""
    for count in counts:
        work_str += f"{count[1]}{count[0]}"

print(len(work_str))

# for _ in range(50):
#     counts = []
#     curr_char = None
#     curr_char_count = 0
#     for char in work_str:
#         if char != curr_char:
#             if curr_char is not None:
#                 counts.append((curr_char, curr_char_count))

#             curr_char = char
#             curr_char_count = 1
#         else:
#             curr_char_count +=1

#     counts.append((curr_char, curr_char_count))

#     work_str = ""
#     for count in counts:
#         work_str += f"{count[1]}{count[0]}"

# print(len(work_str))

def look_and_say(input):
    return ''.join(str(len(list(v))) + k for k, v in groupby(input))

work_str = content[0].strip()
for _ in range(50):
    work_str = look_and_say(work_str)
print(len(work_str))
