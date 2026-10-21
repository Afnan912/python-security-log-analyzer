
from collections import Counter
from pathlib import Path

LOG_FILE = Path(__file__).with_name("sample_logs.txt")
THRESHOLD = 3


def analyze_logs():
    failed_ips = Counter()
    successful_logins = 0
    total_events = 0

    try:
        with LOG_FILE.open("r", encoding="utf-8") as file:
            for line in file:
                parts = line.split()

                if len(parts) < 4:
                    continue

                status = parts[2]
                ip_address = parts[-1]

                if status not in ("SUCCESS", "FAILED"):
                    continue

                total_events += 1

                if status == "FAILED":
                    failed_ips[ip_address] += 1
                else:
                    successful_logins += 1

    except FileNotFoundError:
        print(f"Error: {LOG_FILE.name} was not found.")
        return

    print("=== Security Log Analysis ===")
    print(f"Total login events: {total_events}")
    print(f"Successful logins: {successful_logins}")
    print(f"Failed login events: {sum(failed_ips.values())}")
    print("\n=== Failed Attempts by IP ===")

    for ip, count in failed_ips.most_common():
        print(f"{ip}: {count} failed attempts")

        if count >= THRESHOLD:
            print(f"  ALERT: Repeated failures detected for {ip}")


if __name__ == "__main__":
    analyze_logs()
