# OOP_Slot_Machine_Game

***
Chenlin Ye

OOP Sample Project

chenliny@berkeley.edu
***

The general idea behind the project is a slot machine game that mimics player and slot machine interactions in a casino. When the player initiates the game, he/she would need to input his/her name and room number for verification. If the player is a verified guest, he/she will have $50 starting balance. If the player is a visitor, he/she will have $10 starting balance. The player can then choose what actions he/she wants to take and corresponding consequences will be reflected in the player’s account. 

There are three classes in the program: Player, SlotMachine, and Casino. Casino acts as the central brain of the game, making the SlotMachine class instances and the Player class instances interact with each other. Under the spin_wheels() method of a SlotMachine object, there is be a random symbol generator and a selection algorithm for each reel on the slot machine. Probability of certain symbol being drawn will be set based on the player’s bet amount.

**To run the game**, simply execute the ye_slot_machine_game.py file. The on-screen instructions will guide you through the game. There are two special guests in the casino, Jupyter Notebook who lives in Rm 8888, and Hello World, who lives in Rm 1234, just saying...

Have fun!
---------

Here is a break-down of the three classes:

1. Player (username, rm_num, balance = 0)
   - Attributes:
     - balance
    
   - Methods:
     -	set_balance(amount)
     -	deposit(amount)
     -	withdraw(amount)



2. SlotMachine (player, jackpot = 1000000)
   - Attributes:
     -	reels
    
   - Static method:
     -	center_message(text, width)
    
   - Methods:
     -	spin_wheels(bet_amount, symbol_pool)
     -	pay_out(reels)
    
    
    
3. Casino (player)
   - Attributes: 
     -	guest_list
     -	menu options
     -	bet_amount options
 
   - Static method:
     -	center_message(text, width)

   - Methods:
     -	display_menu()
     -	verify_guest(username, rm_num)
     -   create_account(username, rm_num)
     -	start()
