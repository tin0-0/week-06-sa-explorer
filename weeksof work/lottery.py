import random

def generate_ticket():
    # TODO: 6 unique numbers from 1-52, sorted
    return sorted(random.sample(range(1, 53), 6))

def format_ticket(numbers):
    # TODO: "| 05 | 12 | ... |" format
    return " | ".join(f"{num:02d}" for num in numbers)

def count_matches(ticket, winning):
    # TODO: count matching numbers
    return len(set(ticket) & set(winning))

print("Welcome to the Lottery!")

print(format_ticket(generate_ticket()))
winning = generate_ticket()
print(count_matches(ticket, winning))