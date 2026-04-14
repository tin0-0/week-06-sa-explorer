# def calculate_vat(amount,rate=0.15):
#     return amount * rate


# amount = int (input("Amount Excl:"))
# vat_amount = calculate_vat(amount)

def calculate_vat(price, rate=0.15):
    # TODO: return price * rate
    return price * rate


def calculate_total(price, rate=0.15):
    # TODO: return price + VAT
    return price + calculate_vat(price, rate)

def format_zar(amount):
    # TODO: return formatted string like "R1,500.00"
    return (f"R{amount:,.2f}")

price = int(input("Price Excl: "))
vat_amount = calculate_vat(price)
total_amount = calculate_total(price)
print(f"VAT: {format_zar(vat_amount)}")
print(f"Total: {format_zar(total_amount)}")