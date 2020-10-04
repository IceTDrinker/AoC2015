import hashlib

content = None
with open("exercise_and_input/04/input.txt", "r") as f:
    content = f.readlines()

key = content[0].strip()

idx = 0
while True:
    idx += 1
    digest = hashlib.md5(f"{key}{idx}".encode()).hexdigest()
    if digest.startswith("00000"):
        break

print(f"Suffix : {idx}")
print(f"Digest : {digest}")

idx = 0
while True:
    idx += 1
    digest = hashlib.md5(f"{key}{idx}".encode()).hexdigest()
    if digest.startswith("000000"):
        break

print(f"Suffix : {idx}")
print(f"Digest : {digest}")