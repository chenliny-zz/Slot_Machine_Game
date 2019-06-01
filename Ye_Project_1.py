class Player:
    """This is the main player in the casino. 
    It takes a name and strores attributes and actions of that player."""
    
    # Each player object will be initiated with $0 balance
    # If a player is a registered guest, then saved balance 
    # amount will be passed in uopon guest verification
    def __init__(self, username, passcode, balance=0):  
        self.username = username
        self.passcode = passcode
        self.__balance = balance
        
    @property     
    def balance(self):
        return self.__balance

    @balance.setter
    def set_balance(self, amount):
        self.__balance = amount
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError

            

class SlotMachine:
    
    from IPython.display import clear_output
    """This is the brain of the slot machine."""
    def __init__(self, player, jackpot=1000000):
        self.player = player
        self.jackpot = jackpot
        self.reels = []
    
    def center_message(self, text, width=70):
        """A function to print centered messages."""
        symbol = "=" * width
        pad = (width + len(text)) // 2
        return "{0}\n{1:>{2}}\n{0}".format(symbol, text, pad) 
    
    def spin_wheels(self, bet_amount, symbol_pool=[]):
        self.bet_amount = bet_amount
        self.symbol_pool = symbol_pool
        
        import random
        import time
        from IPython.display import clear_output
        
        banana = u"\U0001F34C"
        peach = u"\U0001F351"
        watermelon = u"\U0001F349"
        money = u"\U0001F4B0"
        free = u"\U0001F193"
        slot = u"\U0001F3B0"
        
        # Adjust probability based on bet amount
        if self.bet_amount == 0.1:
            self.symbol_pool.extend(banana*15)  
            self.symbol_pool.extend(peach*6)
            self.symbol_pool.extend(watermelon*6)
            self.symbol_pool.extend(money)
            self.symbol_pool.extend(slot*3)
        if self.bet_amount == 2:
            self.symbol_pool.extend(banana*7)
            self.symbol_pool.extend(peach*10)
            self.symbol_pool.extend(watermelon*10)
            self.symbol_pool.extend(money)
            self.symbol_pool.extend(slot*3)
        if self.bet_amount == 5:
            self.symbol_pool.extend(banana*4)
            self.symbol_pool.extend(peach*8)
            self.symbol_pool.extend(watermelon*8)
            self.symbol_pool.extend(money)
            self.symbol_pool.extend(slot*10)
        
        r1 = random.choice(self.symbol_pool)
        r2 = random.choice(self.symbol_pool)
        r3 = random.choice(self.symbol_pool)
        
        self.reels = [r1, r2, r3]
        
        for reel_num, reel in zip([1,2,3],self.reels):
            for letter in 'No.{} REEL DISPLAYS {}\n'.format(reel_num, reel):
                time.sleep(0.02)
                print(letter, end="")

        time.sleep(1)
        clear_output()
        print(self.center_message("The results for this round is: {}--{}--{}").format(self.reels[0], 
                                                                                      self.reels[1], 
                                                                                      self.reels[2]))
        return self.reels
    
    def pay_out(self, reels):
        """Function to calculate payouts based on reel symbols."""
        self.reels = reels
        
        banana = u"\U0001F34C"
        peach = u"\U0001F351"
        watermelon = u"\U0001F349"
        money = u"\U0001F4B0"
        free = u"\U0001F193"
        slot = u"\U0001F3B0"
       
        win = 0
        if self.reels.count(banana) == 3:
            win = 1
        elif self.reels.count(peach) == 3:
            win = 5
        elif self.reels.count(watermelon) == 3:
            win = 10
        elif self.reels.count(slot) == 3 :
            win = self.jackpot
        else:
            if self.reels.count(peach) == 2:
                win += 2
            if self.reels.count(watermelon) == 2:
                win += 5
            if self.reels.count(money) > 0:
                win += self.reels.count(money)*10
        return win

    
    
class Casino:
    """The Casino class houses the backbone of the game."""
    
    def __init__(self, player):
        """Takes a player object and get game components ready."""
        self.player = player
        
        #Initialize necessary classes 
        self.slot_machine = SlotMachine(self.player)
        
        # The user_list attribute of the Casino class used for user verification
        # The casino gives its guests $50 credit to start with
        self.guest_list = {
            "gerry benoit": {"Passcode": 1234, "Balance": 50},
            "tolu adesanya": {"Passcode": 1234, "Balance": 50},
            "swati akella": {"Passcode": 1234, "Balance": 50},
            "nick cirella": {"Passcode": 1234, "Balance": 50},
            "teddy fong": {"Passcode": 1234, "Balance": 50},
            "ed hott": {"Passcode": 1234, "Balance": 50},
            "satoshi iriyama": {"Passcode": 1234, "Balance": 50},
            "tom martinez": {"Passcode": 1234, "Balance": 50},
            "matt mcElhaney": {"Passcode": 1234, "Balance": 50},
            "andrew morris": {"Passcode": 1234, "Balance": 50},
            "hongsuk nam": {"Passcode": 1234, "Balance": 50},
            "arnaldo tavares Filho": {"Passcode": 1234, "Balance": 50},
            "chenlin ye": {"Passcode": 1234, "Balance": 50}
        }
        
        # Menu options
        self.choices = {
            "1": "check balance",
            "2": "spin wheels",
            "3": "make deposit",
            "4": "withdraw cash",
            "5": "exit"
        }
        
        # Bet amount options
        self.bet_amount = {
            "1": 0.1,
            "2": 2,
            "3": 5,
        }    
    
    def center_message(self, text, width=70):
        """Function to print centered messages."""
        symbol = "=" * width
        pad = (width + len(text)) // 2
        return "{0}\n{1:>{2}}\n{0}".format(symbol, text, pad)
    
    def display_menu(self):
        """A static method to diaplay menu."""
        menu = """
        Slot Machine Menu
        
        [1]: Check Balance
        [2]: Make Bet & Spin
        [3]: Make a Deposit
        [4]: Withdraw Cash
        [5]: Quit
        """
    
        print()
        print()
        print(u"\U0001F3B0"*30)
        print(menu)
        print(u"\U0001F3B0"*30)
        
    def verify_guest(self, username, passcode):
        """Function to verify if the user-inputed guest is a hotel guest."""
        if self.player.username not in self.guest_list.keys():
            return "Name mismatch"
        elif self.player.passcode != self.guest_list[self.player.username]["Passcode"]:  
            return "Passcode mismatch"
        return "Verified guest"
    
    # This is meant for Casino use only when it needs to add new guests
    def create_account(self, username, passcode):
        """Function to add new guests."""
        if username not in self.guest_list.keys():
            self.guest_list.update({username:{"Passcode": passcode, "Balance": 50}})
        else:
            return "Username already exists."
    
    def start(self):
        from IPython.display import clear_output
        """Function to start the game only if verify_guest() returns favorable outcome."""
        if self.verify_guest(self.player.username, self.player.passcode) == "Name mismatch":
            print("Sorry, {} is not a registered user at our casino. The slot machine cannot be initiated.".format(self.player.username))
            print("Please contact the customer service department at xxx-xxx-xxxx for further assistance.")
            print("Have a wonderful day!")
        elif self.verify_guest(self.player.username, self.player.passcode) == "Passcode mismatch":
            print("Sorry, the passcode you have entered does not match our records for {}".format(self.player.username))
            print("Please start the initiation process and try again.")
        else:
            # Game starts 
            # Balance will be passed in here if the user passes the verification
            self.player.set_balance = self.guest_list[self.player.username]["Balance"]
            
            # Opening line
            opening_line = """Welcome to the casino, {name}. We are thrilled to have you here today!""".format(name="Chenlin")
            print(u"\U0001F4B0"*3, self.center_message(opening_line), u"\U0001F4B0"*3)
            input("Press Enter to continue...")
            clear_output()

            # Instructions
            instructions = "\nWe know you can't wait to place your first bet, but why don't we first \nget acquinted with how the " + \
            "system works?\n\nOn the slot machine, you will be guided through our menus \nto navigate through various options." + \
            "You can make a bet, \ndeposit funds, withdraw available funds, or quit the game.\n\nThere are 5 different symbols on " + \
            "each reel: {b} {p} {w} {m} {s}\nWinning combinations consist the following...\n\n{b}--{b}--{b}: $1\n\n{p}--{p}: $2\n\n{p}--{p}--{p}: "\
            .format(b=u"\U0001F34C", p=u"\U0001F351", w=u"\U0001F349", m=u"\U0001F4B0", s=u"\U0001F3B0") + \
            "$5\n\n{w}--{w}: $5\n\n{w}--{w}--{w}: $10\n\n{s}--{s}--{s}: THE JACKPOT!!!!!\n\n{m}: $10 bonus for each money bag\n"\
            .format(b=u"\U0001F34C", p=u"\U0001F351", w=u"\U0001F349", m=u"\U0001F4B0", s=u"\U0001F3B0") + \
            "\n\nAnd remember, the higher your bet amount is for each spin, \nthe more likely you will get {p} {w} or even {s}\n"\
            .format(p=u"\U0001F351", w=u"\U0001F349", s=u"\U0001F3B0")
            print(u"\U0001F3B0"*3, self.center_message(instructions), u"\U0001F3B0"*3)
            
            input("Press Enter to continue...")
            clear_output()
            
            while True:
                
                self.display_menu()
                choice = input("Please choose an action item from the following: ")
                action = self.choices.get(choice)
                
                if action == "check balance":
                    clear_output()
                    print (self.center_message("Hi {}, your current balance is: ${:,}".format(self.player.username, self.player.balance)))
                
                elif action == "spin wheels":
                    clear_output()
                    
                    while True:
                        
                        print(self.center_message("""
                        Bet Options:
                        [1]: for $0.1
                        [2]: for $2
                        [3]: for $5
                        """))
                        
                        amount = self.bet_amount.get((input("How much would you like to bet: ")))
                        if amount in [0.1, 2, 5]:
                            self.player.set_balance = self.player.balance - amount
                            self.slot_machine.spin_wheels(amount)
                            win_amount = self.slot_machine.pay_out(self.slot_machine.reels)
                            self.player.set_balance = self.player.balance + win_amount
                            print(self.center_message("You won ${:,}, and your current balance is ${:,}".format(win_amount, 
                                                                                                                self.player.balance)))
                            break
                        else:
                            clear_output()
                            print(self.center_message("You have entered an invalid bet amount. Please select from 1 to 3."))
        
                elif action == "make deposit":
                    clear_output()
                    try:
                        amount = float(input("How much would you like to deposit?"))
                        self.player.deposit(amount)
                        print(self.center_message("${:,} had been successfully deposited to your account. Your current balance is ${:,}".format(amount, 
                                                                                                                                                 self.player.balance)))
                    except:
                        print("You have entered an invalid value. Please make sure to enter a numeric value.")
                
                elif action == "withdraw cash":
                    clear_output()
                    try:
                        amount = float(input("How much would you like to withdraw?"))
                        clear_output()
                        self.player.withdraw(amount)
                        print(self.center_message("${:,} had been withdrawn. Your current balance is ${:,}".format(amount, 
                                                                                                                   self.player.balance)))
                    except:
                        print("The maximum amount you can withdraw is ${:,}. Please make sure to enter a numeric value that's equal or less than ${}".format(amount, self.player.balance))
                
                elif action == "exit":
                    clear_output()
                    print(self.center_message("Thank you for visiting, {}. We hope to see you again soon!".format(self.player.username)))
                    break
                
                else:
                    clear_output()
                    print("You have made an invalid selection. Please make sure to select from 1 to 5 in the menu.")


# Initiate the game here    
# Only W200 Wednesday 6:30 session students with passcode 1234 will pass the verification
guest_name = input("Please input username: ").lower()
guest_passcode = int(input("Please input passcode: "))

player = Player(guest_name, guest_passcode)
game = Casino(player)
game.start()