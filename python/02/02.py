content = None
with open("exercise_and_input/02/input.txt", "r") as f:
    content = f.readlines()

required_paper_area = 0
required_ribbon_length = 0

for line in content:
    l, w, h = (int(val) for val in line.strip().split("x"))

    side_lw_area = l * w
    side_wh_area = w * h
    side_hl_area = h * l

    required_paper_area += 2 * (side_lw_area + side_wh_area + side_hl_area) + min(
        side_lw_area, side_wh_area, side_hl_area
    )

    required_ribbon_length += 2 * sum(sorted([l, w, h])[:2]) + l * w * h

print(f"Required area of paper : {required_paper_area}")
print(f"Required ribbon length : {required_ribbon_length}")
