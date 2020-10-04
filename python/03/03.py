content = None
with open("exercise_and_input/03/input.txt", "r") as f:
    content = f.readlines()

x = 0
y = 0

gifts_distributed_per_house = {}

gifts_distributed_per_house[(0, 0)] = 1

for direction in content[0].strip():
    if direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    elif direction == ">":
        x += 1
    elif direction == "<":
        x -= 1

    coords = (x, y)
    if coords in gifts_distributed_per_house.keys():
        gifts_distributed_per_house[coords] += 1
    else:
        gifts_distributed_per_house[coords] = 1

lucky_house_count = len(gifts_distributed_per_house)

print(f"Lucky house count : {lucky_house_count}")

x_santa = 0
y_santa = 0

x_robot = 0
y_robot = 0

gifts_distributed_per_house = {}

gifts_distributed_per_house[(0, 0)] = 2

santa_is_moving = True

for direction in content[0].strip():
    if direction == "^":
        if santa_is_moving:
            y_santa += 1
        else:
            y_robot += 1
    elif direction == "v":
        if santa_is_moving:
            y_santa -= 1
        else:
            y_robot -= 1
    elif direction == ">":
        if santa_is_moving:
            x_santa += 1
        else:
            x_robot += 1
    elif direction == "<":
        if santa_is_moving:
            x_santa -= 1
        else:
            x_robot -= 1

    coords = (x_santa, y_santa) if santa_is_moving else (x_robot, y_robot)
    if coords in gifts_distributed_per_house.keys():
        gifts_distributed_per_house[coords] += 1
    else:
        gifts_distributed_per_house[coords] = 1

    santa_is_moving = not santa_is_moving

lucky_house_count = len(gifts_distributed_per_house)

print(f"Lucky house count : {lucky_house_count}")

