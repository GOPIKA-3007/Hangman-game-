import random
name = input("What is your name? ")
print("Good Luck !! ", name)

choices = ['computer', 'science', 'programming','python', 'mathematics', 'player']
word = random.choice(choices)

print("Guess the characters")
guesses=''
chances=10
valid_entry = set('abcdefghijklmnopqrstuvwxyz')
while chances>0:
    
    failed=0

    for char in word:

        if char in guesses:
            print(char)

        else:

            print("_")
            failed += 1

    if failed==0:
        print("You Win")
        print("The word is:",word)
        break
    
    guess=input("guess a character:")
    guesses += guess
    if guess not in word:
        chances -= 1
        print("Wrong")
        

        if chances==9:
            print("9 chances left!!!")
            print("--------------")
        if chances==8:
            print("8 chances left!!!")
            print("--------------")
            print("      O       ")
        if chances==7:
            print("7 chances left!!!")
            print("--------------")
            print("      O       ")
            print("      |       ")
        if chances==6:
            print("6 chances left!!!")
            print("--------------")
            print("      O       ")
            print("      |       ")
            print("     /        ")    
        if chances==5:
            print("5 chances left!!!")
            print("--------------")
            print("      O       ")
            print("      |       ")
            print("     / \       ") 
        if chances==4:
            print("4 chances left!!!")
            print("--------------")
            print("     \O       ")
            print("      |       ")
            print("     / \       ")
        if chances==3:
            print("3 chances left!!!")
            print("--------------")
            print("     \O/       ")
            print("      |       ")
            print("     / \       ")   
        if chances==2:
            print("2 chances left!!!")
            print("--------------")
            print("     \O/ |      ")
            print("      |       ")
            print("     / \       ")
        if chances==1:
            print("Only 1 chance left!!!")
            print("--------------")
            print("     \O/_|      ")
            print("      |       ")
            print("     / \       ")                      
                        

    if chances==0:
        print("You loose")
        print("--------------")
        print("      O_|      ")
        print("     /|\       ")
        print("     / \       ")
        break 
