import random

def wordpicker():

    with open ("words.txt","r") as word:
        words = word.readlines()
    w = words[random.randint(0,len(words))]
    x = w.split("\n")
    return x[0]

def hangman(tries):
    print()
    arr = [[" "," ","O"],["\n","--"],["|"],["--","\n"],["  ","|"],["\n"," ","/"],[" ","\\"]]
    for i in range(tries):
        for j in range(len(arr[i])):
            print(arr[i][j],end="")

def printer(l):


    for i in range(len(l)):
        print(l[i],end=" ")
    print()

word = wordpicker()
tries = 0
chance = 7
l = ["_" for i in range(len(word))]
printer(l)

while True:

    if word.upper() == "".join(l):
        print("Yaaa! you saved me!")
        break

    guess = input("\nEnter Guess: ")

    if guess in word:    
        index = [i for i, l in enumerate(word) if l == guess]
        for i in index:
            l[i] = guess.upper()
        printer(l)
        
    if (tries == chance):
        print("I trusted you...")
        print("the word was,",word)
        break

    if guess not in word:
        tries+=1
        hangman(tries)
        print()
        print()
        printer(l)
