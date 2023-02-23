#for using random method, we should import this function
import random
#list
My_List=[]

#function is hop's code
def Game():
    #user's name
    Name=input('Ur name:')
    My_List.append([Name,str(0)])
    #user's score
    Score=0
    # the first number
    First=random.randint(0, 10)
    #when the first number is hop,this is wrong so it should changed
    while First%5==0:
        First=random.randint(0, 10)
    print('The first number:'+str(First))
    #User number that is True
    UserNumberT=First+1
    while True:
    #if UserNumberT is not hop, input is int
        if UserNumberT%5 !=0:
    #User number that is received
            UserNumberR=input('The correct answer:')
            #it is possible that user writes hop
            if UserNumberR !="hop" and UserNumberR !="Hop":
                UserNumberR=int(UserNumberR)
                if UserNumberR==UserNumberT:
                    print('Correct!')
                    Score=Score+1
                    My_List.remove([Name,str(Score-1)])
                    My_List.append([Name,str(Score)])
                    if (UserNumberT+1)%5==0:
                        print("Hop")
                    else:
                        print(UserNumberT+1)  
            
                else:
                
                    print('Wrong')
                    #UserNumberT is number that is not hop
                    if UserNumberT%5 !=0:
                        print('The correct answer:'+str(UserNumberT))
                    else:
                        #UserNumberT is hop
                        print('Hop')
                    print('Do you want to play again?')
                    #Answer is yes or no
                    Answer=input('y or n?')
                    if Answer=="y":
                        Game()
                    else:
                        for Element in My_List:
                            if Element[0]==Name:
                                if int(Element[1])<Score:
                                    My_List.remove(Element)
                                    My_List.append([Name,str(Score)])
                        print(str(My_List))
                        break

                    
        
                   
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
                    Game()
                else:
                    for Element in My_List:
                        if Element[0]==Name:
                            if int(Element[1])<Score:
                                My_List.remove(Element)
                                My_List.append([Name,str(Score)])
                                print(str(My_List))
                    break
        #UserNumberT is hop
        else:
            UserNumberR=input('The correct answer:')
            if UserNumberR=="hop" or UserNumberR=="Hop":
                print('Correct!') 
                Score=Score+1
                My_List.remove([Name,str(Score-1)])

                My_List.append([Name,str(Score)])
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
                    Game()
                else:
                    for Element in My_List:
                        if Element[0]==Name:
                            if int(Element[1])<Score:
                                My_List.remove(Element)
                                My_List.append([Name,str(Score)])
                    print(str(My_List))
                    break
        UserNumberT=UserNumberT+2
#call function
Game()
