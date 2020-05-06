def display_inventory(inventory):
    print('Inventory List: ')
    item_total = 0
    for stuff, n in inventory.items(): #こう書くことでstuffにキーを、nにバリューを順番に代入できる。
        print(str(n) + ' ' + str(stuff))
        item_total += n
    print('item total: ' + str(item_total))
inventory = {'rope':1, 'torch':6, 'gold coin': 42, 'dirk':1, 'arrow':12}
display_inventory(inventory)
