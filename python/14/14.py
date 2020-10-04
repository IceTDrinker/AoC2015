from pathlib import Path

content = None
with open(f"exercise_and_input/{Path(__file__).with_suffix('').name}/input.txt", "r") as f:
    content = f.readlines()

time_length = 2503

deer_stats = {}
distances = []
for line in content:
    deer_stat_str, rest_str = line.strip()[:-9].split(" seconds, but then must rest for ")

    rest_duration = int(rest_str)

    deer_name, stat = deer_stat_str.split(" can fly ")
    speed_str, duration_str = stat.split(" km/s for ")

    speed = int(speed_str)
    top_speed_duration = int(duration_str)

    deer_stats[deer_name] = {
        "top_speed": speed,
        "top_duration": top_speed_duration,
        "rest_duration": rest_duration,
        "total_cycle_duration": top_speed_duration + rest_duration,
        "distance_during_cycle": speed * top_speed_duration
    }


for deer_name, curr_deer_stats in deer_stats.items():
    total_cycle_duration = curr_deer_stats["total_cycle_duration"]
    distance_during_cycle = curr_deer_stats["distance_during_cycle"]
    top_duration = curr_deer_stats["top_duration"]
    top_speed = curr_deer_stats["top_speed"]

    number_of_full_cycles = time_length // total_cycle_duration
    full_cycles_distance = number_of_full_cycles * distance_during_cycle

    seconds_in_unfinished_cycle = time_length % total_cycle_duration
    unfinished_cycle_seconds_at_top_speed = min(top_duration, seconds_in_unfinished_cycle)
    unfinished_cycle_ditance = unfinished_cycle_seconds_at_top_speed * top_speed

    distances.append((deer_name, full_cycles_distance + unfinished_cycle_ditance))

print(max(distances, key=lambda x: x[1]))

for v in deer_stats.values():
    v["running"] = True
    v["running_time_remaining"] = v["top_duration"]
    v["resting_time_remaining"] = v["rest_duration"]
    v["distance"] = 0

scores = {deer_name: 0 for deer_name in deer_stats.keys()}
for _ in range(time_length):
    for deer_name, curr_deer_stats in deer_stats.items():
        if curr_deer_stats["running"]:
            curr_deer_stats["distance"] += curr_deer_stats["top_speed"]
            curr_deer_stats["running_time_remaining"] -= 1
            if curr_deer_stats["running_time_remaining"] == 0:
                curr_deer_stats["running_time_remaining"] = curr_deer_stats["top_duration"]
                curr_deer_stats["running"] = False
        else:
            curr_deer_stats["resting_time_remaining"] -= 1
            if curr_deer_stats["resting_time_remaining"] == 0:
                curr_deer_stats["resting_time_remaining"] = curr_deer_stats["rest_duration"]
                curr_deer_stats["running"] = True

    max_dist = max(v["distance"] for v in deer_stats.values())
    for deer_name, v in deer_stats.items():
        if v["distance"] == max_dist:
            scores[deer_name] += 1

max_key = max(scores, key=lambda x: scores[x])
print(f"{max_key} {scores[max_key]}")
