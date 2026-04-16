from sa_utils import calculate_vat, format_zar, validate_sa_id

assert calculate_vat(100) == 15.0

#assert calculate_vat(100) == 99.0

assert calculate_vat(0) == 0.0
assert calculate_vat(100, 0.10) == 10.0

#format ZAR tests

assert format_zar(1500) == "R1,500.00"
assert format_zar(0) == "R0.00"

#validate_sa_id tests
assert validate_sa_id("9501015009087") == True
assert validate_sa_id("123") == False

print("All tests passed!")