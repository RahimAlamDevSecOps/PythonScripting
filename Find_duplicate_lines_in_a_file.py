# Find duplicate lines in a file

file_path = "/var/log/application.log"

seen = set()
duplicates = set()

try:
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line in seen:
                duplicates.add(line)
            else:
                seen.add(line)

    if duplicates:
        print("Duplicate lines found:")
        for line in duplicates:
            print(line)
    else:
        print("No duplicate lines found.")

except FileNotFoundError:
    print(f"{file_path} not found.")

except Exception as e:
    print(f"An error occurred: {e}")
