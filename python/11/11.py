from pathlib import Path

content = None
with open(f"exercise_and_input/{Path(__file__).with_suffix('').name}/input.txt", "r") as f:
    content = f.readlines()

work_str = content[0].strip()


def validate_seq_and_bigrams(str_to_val: str) -> bool:
    has_increasing_sequence = False
    has_two_bigrams = False
    pass_is_valid = False
    bigrams = set()
    for idx, char in enumerate(str_to_val):
        if idx < len(str_to_val) - 2:
            if (
                ord(str_to_val[idx + 1]) == ord(char) + 1
                and ord(str_to_val[idx + 2]) == ord(char) + 2
            ):
                has_increasing_sequence = True

        if idx < len(str_to_val) - 1:
            if char == str_to_val[idx + 1]:
                bigrams.add(char * 2)

        has_two_bigrams = len(bigrams) >= 2
        pass_is_valid = has_increasing_sequence and has_two_bigrams

        if pass_is_valid:
            break

    return pass_is_valid


def increment_str(str_to_inc: str) -> str:
    iol_idx = max(str_to_inc.find(iol) for iol in ["i", "o", "l"])
    if iol_idx == -1:
        results = str_to_inc
        num_letters = len(results)
        for idx, char in enumerate(reversed(str_to_inc)):
            if char != "z":
                first_part = results[:num_letters -idx - 1]
                last_part = results[num_letters - idx:]
                results = f"{first_part}{chr(ord(char) + 1)}{last_part}"
                return results
            else:
                first_part = results[:num_letters -idx - 1]
                last_part = results[num_letters - idx:]
                results = f"{first_part}a{last_part}"

    else:
        iol_next = chr(ord(str_to_inc[iol_idx]) + 1)
        first_part = str_to_inc[:iol_idx]
        last_part = str_to_inc[iol_idx + 1:]
        str_to_inc = f"{first_part}{iol_next}{'a' * (len(str_to_inc) - iol_idx - 1)}"
        return str_to_inc


while True:
    if validate_seq_and_bigrams(work_str):
        if all(iol not in work_str for iol in ["i", "o", "l"]):
            break

    work_str = increment_str(work_str)

print(work_str)

work_str = increment_str(work_str)

while True:
    if validate_seq_and_bigrams(work_str):
        if all(iol not in work_str for iol in ["i", "o", "l"]):
            break

    work_str = increment_str(work_str)

print(work_str)
