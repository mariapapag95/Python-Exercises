import os
import random

def scrub(words):
    scrubbedwords = []
    for word in words:
        scrubbed = word.strip("'s")
        if "'" in scrubbed:
            scrubbed = scrubbed.replace("'","")
        scrubbedwords.append(scrubbed.lower())
    return scrubbedwords

words = open("wordlist.txt").read().split()
words = scrub(words)

def just_length_n(words,x,y):
    def test(word):
        if len(word) in range(x,y):
            return True
        return False
    return list(filter(test, words))

easy_words = (just_length_n(words, 3,6))
intermediate_words = (just_length_n(words, 5,8))
hard_words = (just_length_n(words, 8,20))


rules = "\n****HANGMAN****\nHOW TO PLAY: \nChoose your difficulty level.\nEnter a guess for a letter between A-Z.\nKeep guessing until you've found the word.\nBut guess carefully..\nIf you run out of guesses, you will be hanged!\nTo quit at any time, enter 'quit'.\n"
print (rules)
quit_ = ["quit", "QUIT", "Quit"]
difficulty = input("--DIFFICULTY-- \nEasy \nIntermediate \nExpert\n\n")

while True:
    if difficulty in quit_:
        computerplay=""
        print ("\nQuitters never win ;P \nBYE LOSER!\n") 
        break       
    elif difficulty.lower() == "easy":
        computerplay = random.choice(easy_words)
        break
    elif difficulty.lower() == "intermediate":
        computerplay = random.choice(intermediate_words)
        break
    elif difficulty.lower() == "expert":
        computerplay = random.choice(hard_words)
        break
    else:
        difficulty = input("That's not an option. Try again.\n")
        continue

error0 = "   ____\n  |    |\n  |    \n  |   \n  |    \n  |   \n _|_\n|   |______\n|          |\n|__________|\n"
error1 = "   ____\n  |    |\n  |    o\n  |   \n  |    \n  |   \n _|_\n|   |______\n|          |\n|__________|\n"
error2 = "   ____\n  |    |\n  |    o\n  |    |\n  |    \n  |   \n _|_\n|   |______\n|          |\n|__________|\n"
error3 = "   ____\n  |    |\n  |    o\n  |   /|\n  |    \n  |   \n _|_\n|   |______\n|          |\n|__________|\n"
error4 = "   ____\n  |    |\n  |    o\n  |   /|\ \n  |    \n  |   \n _|_\n|   |______\n|          |\n|__________|\n"
error5 = "   ____\n  |    |\n  |    o\n  |   /|\ \n  |    |\n  |       \n _|_\n|   |______\n|          |\n|__________|\n"
error6 = "   ____\n  |    |\n  |    o\n  |   /|\ \n  |    |\n  |   /    \n _|_\n|   |______\n|          |\n|__________|\n"
error7 = "   ____\n  |    |\n  |    o\n  |   /|\ \n  |    |\n  |   / \    \n _|_\n|   |______\n|          |\n|__________|\n"
errors = [error0, error1, error2, error3, error4, error5, error6]

right_responses = ["\nWINNER, WINNER, CHICKEN DINNER!","\nDING DING DING!","\nLucky guess!", "\nRIGHT-O", "\nYou got it!", "\nYou can win this!", "\nBingo", "\nYou are one smart cat", "\nNo one's getting hung today", "\nYou're so close!"]
wrong_responses = ["\nHAHAHAAh!", "\nYou'll never win", "\nWhat a dumb answer!", "\nYou should just quit", "\nLOL you're really bad at this game", "\nWRONG!", "\nSO WRONG!", "\nn00b"]

wrong_guess = []
right_guess = []

prompt = "_ " * len(computerplay)
newprompt = ""

if difficulty in quit_:
    pass
else: 
    print ("\n"+errors[len(wrong_guess)])
    print (prompt)


def new_prompt():
    newprompt = ""
    for i in computerplay:
        if i == play or i in right_guess:
            i = i+" "
            newprompt += i
        else:
            newprompt += "_ "
    if "_" not in newprompt:
        exithack = [1,2,3,4,5,6,7]
        for i in exithack:
            wrong_guess.append(exithack)
        return "{}\n\nYOU WON!\nCONGRATULATIONS".format(newprompt.upper())
    else:
        return newprompt

def right(play):
    right_guess.append(play)
    print ("\n"+errors[len(wrong_guess)])
    return new_prompt() 

def wrong(play):
    wrong_guess.append(play)
    try:
        print ("\n"+errors[len(wrong_guess)])
        return new_prompt()
    except IndexError:
        print(error7)
        return "You failed to guess the word '{}'.\nYou have been hung!\nx_x GAME OVER x_x".format(computerplay)


def validate(input_): 
    if input_.isalpha() == False:
        return "\nThat was not a letter. Try again."
    if input_ != "quit" and len(input_) > 1 or len(input_) < 1:
        return "\nYou must choose ONE letter. Try again."
    if input_ in right_guess or input_ in wrong_guess:
        return "\nYou already guessed that letter..."
    if input_ not in computerplay:
        os.system('clear')
        print (random.choice(wrong_responses))
        return wrong(input_)
    else:
        os.system('clear')
        print (random.choice(right_responses))
        return right(input_)


while len(wrong_guess) < 7:
    if difficulty in quit_:       
        break
    play=input("\n")   
    play=play.lower()
    if play in quit_:
        print ("\nQuitters never win ;P \nBYE LOSER!\n")        
        break
    else:
        print(validate(play))
    newprompt=newprompt
