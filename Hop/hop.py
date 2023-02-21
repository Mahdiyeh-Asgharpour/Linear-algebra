#for using random method, we should import this function
import random
# the first number
First=random.randint(0, 10)
while First%5==0:
    First=random.randint(0, 10)
print('The first number:'+str(First))
#User number that is True
UserNumberT=First+1
while True:
    if UserNumberT%5 !=0:
#User number that is received
        UserNumberR=int(input('The correct answer:'))
        if UserNumberR==UserNumberT:
            print('Correct!')
            if (UserNumberT+1)%5==0:
                print("Hop")
            else:
                print(UserNumberT+1)  
        else:
            
            print('Wrong')
            print('The correct answer:'+str(UserNumberT))
            break
    else:
        UserNumberR=input('The correct answer:')
        if UserNumberR=="hop" or UserNumberR=="Hop":
            print('Correct!')            
            print(UserNumberT+1) 
        else:
            
            print('Wrong')
            print('The correct answer:hop')
            break 
    UserNumberT=UserNumberT+2

    