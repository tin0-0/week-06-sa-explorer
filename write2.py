with open("weather.csv", "r") as f:
    lines = f.readlines()[1:]  # Skip header
    with open("weather.txt", "w") as out:
        out.write("Weather Summary Report\n")
        out.write("=" * 30 + "\n")
        for line in lines:
            fields = line.strip().split(",")
            out.write(f"{fields[0]} on  {fields[1]}: {fields[2]}C\n")
        out.write(f"\nTotal records: {len(lines)}\n")