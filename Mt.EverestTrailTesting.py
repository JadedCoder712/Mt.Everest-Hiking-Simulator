rations=0
clothes=0
icepicks=0
tents=0
fuel=0
water=0
thehike=1
falseholder=True
truthholder=True
thehike=1
while truthholder is True:
    gamemenu=input("Welcome to Kathmandu! You may: Press 1 to Start the Hike, press 2 to learn more about the trek up Mt. Everest, press 3 to see the map of the Mt. Everest trek, or press 4 to quit the program.")
    if gamemenu is "2":
        input("The hike up Mount Everest is a long and difficult journey. It is filled with Hazards and danger. Type OK to continue.")
    if gamemenu is "3":
        input("This part of the Mount Everest Trail is under contruction right now. Press Enter to continue.")
    if gamemenu is "4":
        raise SystemExit("Goodbye")
    if gamemenu is "1":
        truthholder=False
while truthholder is False:
    playertype=input("Many people attempt to hike Everest each year. Who are you? You may be: 1. A CEO from America, 2. An accountant from England, 3. A scientist from Australia. Press 4 to learn more about these choices and how they affect the game.")
    if playertype is "4":
        input("The type of person you are affects how much money you have. For instance, a CEO will have more money than an accountant or scientist. However, if you choose the CEO, this will reduce your score at the end of the game. Press Enter to continue.")
    if playertype is "1":
        money=10,000
        truthholder=True
    if playertype is "2":
        money=7,000
        truthholder=True
    if playertype is "3":
        money=6,500
        truthholder=True
while truthholder is True:
    store=input("You will need to buy supplies for the expedition. Press 1 to go to the store, or press 2 to go on the hike without supplies.")
    if store is "2":
        areyousure=input("Are you sure? The hike up Mount Everest is long and dangerous, and there will not be too many opportunities to buy supplies during the hike. Please type 'yes' or 'no' to confirm your choice.")
        if areyousure is "yes":
            thehike=1
            truthholder=False
    if store is "1":
        truthholder=False
if store is "1":
    while truthholder is False:
        itemmenu=input("You have {0} rations, {1} sets of clothes, {2} ice picks, {3} tents, {4} canisters of fuel, and {5} liters of water. 1. Go to store, 2. Learn more about each item.".format(rations, clothes, icepicks, tents, fuel, water)) 
        if itemmenu is "2":
            input("Rations are what keep you alive. Without rations, your health will get worse. Clothes are what keep you warm. If they get wet, you will need a new set of clothes. If you do not change clothes or dry your clothes, you will get cold and your health will get worse. Ice picks help you scale ice walls. Ice picks break, so you will need to make sure to have some at all times. Tents are what you sleep in. These can break, and if they do and you not repair it or get a new one, you cannot sleep. Fuel is what you use to heat up rations to eat, as well as to melt snow to make water. Water is another necessary element to survive. Press Enter to continue.") 
        if itemmenu is "1":
            truthholder is True
if itemmenu is "1":
    falseholder=True
    while falseholder is True:
        storemenu=input("Welcome to Mt. Everest Equipment Store! We sell at the lowest prices in all of the Himalayas. We sell: 1. Rations, 2. Clothes, 3. Ice picks, 4. Tents, 5. Fuel, 6. Water. What would you like to buy?")
        
if thehike==1:
    
            
            
            
            
            