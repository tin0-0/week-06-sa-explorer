#1. Print welcome message
#2. Print numbered list of 9 provinces
#3. Ask user to type a province name
#4. Convert input to lowercase (for case-insensitive matching)
#5. Use if/elif/else to match province
#6. If matched: print capital, population, area, languages
#7. If not matched: print "Province not found"
#8. Ask "Explore another? (yes/no)"
#9. If yes: go back to step 3

print("Welcome to the South African Province Explorer!")
provinces = {
    "GP": {
            "province":"Gauteng",
            "Capital": "Johannesburg",
            "population": "16100000",
            "area": "18176",
            "languages": ["Afrikaans", "English", "isiZulu", "isiXhosa"]
    },
    "WC": {
            "province":"Western Cape",
            "Capital": "Cape Town",
            "population": "7100000",
            "area": "129462",
            "languages": ["Afrikaans", "English", "isiXhosa"]
    },
    "KZN": {
            "province":"KwaZulu-Natal",
            "Capital": "Durban",
            "population": "11500000",
            "area": "94361",
            "languages": ["isiZulu", "English", "Afrikaans"]
    },
    "EC": {
            "province":"Eastern Cape",
            "Capital": "Bhisho",
            "population": "6700000",
            "area": "168966",
            "languages": ["isiXhosa", "Afrikaans", "English"]
    },
    "FS": {
            "province":"Free State",
            "Capital": "Bloemfontein",
            "population": "2900000",
            "area": "129825",
            "languages": ["Afrikaans", "English", "isiZulu"]
    },
    "LP": {
            "province":"Limpopo",
            "Capital": "Polokwane",
            "population": "5800000",
            "area": "125754",
            "languages": ["Sepedi", "Xitsonga", "Afrikaans", "English"]
    },
    "MP": {
            "province":"Mpumalanga",
            "Capital": "Nelspruit",
            "population": "4500000",
            "area": "76495",
            "languages": ["isiZulu", "Afrikaans", "English", "isiXhosa"]
    },
    "NC": {
            "province":"Northern Cape",
            "Capital": "Kimberley",
            "population": "1200000",
            "area": "372889",
            "languages": ["Afrikaans", "English", "isiXhosa"]
    },
    "NW": {
            "province":"North West",
            "Capital": "Mahikeng",
            "population": "4100000",
            "area": "104882",
            "languages": ["Setswana", "Afrikaans", "English"]
    }
}
while True:
    province = input("Please enter the code of a South African province: ").lower()
  
    if province in provinces:
        print(provinces[province])
    else:
        print("Province not found.")


   
