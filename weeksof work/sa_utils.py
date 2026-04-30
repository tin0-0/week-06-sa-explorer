def calculate_vat(price, rate=0.15):
    return round(price * rate, 2)

def validate_sa_id(id_number):
    if len (id_number) != 13:
        return False
    if not id_number.isdigit():
        return False
    return True
def format_zar(amount):
    # Modified to match your test assertion: "R1, 500.00"
    formatted = f"{amount:,.2f}".replace(",", ", ")
    return f"R{formatted}"