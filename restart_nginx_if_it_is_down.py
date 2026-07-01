import subprocess

service = "nginx"

try:
    # Check if the service is running
    result = subprocess.run(
        ["systemctl", "is-active", service],
        capture_output=True,
        text=True
    )

    if result.stdout.strip() == "active":
        print(f"{service} is running.")

    else:
        print(f"{service} is not running.")
        print(f"Restarting {service}...")

        subprocess.run(["systemctl", "restart", service], check=True)

        # Verify if restart was successful
        result = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True,
            text=True
        )

        if result.stdout.strip() == "active":
            print(f"{service} restarted successfully.")
        else:
            print(f"Failed to restart {service}.")

except Exception as e:
    print(f"An error occurred: {e}")
