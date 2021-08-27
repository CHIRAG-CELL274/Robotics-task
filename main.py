import random
overs =int(input("Enter the number of overs "))
compscore = random.randint (0,36)
print("Computer has score=",end="")
print(compscore)
print("Your target=",end="")
print(compscore+1)

m=0
x=0

def sum(m):
    m=score
    return m

for i in range(1,overs+1):
    for j in range(1,7):
        score=int(input("Enter number to bat="))
        print("Computer's no=",end="")
        compno=random.randint(0,6)
        print(compno)
        if compno == score:
            print("out")
            break
        else:
            x=x+sum(m)

        if x>compscore:
            break

if x>compscore:
    print ("You own the match by",x-compscore-1)
elif x==compscore:
    print("Match draw")
else:
    print ("Computer won the match by",compscore-x-1)

