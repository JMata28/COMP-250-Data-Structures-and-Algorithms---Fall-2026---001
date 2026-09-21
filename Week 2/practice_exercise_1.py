name = input("Please enter your name: ").title().strip()
drink = input("What drink would you like: ").upper().strip()
price = float(input("Enter the price: ").strip())
amount = int(input(f"Enter the amount of {drink}S that you want: ").strip())
tip_percent = float(input("Enter the tip percentage amount: ").strip())

tax_percent = 0.0625

print("\n\n\tBSU COFFEE SHOP")
print(f"\tCostumer: {name}\n\tOrder: {amount} x {drink}")
print(f"\tItem code: {drink[:3]} - {len(drink)}")
subtotal = price * amount
print(f"\tSubtotal: ${subtotal}")
tax = subtotal*tax_percent
print(f"\tTax: ${tax:.2f}")
tip = subtotal*tip_percent/100
print(f"\tTip: ${tip:.2f}")
print(f"\tTOTAL: ${(subtotal + tax + tip):.2f}")

print(f"\tThanks {name}, come back soon!")