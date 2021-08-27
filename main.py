import random
overs =int(input("Enter the number of overs ")) # overs input
compscore = random.randint (0,36) # computer score
print("Computer has score=",end="")
print(compscore)
print("Your target=",end="")
print(compscore+1)

m=0
x=0

def sum(m): # function for calculating the score of player
    m=score
    return m

for i in range(1,overs+1): # loop for number of overs
    for j in range(1,7):   # loop for number of balls
        score=int(input("Enter number to bat="))  # player input
        print("Computer's no=",end="")
        compno=random.randint(0,6)  # computer number
        print(compno)
        if compno == score:
            print("out")
            break
        else:
            x=x+sum(m)  # calculating the score of the player

        if x>compscore:
            break

if x>compscore:
    print ("You own the match by",x-compscore-1)
elif x==compscore:
    print("Match draw")
else:
    print ("Computer won the match by",compscore-x-1)

