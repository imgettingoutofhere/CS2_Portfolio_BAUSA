# Exercise 1: My School Bag

school_items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]

print("School supplies in the bag: ")
print(school_items[0])
print(school_items[1])
print(school_items[2])
print(school_items[3])
print(school_items[4])

# Exercise 2: Travel Destination Manager

destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

print("All travel destinations: ")
for place in destinations:
  print(place)

print(destinations[1:4])

search = input("Enter a destination: ")
if search in destinations:
  print("Found!")
else:
  print("Not found.")

destinations[2] = "Iloilo"
print(destinations)
