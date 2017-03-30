rations=0
clothes=0
ice_picks=0
tents=0
fuel=0
water=0
the_hike=1
false_holder=True
truth_holder=True
the_hike=1
while truth_holder is True:
    game_menu=input("Welcome to Kathmandu! You may: Press 1 to Start the Hike, press 2 to learn more about the trek up Mt. Everest, press 3 to see the map of the Mt. Everest trek, or press 4 to quit the program.")
    if game_menu is "2":
        input("The hike up Mount Everest is a long and difficult journey. It is filled with Hazards and danger. Type OK to continue.")
    if game_menu is "3":
        input("This part of the Mount Everest Trail is under contruction right now. Press Enter to continue.")
    if game_menu is "4":
        raise SystemExit("Goodbye")
    if game_menu is "1":
        truth_holder=False
while truth_holder is False:
    player_type=input("Many people attempt to hike Everest each year. Who are you? You may be: 1. A CEO from America, 2. An accountant from England, 3. A scientist from Australia. Press 4 to learn more about these choices and how they affect the game.")
    if player_type is "4":
        input("The type of person you are affects how much money you have. For instance, a CEO will have more money than an accountant or scientist. However, if you choose the CEO, this will reduce your score at the end of the game. Press Enter to continue.")
    if player_type is "1":
        money=10,000
        truth_holder=True
    if player_type is "2":
        money=7,000
        truth_holder=True
    if player_type is "3":
        money=6,500
        truth_holder=True
while truth_holder is True:
    store=input("You will need to buy supplies for the expedition. Press 1 to go to the store, or press 2 to go on the hike without supplies.")
    if store is "2":
        are_you_sure=input("Are you sure? The hike up Mount Everest is long and dangerous, and there will not be too many opportunities to buy supplies during the hike. Please type 'yes' or 'no' to confirm your choice.")
        if are_you_sure is "yes":
            the_hike=1
            truth_holder=False
    if store is "1":
        truth_holder=False
if store is "1":
    while truth_holder is False:
        item_menu=input("You have {0} rations, {1} sets of clothes, {2} ice picks, {3} tents, {4} canisters of fuel, and {5} liters of water. 1. Go to store, 2. Learn more about each item.".format(rations, clothes, ice_picks, tents, fuel, water)) 
        if item_menu is "2":
            input("Rations are what keep you alive. Without rations, your health will get worse. Clothes are what keep you warm. If they get wet, you will need a new set of clothes. If you do not change clothes or dry your clothes, you will get cold and your health will get worse. Ice picks help you scale ice walls. Ice picks break, so you will need to make sure to have some at all times. Tents are what you sleep in. These can break, and if they do and you not repair it or get a new one, you cannot sleep. Fuel is what you use to heat up rations to eat, as well as to melt snow to make water. Water is another necessary element to survive. Press Enter to continue.") 
        if item_menu is "1":
            truth_holder=True
if item_menu is "1":
    false_holder=True
    while false_holder is True:
        store_menu=input("Welcome to Mt. Everest Equipment Store! We sell at the lowest prices in all of the Himalayas. We sell: 1. Rations, 2. Clothes, 3. Ice picks, 4. Tents, 5. Fuel, 6. Water, 7. Review what you already have, 8. Leave store. What would you like to buy/choose?")
        if store_menu is "1":
            rations_loop=True
            while rations_loop is True:
                rations_inp=input("Rations are sold in packs of ten. How many packs of rations would you like to buy at $14 each?")
                max_rations=round(money-(int(rationsinp)*14))
                if max_rations < 0:
                    input("You do not have enough money to buy all those! Press Enter to continue.")
                if max_rations >= 0:
                    rations=rations+(int(rations_inp)*10)
                    money=money-(int(rations_inp)*14)
                    endless_loop=True
                    while endless_loop is True:
                        rations_menu=input("You have {0} dollars left. Press: 1. to buy more rations, 2. Go back to store, 3. Leave the store.".format(money))
                        if rations_menu is "1":
                            endless_loop=False
                        if rations_menu is "2":
                            rations_loop=False
                        if rations_menu is "3":
                            are_you_sure=input("Are you sure you would like to leave the store and stop buying supplies?")
                            if are_you_sure is "yes":
                                false_holder=False
                    
        """
        if store_menu is "2":
            
        if store_menu is "3":
            
        if store_menu is "4":
            
        if store_menu is "5":
            
        if store_menu is "6":
            
        if store_menu is "7":
            
        if store_menu is "8":
            """
            
        
if the_hike==1:
    input("The hike will continue from here.")
            
            
            