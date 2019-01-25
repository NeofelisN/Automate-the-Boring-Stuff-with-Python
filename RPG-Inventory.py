# This function adds the loot to the inventory and confirms it has been added.
def addToInventory(inv, addedItems):
    # Create dictionary for adding
    add_dict = {}
    # Fill dictionary with new items
    for i in addedItems:
        add_dict.setdefault(i, 0)
        add_dict[i] = add_dict[i] + 1
    # Add new items:
    #   If already exists in inventory, then add
    #   Else, create a new item with the number
    for k in add_dict.keys():
        inv.setdefault(k, 0)
        inv[k] = inv[k] + add_dict[k]
    print(' - - - - - - - - - - - -')
    print('The items have been added to your inventory.')
    print()
    return inv

# This function displays the current inventory.
def displayInventory(inventory):
    print(' - - - - - - - - - - - -')
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(' - ' + str(v) + ' ' + str(k))
        item_total = item_total + int(v)
    print('Total number of items: ' + str(item_total))
    print()

# This function congratulates the player for geeting loot and shows what items they have won.
def congratulate(loot):
    print(' - - - - - - - - - - - -')
    print('You have slain the dragon! you have won the following items:')
    d_loot = {}
    for i in loot:
        d_loot.setdefault(i, 0)
        d_loot[i] = d_loot[i] + 1
    item_total = 0
    for k, v in d_loot.items():
        print(' - ' + str(v) + ' ' + str(k))
        item_total = item_total + int(v)
    print()

####################################################

# Current stuff and dragon loot to be added.
stuff = {'rope' : 1, 'torch' : 6, 'gold coin' : 42, 'dagger' : 1, 'arrow' : 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Congratulate and show loot.
congratulate(dragonLoot)

# Add loot to inventory and confirm.
stuff = addToInventory(stuff, dragonLoot)

# Show inventory
displayInventory(stuff)
