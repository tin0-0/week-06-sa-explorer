province = {
        "name": "gauteng",
        "capital": "Johannesburg",
        "population": 16100000,
        "area": 18176,
        "languages": ["Afrikaans", "English", "isiZulu", "isiXhosa"]
    }

# print(type(province))

print(province["name"])#accessing values in a dictionary using keys
#update

province["population"]= 16500000#updating values in a dictionary using keys
print(province["population"])

province["languages"]= ["Afrikaans", "English", "isiZulu", "isiXhosa", "Sesotho"]#updating values in a dictionary using keys
print(province)

print(province["languages"][0])#accessing values in a nested dictionary using keys and index

for key,value in province.items():
    print(f"{key}: {value}")

# print(province.get("city", "N/A"))

if "capital" in province:
    print("Capital is in the dictionary")

print(list(province.keys()))#getting a list of all keys in the dictionary
print(list(province.values()))#getting a list of all values in the dictionary