import subprocess

service = "nginx"

try:
    result = subprocess.run(
        ["systemctl", "is-active", service],
        capture_output=True,
        text=True
    )

    if result.stdout.strip() == "active":
        print(f"{service} is running.")
    else:
        print(f"{service} is not running.")

except Exception as e:
    print(f"An error occurred: {e}")
