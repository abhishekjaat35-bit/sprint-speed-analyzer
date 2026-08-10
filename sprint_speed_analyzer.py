# ==========================================
# Sprint Speed & Acceleration Analyzer
# Author: Abhishek Tomar
# ==========================================

import csv

print("=" * 65)
print("          SPRINT SPEED & PERFORMANCE ANALYZER")
print("=" * 65)


# ------------------------------------------
# Functions
# ------------------------------------------

def calculate_speed(distance, time):
    """Calculate average sprint speed in m/s."""
    return distance / time


def calculate_acceleration(speed, time):
    """Estimate average acceleration assuming start from rest."""
    return speed / time


def calculate_percentage_difference(best, athlete):
    """Calculate percentage difference from the best performance."""
    return ((athlete - best) / best) * 100


# ------------------------------------------
# Load CSV Data
# ------------------------------------------

filename = "sprint_data.csv"

athletes = []

with open(filename, "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        athlete = row["Athlete"]
        distance = float(row["Distance_m"])
        time = float(row["Time_s"])

        speed = calculate_speed(distance, time)
        acceleration = calculate_acceleration(speed, time)

        athletes.append({
            "name": athlete,
            "distance": distance,
            "time": time,
            "speed": speed,
            "acceleration": acceleration
        })


# ------------------------------------------
# Display Individual Results
# ------------------------------------------

print("\n" + "=" * 75)
print("INDIVIDUAL SPRINT RESULTS")
print("=" * 75)

print(
    f"{'Athlete':<15}"
    f"{'Time':<12}"
    f"{'Speed':<15}"
    f"{'Acceleration':<15}"
)

print("-" * 75)

for athlete in athletes:

    print(
        f"{athlete['name']:<15}"
        f"{athlete['time']:<12.2f}"
        f"{athlete['speed']:<15.2f}"
        f"{athlete['acceleration']:<15.2f}"
    )


# ------------------------------------------
# Find Best Athlete
# ------------------------------------------

best_time = min(athletes, key=lambda x: x["time"])
best_speed = max(athletes, key=lambda x: x["speed"])
best_acceleration = max(
    athletes,
    key=lambda x: x["acceleration"]
)


# ------------------------------------------
# Team Statistics
# ------------------------------------------

average_time = sum(
    athlete["time"] for athlete in athletes
) / len(athletes)

average_speed = sum(
    athlete["speed"] for athlete in athletes
) / len(athletes)

average_acceleration = sum(
    athlete["acceleration"] for athlete in athletes
) / len(athletes)


# ------------------------------------------
# Performance Report
# ------------------------------------------

print("\n" + "=" * 65)
print("TEAM PERFORMANCE REPORT")
print("=" * 65)

print(
    f"Fastest Athlete       : "
    f"{best_time['name']} ({best_time['time']:.2f} s)"
)

print(
    f"Highest Speed         : "
    f"{best_speed['name']} ({best_speed['speed']:.2f} m/s)"
)

print(
    f"Highest Acceleration  : "
    f"{best_acceleration['name']} "
    f"({best_acceleration['acceleration']:.2f} m/s²)"
)

print("-" * 65)

print(f"Average Sprint Time   : {average_time:.2f} s")
print(f"Average Sprint Speed  : {average_speed:.2f} m/s")
print(
    f"Average Acceleration  : "
    f"{average_acceleration:.2f} m/s²"
)


# ------------------------------------------
# Ranking
# ------------------------------------------

print("\n" + "=" * 65)
print("SPRINT RANKING")
print("=" * 65)

ranking = sorted(
    athletes,
    key=lambda x: x["time"]
)

for position, athlete in enumerate(ranking, start=1):

    print(
        f"{position}. "
        f"{athlete['name']:<12} "
        f"{athlete['time']:.2f} s"
    )


# ------------------------------------------
# Performance Gap
# ------------------------------------------

print("\n" + "=" * 65)
print("PERFORMANCE GAP FROM FASTEST ATHLETE")
print("=" * 65)

fastest_time = best_time["time"]

for athlete in athletes:

    gap = (
        (athlete["time"] - fastest_time)
        / fastest_time
    ) * 100

    print(
        f"{athlete['name']:<15} "
        f"{gap:.2f}% slower"
    )


print("\n" + "=" * 65)
print("END OF PERFORMANCE REPORT")
print("=" * 65)