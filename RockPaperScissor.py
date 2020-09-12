import random as r

print("Welcome to the Game")

def player():
    playerChoice="blank"
    while not (playerChoice==playerChoice == "r" or playerChoice== "p" or playerChoice == "s"):
        playerChoice=input("Enter your choice\n"
                            "r for Rock\n"
                            "p for Paper\n"
                            "s for Scissor\n")
        print("Your choice : ",playerChoice)
    return playerChoice

def bot():
    lst=['r','p','s']
    a=r.choice(lst)
    print("Bot  choice : ",a)
    return a



def winner(x,y):
    if x=='r' and y=='r':
        return 0
    elif x=='r' and y=='p':
        return 'y'
    elif x=='r' and y=='s':
        return 'x'
    elif x=='p' and y=='r':
        return 'x'
    elif x=='p' and y=='p':
        return 0
    elif x=='p' and y=='s':
        return 'y'
    elif x=='s' and y=='r':
        return 'y'
    elif x=='s' and y=='p':
        return 'x'
    elif x=='s' and y=='s':
        return 0



def rockPaperScissor():
    playerScore = 0
    botScore = 0
    userWish='y'
    userWish = input("Enter y for continue n for exit")
    while userWish != 'n':
        x = player()
        y = bot()
        won=winner(x,y)
        if(won=='x'):
            playerScore=playerScore+1
        elif(won=='y'):
            botScore=botScore+1
        elif(won==0):\
            print("its a draw")
        print("bot Score: ",botScore)
        print("player Score: ",playerScore)



rockPaperScissor()
