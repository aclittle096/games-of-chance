import random
import time

money = 100
max_money = money

def coin_flip(bet):
    global money, max_money

    print('Now playing Coinflip . . .')
    print_sleep("", 1)

    winning_choice = ''
    cpu = random.randint(1,2)
    if cpu == 1: winning_choice = "heads"
    else: winning_choice = "tails"

    choice = input("Heads or Tails? ").lower()

    if ("heads" not in choice) and ("tails" not in choice):
        print('Hmm, it appears you didn\'t select Heads or Tails.')
        print('Try again!')
        print()
        coin_flip(bet)
    else:
        timer()
        if choice in winning_choice: win(bet)
        else: lose(bet)

    max_money_check()

def cho_han(bet):
    global money, max_money

    print('Now playing Cho Han . . .')
    print_sleep("", 1)

    winning_choice = ''
    cpu = random.randint(1,6) + random.randint(1,6)
    if cpu % 2 == 0: winning_choice = 'even'
    else: winning_choice = 'odd'

    choice = input("Even or Odd?").lower()

    if ("even" not in choice) and ("odd" not in choice):
        print('Hmm, it appears you didn\'t select Even or Odd.')
        print("Try again!")
        print()
        cho_han(bet)
    else:
        timer()
        if choice in winning_choice: win(bet)
        else: lose(bet)

    max_money_check()

def rand_card(bet):
    global money, max_money

    print('Now playing Highest Card . . .')
    print_sleep("", 1)
    
    print_sleep("Choosing your card. . .", 1)
    you = random.randint(1,13)
    if you == 1: print("You have chosen an Ace.")
    elif you < 10: print("You have chosen a " + str(you) + ".")
    elif you == 11: print("You have chosen a Jack!")
    elif you == 12: print("You have chosen a Queen!")
    else: print("You have chosen a King!")
    time.sleep(1)

    print_sleep("Choosing your opponent's card. . .", 1)
    timer()
    cpu = random.randint(1,13)
    if cpu == 1: print("They have chosen an Ace.")
    elif cpu < 10: print("They have chosen a " + str(you) + ".")
    elif cpu == 11: print("They have chosen a Jack!")
    elif cpu == 12: print("They have chosen a Queen!")
    else: print("They have chosen a King!")
    time.sleep(1)

    if you > cpu: win(bet)
    elif you < cpu: lose(bet)
    else:
        print('It seems there was a tie! No one has won or lost money.')
        print()
        time.sleep(3)

    max_money_check()

def roulette(bet):
    global money, max_money

    print('Now playing Roulette . . .')
    print_sleep("", 1)

    winning_choice = ''
    cpu = random.randint(0,38)
    if cpu == 0: winning_choice = 'Zero'
    elif cpu % 2 == 0: winning_choice = 'Even'
    else: winning_choice = 'Odd'

    choice = input("Zero, even, or odd?").lower()

    if ("even" not in choice) and ("odd" not in choice) and ("zero" not in choice) and ("0" not in choice):
        print("Hmm, it appears you didn't select zero, even, or odd.")
    else:
        print_sleep("Spinning the wheel . . .", 1)
        timer()
        if choice == winning_choice: win(bet)
        else: lose(bet)

    max_money_check()
    
def win(bet):
    global money, max_money

    print("Congratulations, you won $" + str(bet) + "!")
    money += bet
    print()
    time.sleep(3)

def lose(bet):
    global money, max_money

    print("Sorry, you lost $" + str(bet) + ".")
    money -= bet
    print()
    time.sleep(3)

def max_money_check():
    global money, max_money
    if money > max_money: max_money = money

def print_sleep(s, t):
    print(s)
    time.sleep(t)

def timer():
    print_sleep("3", 1)
    print_sleep("2", 1)
    print_sleep("1", 1)

def closer(total):
    if total > 1000000: 
        print("Absolutely spectacular. I think you're set for a whlie!")
    elif total > 100000:
        print("Incredible job. You might just be able to break the million-dollar mark at this rate!")
    elif total > 10000:
        print("Great stuff! That's a respectable amount.")
    elif total > 1000:
        print("Not bad! Keep it up, and you might just be able to make some serious cash.")
    else:
        print("I think there's some room for improvement here, but don't lose hope! Keep up the great work.")

#------------------------------------------------------------------------

print_sleep("Hello and welcome to the games of chance!", 2)
print_sleep("With a starting pool of $100, see how much money you can amass.", 2)
print_sleep("Good luck!", 2)
print()

while money > 0:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Current balance: $' + str(money))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Games list:')
    print('1. Coinflip')
    print('2. Cho Han')
    print('3. Highest Card')
    print('4. Roulette')

    # acquring bet
    bet = input('First, choose a bet: ')
    try:
        bet = int(bet)
        if bet < 1:
            print("You can't bet less than $1. Try again!")
            print()
            time.sleep(2)
            continue
    except ValueError:
        print('Now now, that\'s not a number. Try again!')
        print()
        time.sleep(2)
        continue

    # acquring game choice
    g_choice = input('Enter a number corresponding to the game you want to bet on: ')
    try:
        g_choice = int(g_choice)
        if (g_choice < 1) or (g_choice > 4):
            print('Now now, that\'s not an acceptable number. Try again!')
            print()
            time.sleep(2)
            continue
    except ValueError:
        print('Now now, that\'s not a number. Try again!')
        print()
        time.sleep(2)
        continue

    print()

    # playing selected game
    if g_choice == 1: coin_flip(bet)
    elif g_choice == 2: cho_han(bet)
    elif g_choice == 3: rand_card(bet)
    else: roulette(bet)

print_sleep('It appears you have run out of funds.', 2)
print('You managed to amass a maximum of $' + str(max_money) + '.')
time.sleep(2)
closer(max_money)
time.sleep(2)