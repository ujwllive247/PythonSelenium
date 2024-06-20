
menu = {
    'Pizza': 40,
    'Burger':50,
    'Salad' :35,
    'Coffee':45
}


print("Welcome to the python project")

print("Pizza :Rs40\nBurger:Rs50\nSalad:Rs35\nCoffee:45")

order_total = 0

item_1 = input("Enter the item =")

if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your order{item_1} added to the card")

else:
    print(f"item {item_1} is not available")

another_order = input("Do you want to order something more ? Yes/No")


if another_order =="Yes":
    item_2 =input("Enter the name of second item = ")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to order")

    else:
        print(f"Ordered item {item_2} is not available")

print(f"The total amount of items is {order_total}")







