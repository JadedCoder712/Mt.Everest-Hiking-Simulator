rations=0
clothes=0
icepicks=0
tents=0
fuel=0
water=0
thehike=1
falseHolder=True
truthHolder=True
thehike=1
while truthHolder is True:
    gamemenu=input("Welcome to Kathmandu! You may: Press 1 to Start the Hike, press 2 to learn more about the trek up Mt. Everest, press 3 to see the map of the Mt. Everest trek, or press 4 to quit the program.")
    if gamemenu is "2":
        input("The hike up Mount Everest is a long and difficult journey. It is filled with Hazards and danger. Type OK to continue.")
    if gamemenu is "3":
        input("This part of the Mount Everest Trail is under contruction right now. Press Enter to continue.")
    if gamemenu is "4":
        raise SystemExit("Goodbye")
    if gamemenu is "1":
        truthHolder=False
while truthHolder is False:
    playertype=input("Many people attempt to hike Everest each year. Who are you? You may be: 1. A CEO from America, 2. An accountant from England, 3. A scientist from Australia. Press 4 to learn more about these choices and how they affect the game.")
    if playertype is "4":
        input("The type of person you are affects how much money you have. For instance, a CEO will have more money than an accountant or scientist. However, if you choose the CEO, this will reduce your score at the end of the game. Press Enter to continue.")
    if playertype is "1":
        money=10,000
        truthHolder=True
    if playertype is "2":
        money=7,000
        truthHolder=True
    if playertype is "3":
        money=6,500
        truthHolder=True
while truthHolder is True:ttruthholderuthHolderr=False
if store is "1":
    while truthHolder is False:truthHoldertruthholder=True
if itemmenu is "1":
    falseHolder=True
    while falseHolder is True:
        stortruthHolder("Welcome to Mt. Everest Equipment Store! We sell at the lowest prices in all of the Himalayas. We sell: 1. Rations, 2. Clothes, 3. Ice picks, 4. Tents, 5. Fuel, 6. Water, 7. Review what you already have, 8. Leave store. What would you like to buy/choose?")
        if storemenu is "1":
            rationsloop=True
            while rationsloop is True:
                rationsinp=input("Rations are sold in packs of ten. How many packs of rations would you like to buy at $14 each?")
                maxrations=round(money-(int(rationsinp)*14))
                if maxrations < 0:
                    input("You do not have enough money to buy all those! Press Enter to continue.")
                if maxrations >= 0:
                    rations=rations+(int(rationsinp)*10)
                    money=money-(int(rationsinp)*14)
                    endlessloop=True
                    while endlessloop is True:
                        rationsmenu=input("You have {0} dollars left. Press: 1. to buy more rations, 2. Go back to store, 3. Leave the store.".format(money))
                        if rationsmenu is "1":
                            endlessloop=False
                        if rationsmenu is "2":
                            rationsloop=False
                        if rationsmenu is "3":
                            areyousure=input("Are you sure you would like to leave the store and stop buying supplies?")
                            if areyousure is "yes":
                                falseHolder=False
                    
        """
        if storemenu is "2":
            
        if storemenu is "3":
            
        if storemenu is "4":
            
        if storemenu is "5":
            
        if storemenu is "6":
            
        if storemenu is "7":
            
        if storemenu is "8":
            """
            
        
if thehike==1:
    input("The hike will continue from here.")
    
            
            
            
            
            