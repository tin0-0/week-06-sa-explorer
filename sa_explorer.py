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
provinces = ["gauteng", 
                "western cape", 
                "kwazulu-natal", 
                "eastern cape", 
                "free state", 
                "limpopo", 
                "mpumalanga", 
                "northern cape", 
                "north west"]
province = input("Please enter the name of a South African province: ").lower()
gauteng_population = 16100000
gauteng_area = 18176

western_cape_population = 7100000
western_cape_area = 129462

kwazulu_natal_population = 11500000
kwazulu_natal_area = 94361

eastern_cape_population = 6700000
eastern_cape_area = 168966

free_state_population = 2900000
free_state_area = 129825

limpopo_population = 5800000
limpopo_area = 125754

mpumalanga_population = 4500000
mpumalanga_area = 76495

northern_cape_population = 1200000
northern_cape_area = 372889

north_west_population = 4100000
north_west_area = 104882

if province == "gauteng":
    print("Capital: Johannesburg")
    print(f"Population: {gauteng_population:,}")
    print(f"Area: {gauteng_area:,} km²")
    print("Languages: Afrikaans, English, isiZulu, isiXhosa")
elif province == "western cape":
    print("Capital: Cape Town")
    print(f"Population: {western_cape_population:,}")
    print(f"Area: {western_cape_area:,} km²")
    print("Languages: Afrikaans, English, isiXhosa")
elif province == "kwazulu-natal":
    print("Capital: Durban")
    print(f"Population: {kwazulu_natal_population:,}")
    print(f"Area: {kwazulu_natal_area:,} km²")
    print("Languages: isiZulu, English, Afrikaans")
elif province == "eastern cape":
    print("Capital: Bhisho")
    print(f"Population: {eastern_cape_population:,}")
    print(f"Area: {eastern_cape_area:,} km²")
    print("Languages: isiXhosa, Afrikaans, English")
elif province == "free state":
    print("Capital: Bloemfontein")
    print(f"Population: {free_state_population:,}")
    print(f"Area: {free_state_area:,} km²")
    print("Languages: Afrikaans, English, isiZulu")
elif province == "limpopo":
    print("Capital: Polokwane")
    print(f"Population: {limpopo_population:,}")
    print(f"Area: {limpopo_area:,} km²")
    print("Languages: Sepedi, Xitsonga, Afrikaans, English")
elif province == "mpumalanga":
    print("Capital: Nelspruit")
    print(f"Population: {mpumalanga_population:,}")
    print(f"Area: {mpumalanga_area:,} km²")
    print("Languages: isiZulu, Afrikaans, English, isiXhosa")
elif province == "northern cape":
    print("Capital: Kimberley")
    print(f"Population: {northern_cape_population:,}")
    print(f"Area: {northern_cape_area:,} km²")
    print("Languages: Afrikaans, English, isiXhosa")
elif province == "north west":
    print("Capital: Mahikeng")
    print(f"Population: {north_west_population:,}")
    print(f"Area: {north_west_area:,} km²")
    print("Languages: Setswana, Afrikaans, English")
else:
    print("Province not found. Please check your spelling and try again.")

explore_again = input("Would you like to explore another province? (yes/no): ")
if explore_again.lower() == "yes":
    province = input("Please enter the name of a South African province: ").lower()
  

