price = int(input("Enter price : "))

if price > 5000:
    discount = price * 0.20
else:
    discount = price * 0.10

net_price = price - discount
print('Net price =', net_price)
