import os
import random


#the list to store all the words
word_list = []

with open("words.txt") as words_txt:
    words = (words_txt).read()
    #read each word in the file and store them in the 'word_list' array
    for word in words.split():
        word_list.append(word)

#--CONST--
THE_WORD = random.choice(word_list)     #pick a random word from the list
LIFE = 5                                #choose the number of lives you want to have

#--VARIABLES--
displayed_state = []
for i in range(len(THE_WORD)):
    displayed_state.append('_')

gg = False                               #variable to see if the game is done or not

#--FUNCTIONS--
def GetGuess():
    global guess
    guess = input("Enter a character that you think is in the word: ")
    if len(guess) !=1 or not guess.isalpha():
        print("\nInvalid input!")
        GetGuess()
    guess = guess.lower()

def DisplayState():
    print("You have {} lives left!\n".format(LIFE))
    print(" ".join(displayed_state),'\n')

def UpdateState(correct_guess):
    indexes = [a for a,b in enumerate(THE_WORD) if b == correct_guess]
    for i in indexes:
        displayed_state[i] = correct_guess

if __name__ == '__main__':
    DisplayState()
    
    while LIFE > 0 and (not gg):
        GetGuess()
        if guess in THE_WORD:
            UpdateState(guess)
        else:    
            print("Rip, that is not in the word...\n")
            LIFE -= 1
        DisplayState()
        
        if not ('_' in displayed_state):
            gg = True

    if LIFE == 0:
        print("Darn!! So close. Try again!")
    else:
        print("Congratulations! You won!")
              
    print("\nThe word was {}".format(THE_WORD))
