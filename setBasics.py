food={"apple","mango","lichi","banana","lichi"}
veg={"potato","tomato","chilli","lichi","banana"}

print(food)
print(veg)
# sets do not enretain duplicacy

emptyset= set()
print(type(emptyset))
print(type(food))

#adding & removing

food.add("kunafa")
print(food)
food.remove("apple")
print(food)
veg.pop("potato")
print(veg)
food.union(veg)
print(food)
food.intersection(veg)
print(food)
