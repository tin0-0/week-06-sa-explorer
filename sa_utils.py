def calculate_vat(price, rate=0.15):
    return round(price * rate, 2)

def valiudate_sa_id(id_number):
    if len (id_number) != 13:
        return False
    if not id_number.isdigit():
        return False
    return True


def format_zar(amount):
    return f"R {amount:,.2f}"