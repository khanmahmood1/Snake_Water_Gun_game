import random
def gameWin(comp, you):
    #if computer and your choice is same
    if comp == you:
        return None
    
    #if computer choose snake
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
        
    #if computer choose gun
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False
        
    #if computer choose water  
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
   



print("computer turn: snake(s), water(w) or gun(g)?")
randomNo = random.randint(1, 3)
# print(randomNo)

if randomNo == 1:
    comp = 's'
elif randomNo == 2:
    comp = 'w'
elif randomNo == 3:
    comp = 'g'

you = input("Player's turn: snake(s), water(w) or gun(g)? ")

a = gameWin(comp, you)

print(f"computer choose {comp}")
print(f"You  {you}")

if a == None:
    print("The game is tie!")
elif a:
    print("You win")
else:
    print("You lose")