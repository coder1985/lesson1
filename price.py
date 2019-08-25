def discounted (price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount

product = {'name': 'BMW', 'stock': 50, 'price': 1500000, 'discount': 20}
product['with_discount'] = discounted (product['price'], product['discount'])
print(product['with_discount'])