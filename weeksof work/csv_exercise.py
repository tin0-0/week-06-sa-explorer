import csv
from os import write

with open("sa_census.csv") as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header
    for row in reader:
     print(row)

with open ("sa_census.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        #print(f"{row['name']:20}: population {int(row['population']):>12}")
        if int(row["area_km2"]) > 100000:
           write.out f"{row['name']} has an area of {row['area_km2']} km2\n"

