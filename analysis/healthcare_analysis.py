import csv
from statistics import mean

file_path = "data/healthcare_sample.csv"

# Load the dataset
with open(file_path, newline="", encoding="utf-8") as file:
    data = list(csv.DictReader(file))

# Extract numerical data
wait_times = [int(row["wait_time_minutes"]) for row in data]
satisfaction = [int(row["satisfaction_score"]) for row in data]

print("=" * 45)
print("        HEALTHCARE DATA ANALYSIS")
print("=" * 45)

# Overall summary
print("\nOVERALL SUMMARY")
print("-" * 30)

print(f"Number of patient records: {len(data)}")
print(f"Average waiting time: {mean(wait_times):.1f} minutes")
print(f"Average satisfaction score: {mean(satisfaction):.1f}/5")
print(f"Longest waiting time: {max(wait_times)} minutes")
print(f"Shortest waiting time: {min(wait_times)} minutes")

# Department analysis
print("\nDEPARTMENT SUMMARY")
print("-" * 30)

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
        f"{len(department_rows)} visits | "
        f"Average wait: {department_wait:.1f} minutes | "
        f"Average satisfaction: "
        f"{department_satisfaction:.1f}/5"
    )

# Visit type analysis
print("\nVISIT TYPE SUMMARY")
print("-" * 30)

visit_types = sorted(set(row["visit_type"] for row in data))

for visit_type in visit_types:
    visit_rows = [
        row for row in data
        if row["visit_type"] == visit_type
    ]

    visit_wait = mean(
        int(row["wait_time_minutes"])
        for row in visit_rows
    )

    visit_satisfaction = mean(
        int(row["satisfaction_score"])
        for row in visit_rows
    )

    print(
        f"{visit_type}: "
        f"{len(visit_rows)} visits | "
        f"Average wait: {visit_wait:.1f} minutes | "
        f"Average satisfaction: "
        f"{visit_satisfaction:.1f}/5"
    )

# Simple interpretation
print("\nKEY OBSERVATIONS")
print("-" * 30)

highest_wait_department = max(
    departments,
    key=lambda department: mean(
        int(row["wait_time_minutes"])
        for row in data
        if row["department"] == department
    )
)

highest_satisfaction_department = max(
    departments,
    key=lambda department: mean(
        int(row["satisfaction_score"])
        for row in data
        if row["department"] == department
    )
)

print(
    f"The department with the highest average waiting time "
    f"is {highest_wait_department}."
)

print(
    f"The department with the highest average satisfaction "
    f"score is {highest_satisfaction_department}."
)

print("\nAnalysis complete.")