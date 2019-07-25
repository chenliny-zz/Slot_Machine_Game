class Player:
    """
    This is the main player in the casino.
    It takes a name and strores attributes and actions of that player.
    Each player object will be initiated with $0 balance.
    If a player is a registered guest, then saved balance amount will be
    passed in upon guest verification
    """

    def __init__(self, username, rm_num, balance=0):
        self.username = username
        self.rm_num = rm_num
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
    """This is the brain of the slot machine."""

    from IPython.display import clear_output
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
        probability = {
            0.1: [15, 6, 6, 1, 3],
            2: [7, 10, 10, 1, 3],
            5: [4, 8, 8, 1, 10]
        }

        reel_item = [banana, peach, watermelon, money, slot]

        self.symbol_pool.extend(reel * num
                                for reel, num
                                in zip(reel_item, probability[self.bet_amount]))

        self.symbol_pool =[symbol for subset in self.symbol_pool for symbol in subset]
        self.reels = [random.choice(self.symbol_pool) for x in range(3)]

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
        # The casino gives its registered guests $50 credit to start with
        self.guest_list = {
            "Jupyter Notebook": {"rm_num": 8888, "Balance": 50},
            "Hello World": {"rm_num": 1234, "Balance": 50},
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

    def verify_guest(self, username, rm_num):
        """Function to verify if the user-inputed guest is a hotel guest."""
        if self.player.username not in self.guest_list.keys():
            return "Name mismatch"
        elif self.player.rm_num != self.guest_list[self.player.username]["rm_num"]:
            return "Room Number mismatch"
        return "Verified guest"

    # This is meant for Casino use only when it needs to add new guests
    def create_account(self, username, rm_num):
        """Function to add new guests."""
        if username not in self.guest_list.keys():
            self.guest_list.update({username:{"rm_num": rm_num, "Balance": 50}})
        else:
            return "Username already exists."

    def start(self):
        from IPython.display import clear_output
        """Function to start the game"""

        if self.verify_guest(self.player.username, self.player.rm_num) == "Name mismatch":
            print("Hi {}, seems like you are a visitor to our casino. Welcome!".format(self.player.username.upper()),
                "A new visitor account with a cmplementary balance of $10 had been created for you.")
            self.player.set_balance = 10
        elif self.verify_guest(self.player.username, self.player.rm_num) == "Room Number mismatch":
            print("The room number you have entered does not match our records for {}".format(self.player.username.upper()))
            print("A visitor account had been initiated with a complementary balance of $10")
            self.player.set_balance = 10
        else:
            # Balance will be passed in here if the user passes the verification
            self.player.set_balance = self.guest_list[self.player.username]["Balance"]

        # Opening line
        opening_line = """{name}, we are thrilled to have you here today!""".format(name=self.player.username.upper())
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
                print (self.center_message("Hi {}, your current balance is: ${:,}".format(self.player.username.upper(), self.player.balance)))

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
                        if self.player.balance < amount:
                            print(self.center_message("You do not have enough balance left. Please make a deposit to place the bet."))
                        else:
                            self.player.set_balance = self.player.balance - amount
                            self.slot_machine.spin_wheels(amount)
                            win_amount = self.slot_machine.pay_out(self.slot_machine.reels)
                            self.player.set_balance = self.player.balance + win_amount
                            print(self.center_message("You won ${:,}, and your current balance is ${:,}".format(win_amount, self.player.balance)))
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
                print(self.center_message("Thank you for visiting, {}. We hope to see you again soon!".format(self.player.username.upper())))
                break

            else:
                clear_output()
                print("You have made an invalid selection. Please make sure to select from 1 to 5 in the menu.")


# Initiate the game here

def main():
    """Initiates the game"""
    
    while True:
        guest_name = input("Please input Guest Name: ").lower()
        if guest_name.isdigit() or guest_name == "":
            print("Please enter a valid name")
            continue
        else:
            break

    while True:
        try:
            guest_rm_num = int(input("Please input room number: "))
        except:
            print("please enter a valid room number")
            continue
        else:
            break

    player = Player(guest_name, guest_rm_num)
    game = Casino(player)
    game.start()

if __name__ == '__main__':
    main()
