from pathlib import Path

import numpy

content = None
with open(f"exercise_and_input/{Path(__file__).with_suffix('').name}/input.txt", "r") as f:
    content = f.readlines()

TOGGLE_CMD = "toggle "
TURN_ON_CMD = "turn on "
TURN_OFF_CMD = "turn off "

lights = numpy.zeros((1000, 1000), dtype=numpy.int)

for instruction in content:
    instruction.strip()

    cmd = None
    if instruction.startswith(TOGGLE_CMD):
        instruction = instruction.replace(TOGGLE_CMD, "", 1)
        cmd = TOGGLE_CMD
    elif instruction.startswith(TURN_ON_CMD):
        instruction = instruction.replace(TURN_ON_CMD, "", 1)
        cmd = TURN_ON_CMD
    elif instruction.startswith(TURN_OFF_CMD):
        instruction = instruction.replace(TURN_OFF_CMD, "", 1)
        cmd = TURN_OFF_CMD

    left_coord_str, right_coord_str = instruction.split(" through ")
    left, top = (int(val) for val in left_coord_str.split(","))
    right, bot = (int(val) for val in right_coord_str.split(","))

    if cmd == TOGGLE_CMD:
        lights[left:right + 1, top:bot + 1] = 1 - lights[left:right + 1, top:bot + 1]
    elif cmd == TURN_ON_CMD:
        lights[left:right + 1, top:bot + 1] = 1
    elif cmd == TURN_OFF_CMD:
        lights[left:right + 1, top:bot + 1] = 0

print(f"Light count : {lights.sum()}")

lights = numpy.zeros((1000, 1000), dtype=numpy.int)

for instruction in content:
    instruction.strip()

    cmd = None
    if instruction.startswith(TOGGLE_CMD):
        instruction = instruction.replace(TOGGLE_CMD, "", 1)
        cmd = TOGGLE_CMD
    elif instruction.startswith(TURN_ON_CMD):
        instruction = instruction.replace(TURN_ON_CMD, "", 1)
        cmd = TURN_ON_CMD
    elif instruction.startswith(TURN_OFF_CMD):
        instruction = instruction.replace(TURN_OFF_CMD, "", 1)
        cmd = TURN_OFF_CMD

    left_coord_str, right_coord_str = instruction.split(" through ")
    left, top = (int(val) for val in left_coord_str.split(","))
    right, bot = (int(val) for val in right_coord_str.split(","))

    if cmd == TOGGLE_CMD:
        lights[left:right + 1, top:bot + 1] += 2
    elif cmd == TURN_ON_CMD:
        lights[left:right + 1, top:bot + 1] += 1
    elif cmd == TURN_OFF_CMD:
        lights[left:right + 1, top:bot + 1] -= 1
        lights = numpy.clip(lights, 0, None)

print(f"Total brightness : {lights.sum()}")
