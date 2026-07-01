
# Read a log file and print only the ERROR lines

log_file = "/var/log/application.log"

try:
    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                print(line.strip())

except FileNotFoundError:
    print(f"{log_file} not found.")

except Exception as e:
    print(f"An error occurred: {e}")
