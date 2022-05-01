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
chance = 8
g = []
l = ["_" for i in range(len(word))]
printer(l)
print(word)
while tries != chance:

    if word.upper() == "".join(l):
        print("Yaaa! you saved me!")
        break

    guess = input("\nEnter Guess: ",)
    g.append(guess)
    if len(g) > 0:
        print("(",end="")
        for i in g:
            print(i,end=" ") 
        print(")",end="")
    print()

    if guess in word:    
        index = [i for i, l in enumerate(word) if l == guess]
        for i in index:
            l[i] = guess.upper()
        printer(l)
        print(tries)

    if guess not in word:
        tries+=1
        hangman(tries)
        print()
        print()
        printer(l)
        print(tries)
else:
    print("/ni trusted you...")
    print("The word was,",word)
