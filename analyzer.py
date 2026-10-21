
from collections import Counter
from pathlib import Path


def analyze_logs(log_file):
    """Analyze authentication logs for failed logins."""

    path = Path(log_file)

    if not path.exists():
        print(f"Error: Log file not found: {path}")
        return

    failed_ips = Counter()
    total_lines = 0

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            total_lines += 1
            parts = line.split()

            if "FAILED" in line.upper() and parts:
                ip_address = parts[-1]
                failed_ips[ip_address] += 1

    print("\n=== Security Log Analysis ===")
    print(f"Total log entries: {total_lines}")
    print(f"Failed login entries: {sum(failed_ips.values())}")

    print("\nFailed login attempts by IP:")
    for ip, count in failed_ips.most_common():
        print(f"{ip}: {count}")

    if not failed_ips:
        print("No failed login attempts found.")


if __name__ == "__main__":
    analyze_logs("sample_logs.txt")

