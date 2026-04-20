'''SA Math Toolkit — Start Building the Deliverable'''
def claculate_vat(price ,rate=0.15):
    return (price * rate)

def sa_tax_bracket(annual_income):
    """
    Returns the 2025/2026 SA income tax bracket details.
    Note: This is the raw tax before rebates.
    """
    if annual_income <= 237100:
        return "Bracket 1: 18% of taxable income"
    elif annual_income <= 370500:
        return "Bracket 2: R42,678 + 26% of income above R237,100"
    elif annual_income <= 512800:
        return "Bracket 3: R77,362 + 31% of income above R370,500"
    elif annual_income <= 673000:
        return "Bracket 4: R121,475 + 36% of income above R512,800"
    elif annual_income <= 857900:
        return "Bracket 5: R179,147 + 39% of income above R673,000"
    elif annual_income <= 1817000:
        return "Bracket 6: R251,258 + 41% of income above R857,900"
    else:
        return "Bracket 7: R644,489 + 45% of income above R1,817,000"
