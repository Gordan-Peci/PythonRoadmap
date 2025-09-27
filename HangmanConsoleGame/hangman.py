import random

wordList = ["Developer", "Program", "List", "Function", "Random", "Exception"]

def choose_word():
    return random.choice(wordList).upper()

def play():
    word = choose_word()
    guessed = set()
    attempts = 6
    
    while attempts > 0:
        for char in word:
            print(char if char in guessed else "_", end=" ")
        
        letter = input("Enter letter: ").upper()
        
        if letter in guessed:
            continue
            
        guessed.add(letter)
        
        if letter not in word:
            attempts -= 1
            print("Wrong!")
        else:
            print("Correct!")
        
        # Check if won
        if all(char in guessed for char in word):
            print(f"You won! Word: {word}")
            return
    
    print(f"Lost! Word was: {word}")

play()