'''
1. Real World Python Dictionary Applications

Task 1: Restaurant Menu Update

Problem Statement:
Given the initial menu restaurant_menu:
  - Add a new category called "Beverages" with at least two items.
  - Update the price of "Steak" to 17.99.
  - Remove "Bruschetta" from "Starters".
'''

restaurant_menu = {
  "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
  "Main Course": {"Steak": 15.99, "Salmon": 13.99},
  "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Hot Coffee": 2.99, "Iced Coffee": 3.99}
restaurant_menu["Main Course"]["Steak"] = 17.99
del restaurant_menu["Starters"]["Bruschetta"]

print(restaurant_menu)
