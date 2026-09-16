import csv
from statistics import mean

file_path = "data/healthcare_sample.csv"

with open(file_path, newline="", encoding="utf-8") as file:
    data = list(csv.DictReader(file))

wait_times = [int(row["wait_time_minutes"]) for row in data]
satisfaction = [int(row["satisfaction_score"]) for row in data]

print("HEALTHCARE DATA ANALYSIS")
print("-" * 30)

print(f"Number of patient records: {len(data)}")
print(f"Average waiting time: {mean(wait_times):.1f} minutes")
print(f"Average satisfaction score: {mean(satisfaction):.1f}/5")
print(f"Longest waiting time: {max(wait_times)} minutes")
print(f"Shortest waiting time: {min(wait_times)} minutes")

print("\nDepartment Summary")
departments = sorted(set(row["department"] for row in data))

for department in departments:
    department_rows = [
        row for row in data
        if row["department"] == department
    ]

    department_wait = mean(
        int(row["wait_time_minutes"])
        for row in department_rows
    )

    department_satisfaction = mean(
        int(row["satisfaction_score"])
        for row in department_rows
    )

    print(
        f"{department}: "
        f"{len(department_rows)} visits, "
        f"average wait {department_wait:.1f} minutes, "
        f"average satisfaction {department_satisfaction:.1f}/5"
    )