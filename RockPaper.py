import random
counter=0
while counter==0:
    a=["paper","scissors","rock"]
    c=random.randint(0,2)
    b=a[c]
    print("Rock Paper Scissors Game")
    print("Rock beats scissors")
    print("Scisssors cuts paper")
    print("Paper covers rock")
    print("Choose 0 for paper , 1 for scissors and 2 for rock")
    n=int(input())
    if n==c:
        print("You choose ",a[n],"computer choose",b)
        print("its a tie")
    elif n==0:
        if c==1:
            print("You choose ",a[n],"computer choose",b)
            print("computer won")
        if c==2:
            print("You choose ",a[n],"computer choose",b)
            print("you won")
    elif n==1:
        if c==0:
            print("You choose ",a[n],"computer choose",b)
            print("you won")
        if c==2:
            print("You choose ",a[n],"computer choose",b)
            print("computer won")
    elif n==2:
        if c==1:
            print("You choose ",a[n],"computer choose",b)
            print("you won")
        if c==0:
            print("You choose ",a[n],"computer choose",b)
            print("computer won")
    else:
        print("choose valid number")
    print("Play again")
    print("Choose 0 for yes , 1 for no")
    z=int(input())
    if z!=0:
        break
                
            
        
        
        
        
