from itertools import permutations
from pathlib import Path

content = None
with open(f"exercise_and_input/{Path(__file__).with_suffix('').name}/input.txt", "r") as f:
    content = f.readlines()

adjacency_dict = {}
for line in content:
    path_str, distance_str = line.strip().split(" = ")
    city_1, city_2 = path_str.split(" to ")

    adjacency_list_1 = adjacency_dict.get(city_1, {})
    adjacency_list_1[city_2] = int(distance_str)
    adjacency_dict[city_1] = adjacency_list_1

    adjacency_list_2 = adjacency_dict.get(city_2, {})
    adjacency_list_2[city_1] = int(distance_str)
    adjacency_dict[city_2] = adjacency_list_2

all_permutations = permutations(adjacency_dict.keys())

scores = [
    (sum(adjacency_dict[src][dst] for src, dst in zip(perm[:-1], perm[1:])), perm)
    for perm in all_permutations
]

min_elt = min(scores, key=lambda x: x[0])

print(f"Min elt : {min_elt}")

max_elt = max(scores, key=lambda x: x[0])

print(f"Max elt : {max_elt}")
