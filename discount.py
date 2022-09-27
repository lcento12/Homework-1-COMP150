def discount():
    price = int(input("Enter a price: "))
    discount = int(input("Enter a discount percentage: "))
    final = ((1 - 'price'/100)*'discount')
    print(final)
