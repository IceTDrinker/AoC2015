import json

from pathlib import Path

content = None
with open(f"exercise_and_input/{Path(__file__).with_suffix('').name}/input.txt", "r") as f:
    content = json.load(f)

def sum_nested(nested_stuff):
    acc = 0
    if isinstance(nested_stuff, dict):
        for _, v in nested_stuff.items():
            if isinstance(v, int):
                acc += v
            else:
                acc += sum_nested(v)
    elif isinstance(nested_stuff, list):
        for v in nested_stuff:
            if isinstance(v, int):
                acc += v
            else:
                acc += sum_nested(v)

    return acc

print(sum_nested(content))

def sum_nested_not_red(nested_stuff):
    acc = 0
    if isinstance(nested_stuff, dict):
        if "red" not in nested_stuff.values():
            for _, v in nested_stuff.items():
                if isinstance(v, int):
                    acc += v
                else:
                    acc += sum_nested_not_red(v)
    elif isinstance(nested_stuff, list):
        for v in nested_stuff:
            if isinstance(v, int):
                acc += v
            else:
                acc += sum_nested_not_red(v)

    return acc

print(sum_nested_not_red(content))

