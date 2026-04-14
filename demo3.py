from sa_utils import calculate_vat, validate_sa_id, format_zar

price = 199.99
vat = calculate_vat(price)
total = price + vat

print(f"Price: {format_zar(price)}")
print(f"VAT: {format_zar(vat)}")
print(f"Total: {format_zar(total)}")

test_id = "950612345678"
if validate_sa_id(test_id):
    print(f"{test_id} is valid.")
else:
    print(f"{test_id} is invalid.")