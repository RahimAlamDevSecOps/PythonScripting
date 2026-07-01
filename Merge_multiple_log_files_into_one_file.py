# Merge multiple log files into one file

import os

log_folder = "/var/log/myapp"
output_file = "/var/log/merged.log"

try:
    with open(output_file, "w") as outfile:

        for file in os.listdir(log_folder):
            if file.endswith(".log"):
                file_path = os.path.join(log_folder, file)

                if os.path.isfile(file_path):
                    with open(file_path, "r") as infile:
                        outfile.write(f"\n----- {file} -----\n")

                        for line in infile:
                            outfile.write(line)

    print(f"All log files merged successfully into {output_file}")

except FileNotFoundError:
    print(f"{log_folder} does not exist.")

except Exception as e:
    print(f"An error occurred: {e}")
