# SA CSV Validator
# Your Task
# Build a program that reads a CSV file and validates every row, reporting errors gracefully instead of crashing.

# Requirements
# Read students.csv (columns: name, age, email, province)
# For each row, check: age is a valid number, province is one of the 9 SA provinces
# Collect valid rows and error rows separately
# Print: how many valid, how many errors, list each error with line number and reason
# Use try/except for type conversion errors

provinces = ["Gauteng", "Western Cape", "KwaZulu-Natal", "Eastern Cape", "Free State", "Limpopo", "Mpumalanga", "North West", "Northern Cape"]
for files in ["student.csv"]:
    with open(files, "r") as f:
        lines = f.readlines()[1:]  # Skip header
        valid_rows = []
        error_rows = []
        for i, line in enumerate(lines, start=2):  # Start at line 2
            fields = line.strip().split(",")
            if len(fields) != 4:
                error_rows.append((i, "Incorrect number of fields"))
                continue
            name, age_str, email, province = fields
            try:
                age = int(age_str)
            except ValueError:
                error_rows.append((i, "Invalid age"))
                continue
            if province not in provinces:
                error_rows.append((i, "Invalid province"))
                continue
            valid_rows.append((name, age, email, province))
        
        print(f"Valid rows: {len(valid_rows)}")
        print(f"Errors: {len(error_rows)}")
        for line_num, reason in error_rows:
            print(f"Line {line_num}: {reason}")