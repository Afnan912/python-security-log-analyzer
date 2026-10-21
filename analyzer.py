
from collections import Counter
from pathlib import Path

LOG_FILE = Path(__file__).with_name("sample_logs.txt")
THRESHOLD = 3


def analyze_logs():
    failed_ips = Counter()

    try:
        with LOG_FILE.open("r", encoding="utf-8") as file:
            for line in file:
                parts = line.split()

                if len(parts) >= 4 and "FAILED" in parts:
                    ip_address = parts[-1]
                    failed_ips[ip_address] += 1

    except FileNotFoundError:
        print(f"Error: {LOG_FILE.name} was not found.")
        return

    print("=== Security Log Analysis ===")

    if not failed_ips:
        print("No failed login attempts found.")
        return

    for ip, count in failed_ips.most_common():
        print(f"{ip}: {count} failed attempts")

        if count >= THRESHOLD:
            print(
                f"  ALERT: Repeated failures detected for {ip}"
            )


if __name__ == "__main__":
    analyze_logs()
