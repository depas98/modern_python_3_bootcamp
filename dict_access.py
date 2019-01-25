from random import choice
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

item = bakery_stock.get(food)
if item is None:
    print("We don't make that")
else:
    print(f"{item} left")

# Or

if item:
    print(f"{item} left")
else:
    print("We don't make that")

# Or
if food in bakery_stock:
    print(f"{item} left")
else:
    print("We don't make that")


game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo",
                   "enemies_on_screen", "enemy_kills", "enemy_kill_streaks",
                   "minutes_played", "notifications", "achievements"]

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result
# to a variable called initial_game_state
initial_game_state = {}.fromkeys(game_properties, 0)
print(initial_game_state)

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}

stock_list = inventory.copy()
stock_list.update(dict(cookie=18))
stock_list.pop("cake")
print(stock_list)

# better way to add an item
stock_list["eggs"] = 20
print(stock_list)
