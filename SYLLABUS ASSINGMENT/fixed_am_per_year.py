# Program to calculate depreciation using percentage

amt = float(input("Enter purchase value of the asset: "))
year = int(input("Enter years of service: "))
rate = float(input("Enter depreciation rate (%): "))

depreciation = (amt * rate * year) / 100
current_value = amt - depreciation

print("Depreciation =", depreciation)
print("Current Value of Asset =", current_value)