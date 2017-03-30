import sys
truthholder=True
while truthholder is True:
    gamemenu=input("Welcome to Kathmandu! You may: Press 1 to Start the Hike, press 2 to learn more about the trek up Mt. Everest, press 3 to see the map of the Mt. Everest trek, or press 4 to quit the program.")
    if gamemenu is "2":
        input("The hike up Mount Everest is a long and difficult journey. It is filled with Hazards and danger. Type OK to continue.")
    if gamemenu is "3":
        input("This part of the Mount Everest Trail is under contruction right now. Press Enter to continue.")
    if gamemenu is "4":
        sys.exit(0)
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
