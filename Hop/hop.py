#for using random method, we should import this function
import random
#list
My_List=[]
#user's name
Name=input('Ur name:')
My_List.append(Name+str(0))
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
                    My_List.remove(Name+str(Score-1))
                    My_List.append(Name+str(Score))
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
                        My_List.remove(Name+str(Score))

                        Score=0
                        My_List.append(Name+str(Score))
                        Game()
                    else:

                        print('Ur score:'+My_List.pop())
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
                    My_List.remove(Name+str(Score))

                    Score=0
                    My_List.append(Name+str(Score))
                    Game()
                else:
                    print('Ur score:'+My_List.pop())
                    return
        else:
            UserNumberR=input('The correct answer:')
            if UserNumberR=="hop" or UserNumberR=="Hop":
                print('Correct!') 
                Score=Score+1
                My_List.remove(Name+str(Score-1))

                My_List.append(Name+str(Score))
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
                    My_List.append(Name+str(Score))
                    Game()
                else:
                    print('Ur score:'+My_List.pop())
                    return
        UserNumberT=UserNumberT+2
#call function
Game()
