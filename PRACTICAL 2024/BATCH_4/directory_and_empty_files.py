import os

# Specify the directory path
path = input("Enter directory path: ")

empty_count = 0

print("\nFiles:")
for item in os.listdir(path):
    full_path = os.path.join(path, item)

    if os.path.isfile(full_path):
        print(item)

        if os.path.getsize(full_path) == 0:
            empty_count += 1

print("\nDirectories:")
for item in os.listdir(path):
    full_path = os.path.join(path, item)

    if os.path.isdir(full_path):
        print(item)

print("\nNumber of empty files:", empty_count)