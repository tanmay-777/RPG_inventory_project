import time
inventory = []
player_gold = 100

potions = {
    'Healing Potion' : 20,
    'Mana Elixir' : 40, 
    'Greater Healing Potion' : 50,
}
prompt = "Please Enter the specified key to browse the shop or exit it\n"
prompt += "[1] View Shop, [2] Buy Item, [3] View Inventory, [4] Exit\n"
prompt_inshop = "[2] Buy Item, [4] Exit\n"

game_loop = True


while game_loop:
    time.sleep(0.8)
    player_input = input(prompt)
    if player_input == '1':
        print("Items and their Price (In gold)\n")
        for item,price in potions.items():
            print(f"{item} for {price}\n")
    elif player_input == '2':
        player_input = input("Please specifiy the item name you want to buy!\n")
        if player_input.title() == 'Healing Potion' and player_gold >= 20:
            print("Congratulations! you bought a Healing potion\n")
            player_gold-=20
            inventory.append('Healing Potion')
            player_input = '3'
        elif player_input.title() == 'Greater Healing Potion' and player_gold >= 50:
            player_gold-=50
            print("Congratulations! you bought a Greater Healing potion\n")
            inventory.append('Greater Healing Potion')
            player_input = '3'
        elif player_input.title() == 'Mana Elixir' and player_gold >= 40:
            print("Congratulations! you bought a Mana Elixir\n")
            inventory.append('Mana Elixir')
            player_gold-=40
            player_input = '3'
        else:
            print("Error enter valid name/Ran out of gold!")
        if player_input == '3':
            for item in inventory:
                print(f'You currently have {item}\n')
            time.sleep(0.8)
            print(f'Remaning gold balance: {player_gold}')
    elif player_input == '3':
        for item in inventory:
            print(f'You currently have {item}\n')
        time.sleep(0.8)
        print(f'Remaning gold balance: {player_gold}')
    elif player_input == '4':
        game_loop = False
    else:
        print('Please Enter a Valid 1-4 input')
