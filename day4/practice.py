#Dictionaries practices
house = {
    "price": 165000000,
    "bedrooms": 20,
    "bathrooms": 23,
    "square_footage": 28660,
    "address": "67 Beverely Park Ct, ",
    "year_built": 1999, 
}

#Get values
print(house['price'])
print(house.get("square_footage"))

#Change Values
house['price'] = 100000
print(f"Price: {house['price']}")



my_house = {
    "year_built": 1910,
    "price": 79000000,
    "squareft": 20000,
    "price_per_sqft":3950,
    "address": "12 E 69t St, New York, NY 10021",
    "bed": 6,
    "bath": 8,

}

print(my_house['price'])
print(my_house.get('address'))

house['price'] = (int(my_house['price']+9000000))
print(f"The originial asking price was ${house['price']}")