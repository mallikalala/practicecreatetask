restaurants = [ "In N Out","Panda Express","McDonalds", "Subway", "PHS Cafeteria"]

new_restaurant = input("What restaurant would you like to add to the list.")

girble = "Din Tai Fung"

for x in restaurants :
  preference1 = input("Do you like A) " + new_restaurant + " or B) " +  x + " more?")
  if preference1 == "B":
    girble = x
    break
  if preference1 == "A" and x == restaurants[4]:
    girble = 5
    break

print (girble)

index = girble
print(index)
if index == 4:
  restaurants.append(new_restaurant)
  print("mr tran")
else:
  restaurants.insert(index,new_restaurant)

print(restaurants)
print(girble)