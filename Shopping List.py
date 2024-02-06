item_names = []
item_quantities = []
item_prices = []
total_cost = 0
for i in range(10):
    item=str(input('Enter item Name; '))
    if item=='exit':
        break
    item_names.append(item)
    quantity=int(input('Enter Quantity; '))
    item_quantities.append(quantity)
    price=eval(input('Enter Price of item; '))
    item_prices.append(price)
    total_cost += item_quantities[i] * item_prices[i]
print("Shopping list:")
for i in range(len(item_names)):
    print(f"{item_names[i]}: {item_quantities[i]} x ${item_prices[i]}")
print(f"Total cost: ${total_cost}")
budget = 2000
if budget >= total_cost:
    print()
    print("You have enough budget to buy everything on your list.")
    print()
else:
    print()
    print("You do not have enough budget to buy everything on your list.")
    print()