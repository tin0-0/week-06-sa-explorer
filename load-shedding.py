stage = int(input("Enter load-shedding stage: "))
time = str(input("Enter time: "))
if stage <= 0 or stage > 8:
    print("Invalid stage. Please enter a number between 1 and 8.")
elif stage <= 2:
    print(f"stage : {stage}- Mild load-shedding.")
    print("Advice: keep edvices charged just incase of load-shedding.")

elif stage <= 4:
    print(f"stage : {stage}- Moderate load-shedding.")
    print("Advice:charge all devices and make sure to have lights on stand by.")

elif stage <= 6:
    print(f"stage : {stage}- Severe load-shedding.")
    print("Advice: Cook meals in advance and make sure to have enough water.")

elif stage <=7:
    print(f"stage : {stage}- Extreme load-shedding.")
    print("Advice: Stay indoors and avoid using elevators and use gas stoves if possible.")