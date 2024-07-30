dict =  {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) +' '+ k)
        item_total = item_total + v
    print('total number of items : ' + str(item_total))



def addToInventory(inventory, addedItems):
    for index,item in enumerate(addedItems):
        #
        if item not in inventory.keys():
            inventory.setdefault(item,1)
        else:
            inventory[item] = inventory[item] + 1
    return inventory

displayInventory(dict)

inv = addToInventory(dict, dragonLoot)
displayInventory(inv)







