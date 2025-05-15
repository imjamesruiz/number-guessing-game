import random

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have certain number of chances chances to guess the correct number\n")

def easy():
    print("Great! You have selected the Easy difficulty level.")
    print("Let's start the game!\n")
    
    number = random.randint(1, 100)
    correct = False
    attempts, chances = 0, 10
    
    while not correct:
        guess = int(input("Enter your guess: "))
        attempts += 1
        chances -= 1
        
        if chances == 0:
            print("You have run out of attempts!")
            print(f"The correct number was {number}")
            break
            
        elif guess == number:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            correct = True
        
        else:
            if guess > number:
                print(f"Incorrect! The number is less than {guess}\n")
                # print(f"Attempts {attempts}")
                # print(f"chances == {chances}\n")
                
            elif guess < number:
                print(f"Incorrect! The number is greater than {guess}\n")
                # print(f"Attempts {attempts}")
                # print(f"chances == {chances}\n")
                
                
def medium():
    print("Great! You have selected the Medium difficulty level.")
    print("Let's start the game!\n")
    
    number = random.randint(1, 100)
    correct = False
    attempts, chances = 0, 5
    
    while not correct:
        guess = int(input("Enter your guess: "))
        attempts += 1
        chances -= 1
        
        if chances == 0:
            print("You have run out of attempts!")
            print(f"attempts: {attempts}")
            print(f"The correct number was {number}")
            break
            
        elif guess == number:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            correct = True
        
        else:
            if guess > number:
                print(f"Incorrect! The number is less than {guess}\n")

                
            elif guess < number:
                print(f"Incorrect! The number is greater than {guess}\n")

                
def hard():
    print("Great! You have selected the Hard difficulty level.")
    print("Let's start the game!\n")
    
    number = random.randint(1, 100)
    correct = False
    attempts, chances = 0, 3
    
    while not correct:
        guess = int(input("Enter your guess: "))
        attempts += 1
        chances -= 1
        
        if chances == 0:
            print("You have run out of attempts!")
            print(f"The correct number was {number}")
            break
            
        elif guess == number:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            correct = True
        
        else:
            if guess > number:
                print(f"Incorrect! The number is less than {guess}\n")
                
            elif guess < number:
                print(f"Incorrect! The number is greater than {guess}\n")


def main():
    print("Please select the difficulty level: ")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)\n")
    
    while True:
        choice = int(input("Enter your choice: "))
        print()

        if choice == 1:
            easy()
            break
            
        elif choice == 2:
            medium()
            break
            
        elif choice == 3:
            hard()
            break
        
        else:
            print("Invalid input: please type (1) (2) or (3) for selection\n")
                
            
        

            
if __name__ == "__main__": 
    main()
    
    while True:
        print()
        quit = input("Do you want to keep playing: (y) or (n): ")
    
        if quit == "y":
            print()
            main()
        
        elif quit == "n":
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid response please type (y) or (n)")
            
            
        
        
        