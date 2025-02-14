from random import randint as rint
from time import sleep as slp
from os import system as sys

#ask how much u want to bet
#do 5 rounds and whoever wins gets the money
#check if money is less then or = 0
#double or nothing button

money = 10

ai_money = money
you_money = money
bet = 0

print(f"Rules!:\nYou start with {money}$ and are able to bet however much you want\nIt will be You vs an AI\nYou will both randomly get a number between 1 and 20\nEhoever has the bigger number wins that round\nBest out if 5 rounds\n")

def Bet():
    global ai_money
    global you_money
    global bet
    if you_money <= 0:
        print("You Lose!!!")
        exit()
    elif ai_money <= 0:
        print("You Win!!!")
        exit()
    print("Your Money:", you_money)
    print("Ai Money:", ai_money)
    while True:
        bet = int(input("How much u wanna bet?: "))
        if bet < 1:
            print("Too small of a number")
        elif bet > you_money:
            print("You do not have that kind of money")
        else:
            break
    sys("clear")
    print("")
    ai_bet = bet
    bets = bet + ai_bet
    you_money = you_money - bet
    ai_money = ai_money - bet
    ai_wins = 0
    you_wins = 0
    
    for i in range(5):
        ai = rint(1, 20)
        you = rint(1, 20)
        if ai == you:
            print("Tie!")
            slp(0.1)
        elif ai > you:
            print("Ai Wins!")
            ai_wins += 1
            slp(0.1)
        elif ai < you:
            print("You Win!")
            you_wins += 1
            slp(0.1)
        else:
            print("idk")
        print("Ai:", ai)
        print(f"You: {you}\n")
    if ai_wins == you_wins:
        print("Tie! we shall go again...")
        you_money = you_money + bet
        ai_money = ai_money + bet
        slp(0.2)
        Bet()
    elif ai_wins > you_wins:
        print("You Lose! Womp womp")
        ai_money += bets
        print("Your money now:", you_money)
        print("The Ai's Money now:", ai_money)
        if you_money <= 0:
            user = input("Double or nothing? y/n: ").lower()
            if user != "y":
                exit()
            else:
                DoubleOrNothing()
        Bet()
    elif ai_wins < you_wins:
        print("You Win!!!")
        you_money += bets
        print("Your money now:", you_money)
        print("The Ai's Money now:", ai_money)
        if ai_money <= 0:
            print("You Win the whole Game!")
            exit()
        user = input("Go again? y/n: ").lower()
        if user != "y":
            exit()
        else:
            sys("clear")
            Bet()
######
####
#####
def DoubleOrNothing():
    global ai_money
    global you_money
    global bet
    global money
    sys("clear")
    ai_wins = 0
    you_wins = 0
    for i in range(5):
        ai = rint(1, 20)
        you = rint(1, 20)
        if ai == you:
            print("Tie!")
            slp(0.3)
        elif ai > you:
            print("Ai Wins!")
            ai_wins += 1
            slp(0.3)
        elif ai < you:
            print("You Win!")
            you_wins += 1
            slp(0.3)
        else:
            print("bug with for loop in double or nothing")
        print("Ai:", ai)
        print(f"You: {you}\n")
    if ai_wins == you_wins:
        print("Since its Double or Nothing... A Tie = You LOSE!")
        exit()
    elif ai_wins > you_wins:
        print("You LOSE!!!")
        exit()
    elif you_wins > ai_wins:
        print("You WON!!!")
        you_money = bet * 2
        ai_money = money
        user = input("Play Again or keep the money?\nPlay y/n: ")
        if user != "y":
            exit()
        else:
            Bet()
Bet()