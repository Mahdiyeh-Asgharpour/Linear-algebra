#for using random method, we should import this function
import random

#user's name
Name=input('Ur name:')

def Game():
    #user's score
    Score=0
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
            UserNumberR=input('The correct answer:')
            if UserNumberR !="hop" and UserNumberR !="Hop":
                UserNumberR=int(UserNumberR)
                if UserNumberR==UserNumberT:
                    print('Correct!')
                    Score=Score+1
                    if (UserNumberT+1)%5==0:
                        print("Hop")
                    else:
                        print(UserNumberT+1)  
            
                else:
                
                    print('Wrong')
                    if UserNumberT%5 !=0:
                        print('The correct answer:'+str(UserNumberT))
                    else:
                        print('Hop')
                    print('Do you want to play again?')
                    #Answer is yes or no
                    Answer=input('y or n?')
                    if Answer=="y":
                        Score=0
                        Game()
                    else:
                        print('Ur score:'+str(Score))
                        return

                    
        
                    
            else:
                
                print('Wrong')
                if UserNumberT%5 !=0:
                    print('The correct answer:'+str(UserNumberT))
                else:
                    print('Hop')
                print('Do you want to play again?')
                    #Answer is yes or no
                Answer=input('y or n?')
                if Answer=="y":
                    Score=0
                    Game()
                else:
                    print('Ur score:'+str(Score))
                    return
        else:
            UserNumberR=input('The correct answer:')
            if UserNumberR=="hop" or UserNumberR=="Hop":
                print('Correct!') 
                Score=Score+1
                print(UserNumberT+1) 
            else:
                
                print('Wrong')
                if UserNumberT%5 !=0:
                    print('The correct answer:'+str(UserNumberT))
                else:
                    print('Hop')
                print('Do you want to play again?')
                    #Answer is yes or no
                Answer=input('y or n?')
                if Answer=="y":
                    Score=0
                    Game()
                else:
                    print('Ur score:'+str(Score))
                    return
        UserNumberT=UserNumberT+2
#call function
Game()