# Exchange Rates to USD
NGN = 1358.68
EGP = 53.11
CFA = 559.19

# User input
amount = int(input("Enter value:"))
in_cur = input("Input currency type (NGN, EGP, CFA):").upper()
out_cur = input("Output currency type (NGN, EGP, CFA):").upper()

# Convert to USD
if in_cur == "NGN":
    USD_value = amount / NGN
elif in_cur == "EGP":
    USD_value = amount / EGP
elif in_cur == "CFA":
    USD_value = amount / CFA

# Convert from USD to Output currency
if out_cur == "NGN":
    Afr_value = USD_value * NGN
elif out_cur == "EGP":
    Afr_value = USD_value * EGP
elif out_cur == "CFA":
    Afr_value = USD_value * CFA
else:
    print("Invalid output currency")
    exit()

# Output
print("Converted amount:", Afr_value)

