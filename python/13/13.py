from itertools import permutations
from pathlib import Path

content = None
with open(f"exercise_and_input/{Path(__file__).with_suffix('').name}/input.txt", "r") as f:
    content = f.readlines()

adjacency_dict = {}

for line in content:
    line = line.strip()[:-1]

    person_would_gain, other_person = line.split(" happiness units by sitting next to ")

    gain = None
    if "gain" in person_would_gain:
        person, gain_str = person_would_gain.split(" would gain ")
        gain = int(gain_str)
    else:
        person, gain_str = person_would_gain.split(" would lose ")
        gain = -int(gain_str)

    adjacency_per_person = adjacency_dict.get(person, {})
    adjacency_per_person[other_person] = gain
    adjacency_dict[person] = adjacency_per_person

all_gains = []
for perm in permutations(adjacency_dict.keys()):
    curr_gain = 0
    for idx, person in enumerate(perm):
        pervious_person = perm[idx - 1]
        next_person = perm[(idx + 1) % len(perm)]

        curr_gain += (
            adjacency_dict[person][pervious_person] + adjacency_dict[person][next_person]
        )

    all_gains.append((curr_gain, perm))

max_gain = max(all_gains, key=lambda x: x[0])

print(max_gain)

me_person = "Me person"

for _, v in adjacency_dict.items():
    v[me_person] = 0

adjacency_dict[me_person] = {k: 0 for k in adjacency_dict.keys()}

all_gains = []
for perm in permutations(adjacency_dict.keys()):
    curr_gain = 0
    for idx, person in enumerate(perm):
        pervious_person = perm[idx - 1]
        next_person = perm[(idx + 1) % len(perm)]

        curr_gain += (
            adjacency_dict[person][pervious_person] + adjacency_dict[person][next_person]
        )

    all_gains.append((curr_gain, perm))

max_gain = max(all_gains, key=lambda x: x[0])

print(max_gain)
