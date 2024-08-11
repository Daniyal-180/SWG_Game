import random
def S_W_G():
    print(f"__Welcome The Snake Water Gun Game__")
    
    user = int(input("Choice\n0 for Snake:\n1 for Water:\n2 for Gun\n"))
    computer = random.randint(0,2)

    print(f"Your choice is {user} and computer is {computer}")
        
    if user == computer:
        print(f"\tGame Tied")
    
    elif user == 0 and computer == 1:
        print(f"\tThe user Win the game")
            
    elif user == 1 and computer == 2 :
        print(f"\tThe user Win the game")
            
    elif user == 2 and computer == 0 :
        print(f"\tThe user Win the game")
            
    else:
        print("\tComputer Win the game")

S_W_G()