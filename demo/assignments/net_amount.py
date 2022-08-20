# Accept quantity and price and display net amount.
# If quantity is more than 3, discount is 30%, otherwise it is 20%.
# Add a tax of 10%

quantity = int(input("Enter Quantity: "))
price = float(input("Enter price: "))
gross_amount = price * quantity

if quantity > 3:
    discount = gross_amount * 0.3
else:
    discount = gross_amount * 0.2

after_discount = gross_amount - discount
tax = float(after_discount * 0.1)
net_amount = after_discount + tax

print(f"Amount             {gross_amount:10.2f}")
print(f"- Discount         {discount:10.2f}")
print(f"                   {'-' * 10}")
print(f"After Discount     {after_discount:10.2f}")
print(f"+ Tax              {tax:10.2f}")
print(f"                   {'-' * 10}")
print(f"Net Amount         {net_amount:10.2f}")
