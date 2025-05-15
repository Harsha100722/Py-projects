menu = {
    'popcorn': 120,
    'pizza': 140,
    'coke': 30,
    'puff': 45
}

cart = []
total = 0

while True:
    user = input("Enter your choice of food from menu (q to quit): ").lower()
    if user == 'q':
        print("Quitting...")
        break
    elif user in menu:
        cart.append(user)
    else:
        print("Item not in menu. Please try again.")

print("Items in your cart:", cart)

for item in cart:
    total += menu.get(item)

print("Total bill:", total)
