def display_inventory(inventory):
    print('Inventory List: ')
    item_total = 0
    for stuff, n in inventory.items(): 
        print(str(n) + ' ' + str(stuff))
        item_total += n
    print('item total: ' + str(item_total))

def add_to_inventory(inventory, gotten_items): #引数はinventory(辞書型)とgotten_items(リスト型)
    for i in gotten_items:
        inventory.setdefault(i, 0) #１つも持っていなったアイテムを追加
        inventory[i] += 1
    return(inventory) #辞書を返す

dragon_loot = ['gold coin', 'dirk', 'gold coin', 'gold coin', 'ruby']
inventory = {'rope':1, 'gold coin': 42}

new_inventory = add_to_inventory(inventory, dragon_loot)

display_inventory(new_inventory)
