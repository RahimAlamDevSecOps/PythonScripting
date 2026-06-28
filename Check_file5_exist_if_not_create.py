import os
filename = "file5"
try:
    if os.path.exists(filename):
        print(f"{filename} already exists.")
    else:
        print(f"{filename} does not exist. Creating ....!")
        with open(filename, "w") as file:
            file.write("Hello Rahim")
            print(f"{filename} created successfully")
except Exception as e:
    print(f"An error occured as: {e}")
