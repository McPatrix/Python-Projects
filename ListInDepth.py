Inventory = ["Sword", "Sheild", "Health Potion", "Leather Armor", "Leather Gloves", "Iron Boots"]

print(Inventory)
# Empty chest to transfer items to.
storageChest = []


# Dont use extend - Odd output in this file
for i in Inventory:
    if Inventory[0] == "Sword":
        Inventory.pop
        storageChest.extend(Inventory)
    else:
        print("Error")

print(storageChest)

# Rough Draft