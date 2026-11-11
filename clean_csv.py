import csv
import json
from datetime import datetime

seen = set()
clean_rows = []
total = 0

with open("messy.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += 1
        clean = {key: value.strip() for key, value in row.items()}
        if clean["name"] == "":
            continue
        key = (clean["name"], clean["age"], clean["joined"])
        if key in seen:
            continue
        seen.add(key)
        try:
            datetime.strptime(clean["joined"], "%Y-%m-%d")
        except ValueError:
            continue
        try:
            clean["age"] = int(clean["age"])
        except ValueError:
            continue
        clean_rows.append(clean)

with open("clean.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "joined"])
    writer.writeheader()
    writer.writerows(clean_rows)

summary = {
    "total_rows": total,
    "clean_rows": len(clean_rows),
    "dropped_rows": total - len(clean_rows),
}

with open("summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("Wrote", len(clean_rows), "clean rows to clean.csv")
print("Summary:", summary)

