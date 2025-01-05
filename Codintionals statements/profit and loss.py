actual_cost=int(input("Enter the actual cost of the product: "))
sale_price=int(input("Enter the sale price of the product:"))
if sale_price  > actual_cost:
    amount=sale_price-actual_cost
    print("Profit ={0}".format(amount))
else:
    print("no profit:")