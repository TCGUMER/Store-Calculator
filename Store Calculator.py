foods = []
prices = []
total = 0

while True:
    food = input("Please enter the food name :").lower()
    if food == 'q':
        break
    else:
        price = float(input(f"please enter the price of {food} $ :"))
        foods.append(food)
        prices.append(price)


print("-----------------")
print("CHECKOUT")        
print("-----------------")   

print("Food :",end=' ')
for food in foods:
    print(food,end=' ')

print("")
for price in prices:
    total += price

print(f"Your total price is {total}")        














