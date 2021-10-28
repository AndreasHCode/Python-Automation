inventory = {"apple": 3, "sword": 1, "arrow": 55, "gold": 155}

def displayInventory(inv):
    print("Inventory")
    totalItems = 0
    for k, v in inv.items():
        print("Key: " + k + ", Value: " + str(v))
        totalItems += inv.get(k, 0)
    print("Total items: " + str(totalItems))

def addToInventory(inv, loot):
    print("Adding Loot to Inventory: " + str(loot))
    for key in loot:
        inv.setdefault(key, 0)
        inv[key] += 1

displayInventory(inventory)

dragonLoot = ["apple", "gold", "gold", "gold", "banana"]
addToInventory(inventory, dragonLoot)
addToInventory(inventory, dragonLoot)

displayInventory(inventory)
