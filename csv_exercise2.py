import csv


with open("sa_census.csv") as f:
    provinces = list(csv.DictReader(f))
    print(provinces)
