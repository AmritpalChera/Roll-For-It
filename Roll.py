# if you can read this, comment your name
# mansheel #Lightning :) #Talha #Arnav
# player 1 and 2 dice- 6 each
# 30 cards (use card array)- 10,5,15...divide equally
# 3 dice on 5 point cards, 4 dice on 10 point cards, 6 dice on 15 point cards 
# create array for dice on cards 
# list of functons: 1. who goes first 2. rolling dice 3. cards 4. dice on cards 5. MATCHING 6.points
import random
 
p1Points=0 #keeps track of PLayer1 points 
p2Points=0 #keeps track of Player2 points
p1Dice=[0,0,0,0,0,0] # numbers on dice intialized to 0                                                  
p2Dice=[0,0,0,0,0,0]
p1name= raw_input("Enter name:\n") #name of player 1
p2name= raw_input("Enter name:\n") #name of player2
player1 = "t"#used in deciding who goes first part of program 
player2 = "n" 
roll_dice1="roll" #sentry variable for nested while loop for Player1
roll_dice2="op" #sentry variable for nested while loop for Player2
num1=0 #used in deciding who goes first part of program 
num2=0


 
############################
#Graphics
 
from turtle import*
 
import turtle
 
#fd=turtle forward motion
#lt=turtle angle motion to the left (right if angle is negative)
#rt=turtle angle motion to the right
#setx and sety=turtle coordinates (puts the turtle to a starting position I want)
#seth=direction the turtle is facing (uses degrees; as if it were a compass)
#speed=how fast the animation should be
#color=used to generate different colours to make the game more lively
#begin_fill and end_fill are used to determine what should be filled in, and what colour
#hideturtle is used to not show the point of animation
#ontimer=delays between each output (in milliseconds)
#Write=displays text on the animated screen
#Update=update's the screen to allow no faults while playing
#The numbers beside the variables usually indicate which player it is meant for
#Displays the title of the window:
title("Roll For it")
 
##def main_graphics():
##    print table()
##    print card_1()
##    print card_2()
##    print card_3()
##    print dice_display1()
##    print dice_display2()
##    print dice_display3()
##    print dice_display4()
##    print dice_display5()
##    print dice_display6()
##print main_graphics()
    
 
 
def table():
    #To display the frame of the table
    speed(-1)
    color('black')
    setx(-1000)
    sety(-1000)
    for outline in range (2):
        begin_fill()
        fd(2000)
        lt(90)
        fd(2000)
        lt(90)
        end_fill()
 
 

 
#Function with dice value of 1 
def dice_display1():
    hideturtle()
    speed(-1)
    penup()
    color('white')
    setx(-180)
    sety(10)
    pendown()  
    begin_fill()
    lt(90)
    lt(90)
    fd(50)
    lt(90)
    fd(50)
    lt(90)
    fd(50)
    end_fill()
    def dot_one(): #dice value with 1
        penup()
        speed(-1)
        color('red')
        setx(-205)
        sety(-15)
        pendown()
        begin_fill()
        circle(5)
        end_fill()
    dot_one()
 
 
 
 
 
#Function for Dice with value of 2 
def dice_display2():
    hideturtle()
    speed(-1)
    penup()
    color('white')
    setx(-180)  #######Change the coordinates to a variable for random dice generation
    sety(80)    ######Change the coordinates to a variable for random dice generation
    pendown()  
    begin_fill()
    lt(90)
    lt(90)
    fd(50)
    lt(90)
    fd(50)
    lt(90)
    fd(50)
    end_fill()
    def dot_two():#dice value with 2
        for c in range (2):
            penup()
            color('red')
            setx(-215)  ######Change the coordinates to a variable for random dice generation
            sety(50)    ######Change the coordinates to a variable for random dice generation   
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            penup()
            color('red')
            setx(-195)  ######Change the coordinates to a variable for random dice generation
            sety(50)    ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
    dot_two()
 
 
 
 
 
 
#Function for Dice with value of 3
def dice_display3():
    hideturtle()
    speed(-1)
    penup()
    color('white')
    setx(-180)  #######Change the coordinates to a variable for random dice generation
    sety(140)    ######Change the coordinates to a variable for random dice generation
    pendown()  
    begin_fill()
    lt(90)
    lt(90)
    fd(50)
    lt(90)
    fd(50)
    lt(90)
    fd(50)
    end_fill()
    def dot_three():#dice value with 3
        for c in range (2):
            #Dot number 1
            penup()
            color('red')
            setx(-220)  ######Change the coordinates to a variable for random dice generation
            sety(109)    ######Change the coordinates to a variable for random dice generation   
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 2
            penup()
            color('red')
            setx(-190)  ######Change the coordinates to a variable for random dice generation
            sety(109)   ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 3
            penup()
            color('red')
            setx(-205)  ######Change the coordinates to a variable for random dice generation
            sety(109)   ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
    dot_three()
 
 
 
 
#Function for Dice with value 4
def dice_display4():
    hideturtle()
    speed(-1)
    penup()
    color('white')
    setx(-9)  #######Change the coordinates to a variable for random dice generation
    sety(120)    ######Change the coordinates to a variable for random dice generation
    pendown()  
    begin_fill()
    lt(90)
    lt(90)
    fd(50)
    lt(90)
    fd(50)
    lt(90)
    fd(50)
    end_fill()
    def dot_four():#dice value with 4
        for c in range (2):
            #Dot number 1
            penup()
            color('red')
            setx(-27)  ######Change the coordinates to a variable for random dice generation
            sety(102)    ######Change the coordinates to a variable for random dice generation   
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 2
            penup()
            color('red')
            setx(-43)  ######Change the coordinates to a variable for random dice generation
            sety(102)   ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 3
            penup()
            color('red')
            setx(-27)  ######Change the coordinates to a variable for random dice generation
            sety(85)   ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 4
            penup()
            color('red')
            setx(-43)    ######Change the coordinates to a variable for random dice generation
            sety(85)   ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
    dot_four()
 
 
 
 
#Function for Dice with value 5
def dice_display5():
    hideturtle()
    speed(-1)
    penup()
    color('white')
    setx(45)  #######Change the coordinates to a variable for random dice generation
    sety(100)    ######Change the coordinates to a variable for random dice generation
    pendown()  
    begin_fill()
    lt(90)
    lt(90)
    fd(50)
    lt(90)
    fd(50)
    lt(90)
    fd(50)
    end_fill()
    def dot_five():#dice value with 5
        for c in range (2):
            #Dot number 1
            penup()
            color('red')
            setx(11)  ######Change the coordinates to a variable for random dice generation
            sety(85)    ######Change the coordinates to a variable for random dice generation   
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 2
            penup()
            color('red')
            setx(30)  ######Change the coordinates to a variable for random dice generation
            sety(65)   ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 3
            penup()
            color('red')
            setx(11)  ######Change the coordinates to a variable for random dice generation
            sety(65)   ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 4
            penup()
            color('red')
            setx(30)    ######Change the coordinates to a variable for random dice generation
            sety(85)   ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 5
            penup()
            color('red')
            setx(21)  ######Change the coordinates to a variable for random dice generation
            sety(75)  ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
    dot_five()
 
 
#Function for Dice with value 6
def dice_display6():
    hideturtle()
    speed(-1)
    penup()
    color('white')
    setx(43)  #######Change the coordinates to a variable for random dice generation
    sety(25)    ######Change the coordinates to a variable for random dice generation
    pendown()  
    begin_fill()
    lt(90)
    lt(90)
    fd(50)
    lt(90)
    fd(50)
    lt(90)
    fd(50)
    end_fill()
    def dot_six():#dice value with 6
        for c in range (2):
            #Dot number 1
            penup()
            color('red')
            setx(11)  ######Change the coordinates to a variable for random dice generation
            sety(7)    ######Change the coordinates to a variable for random dice generation   
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 2
            penup()
            color('red')
            setx(30)  ######Change the coordinates to a variable for random dice generation
            sety(7)   ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 3
            penup()
            color('red')
            setx(11)  ######Change the coordinates to a variable for random dice generation
            sety(-5)   ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 4
            penup()
            color('red')
            setx(30)    ######Change the coordinates to a variable for random dice generation
            sety(-5)   ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 5
            penup()
            color('red')
            setx(11)  ######Change the coordinates to a variable for random dice generation
            sety(-17)  ######Change the coordinates to a variable for random dice generation
            pendown()
            begin_fill()
            circle(5)
            end_fill()
            #Dot number 6
            penup()
            color('red')
            setx(30)
            sety(-17)
            pendown()
            begin_fill()
            circle(5)
            end_fill()
    dot_six()
 
from turtle import *
import turtle
import random
 
card5=[]
card10=[]
card15=[]
 
p1card5=[]
p1card10=[]
p1card15=[]
p2card5=[]
p2card10=[]
p2card15=[]
 
#To display the frame of the table
speed(-1)
color('black')
setx(-1000)
sety(-1000)
for outline in range (2):
    begin_fill()
    fd(2000)
    lt(90)
    fd(2000)
    lt(90)
    end_fill()
 
# cards with 5 points
def card_3():
    seth(270)
    speed(-1)
    penup()
    color('blue') #blue cards have 5 points
    setx(-120)
    sety(-50)
    pendown()
    begin_fill()
    lt(90)
    lt(90)
    fd(250)
    lt(90)
    fd(170)
    lt(90)
    fd(250)
    end_fill()
    #Print card number
    speed(-1)
    penup()
    color('green')
    setx(-215)
    sety(130)
    pendown()
    write("5", font=("Arial", 45, "bold"))
    #Position
    penup()
    xcoor=-225
    ycoor=-30
    seth(0)
    color('white')
    pendown()
    speed(-1)
    for x in range (3):
        penup()
        color('white')
        setx(xcoor)
        sety(ycoor)
        seth(0)
        pendown()
        begin_fill()
        for x in range (4):
            fd(50)
            lt(90)
        end_fill()
        seth(0)
        fd(15)
        color('black')
        number=[1,2,3,4,5,6]
        choice=random.choice(number)
        card5.append(choice)
        write(choice, font=("Arial",30, "bold"))
        ycoor=ycoor+55
    
# cards with 10 points 
def card_2():
    seth(270)
    hideturtle()
    speed(-1)
    penup()
    color('red') #red cards have 10 points
    setx(90)
    sety(-50)
    pendown()
    begin_fill()
    lt(90)
    lt(90)
    fd(250)
    lt(90)
    fd(170)
    lt(90)
    fd(250)
    end_fill()
    #Print card number
    hideturtle()
    speed(-1)
    penup()
    color('white')
    setx(-25)
    sety(130)
    pendown()
    write("10", font=("Arial", 45, "bold"))
    #Position
    penup()
    xcoor=10
    ycoor=-10
    seth(0)
    color('white')
    pendown()
    speed(-1)
    for x in range (2):
        for x in range (2):
            penup()
            color('white')
            setx(xcoor)
            sety(ycoor)
            seth(0)
            pendown()
            begin_fill()
            for x in range (4):
                fd(50)
                lt(90)
            end_fill()
            seth(0)
            fd(15)
            color('black')
            number=[1,2,3,4,5,6]
            choice=random.choice(number)
            card10.append(choice)
            write(choice, font=("Arial",30, "bold"))
            ycoor=ycoor+55
        xcoor=-50
        ycoor=-10
 
# cards with 15 points 
def card_1():
    hideturtle()
    speed(-1)
    penup()
    color('orange') #orange cards have 15 points
    setx(125)
    sety(-50)
    pendown()
    begin_fill()
    fd(170)
    lt(90)
    fd(250)
    lt(90)
    fd(170)
    lt(90)
    fd(250)
    end_fill()
    #Print card number
    hideturtle()
    speed(-1)
    penup()
    color('purple')
    setx(175)
    sety(130)
    pendown()
    write("15", font=("Arial", 45, "bold"))
    #Position
    penup()
    xcoor=230
    ycoor=-30
    seth(0)
    color('white')
    pendown()
    speed(-1)
    for x in range (2):
        for x in range (3):
            penup()
            color('white')
            setx(xcoor)
            sety(ycoor)
            seth(0)
            pendown()
            begin_fill()
            for x in range (4):
                fd(50)
                lt(90)
            end_fill()
            seth(0)
            fd(15)
            color('black')
            number=[1,2,3,4,5,6]
            choice=random.choice(number)
            card15.append(choice)
            write(choice, font=("Arial",30, "bold"))
            ycoor=ycoor+55
        xcoor=150
        ycoor=-30
 
 
 
 
 
 
 
 
 
##########################################################
#Game
    
print "Welcome to Roll For It!"
print "\nLets start with some INSTRUCTIONS"
print "\nIn this game, you have 6 dice, which you will match with cards"
print  "Once all numbers on a card are matched with your dice, the card is yours, along with the amount of points it indicates"
print "The first player to score 40 points WINS"
print "For MORE information, watch this short YouTube video by Calliope Games: https://www.youtube.com/watch?v=boHd0C9-4kI"
print "\nBefore we begin, put this screen and soon to open animated screen into splitscreen view"
print "\nHere are some handy EXIT procedures"
print "When asked to place more dice, enter 'no' to complete your turn, else keep playing :)"
print "To quit choosing a card or a specific number, enter any invalid input of the right type"
print "\n\nAnd finally HAVE FUN playing with your partner!"


#To ensure they type "ok" to continue
confirm=""
while confirm!="ok":
    confirm=raw_input("\nType \"ok\" When Done: ")
    if confirm!="ok":
        print "Sorry! Invalid input"
print "Super!"
print table() #this prints the another separate window with a black background
print "Decide who goes first!"
while num1==num2: # to prevent ties
    roll_dice1="roll" #sentry variable for nested while loop for Player1
    roll_dice2="op" #sentry variable for nested while loop for Player2
    while roll_dice1!="":#Have player roll dice to make game more interactive
        print p1name,
        roll_dice1=raw_input("press ENTER to roll dice")
        num1 = random.randrange(1,7)
#this part will randomly display the dice that player 1 rolls
        if num1==1:
            dice_display1()
        elif num1==2:
            dice_display2()
        elif num1==3:
            dice_display3()
        elif num1==4:
            dice_display4()
        elif num1==5:
            dice_display5()
        elif num1==6:
            dice_display6()
        print "You Rolled:\t",num1
        table()
    while roll_dice2!="":
        print p2name,
        roll_dice2=raw_input("press ENTER to roll dice")
        num2 = random.randrange(1,7)
#this part will randomly display the dice that player 2 rolls
        if num2==1:
            print dice_display1()
        elif num2==2:
            print dice_display2()
        elif num2==3:
            print dice_display3()
        elif num2==4:
            print dice_display4()
        elif num2==5:
            print dice_display5()
        elif num2==6:
            print dice_display6()
        print "You Rolled:\t",num2
        table()
    if num1 < num2: #Decide who is Player1 and who is Player2.
        print p2name,"Goes first  -  You rolled:\t",num2
#print write(p2name, align=('left'), font=("Arial", 20, "bold"))
        print p1name,"Goes second -  You rolled:\t",num1
#print write(p1name, align=('left'), font=("Arial", 20, "bold"))
        player2 = p1name
        player1 = p2name
    elif num1> num2:
        print p1name,"Goes First  -  You rolled:\t",num1
        print p2name,"Goes Second  -  You rolled:\t",num2
        player1 = p1name
        player2 = p2name
    else:
        print "\nBoth Players Roll Again"
 
################################
 
card_1()
card_2()
card_3()

def player1Sum():
    
    print "\nDice Summary For Player 1:\n",player1," on card5 ", p1card5
    print player1," dice on card10 ", p1card10
    print player1," dice on card5 ", p1card15, "\n"

def player2Sum():
    
    print "\nDice Summary For Player 2:\n",player2," on card5 ", p2card5
    print player2," dice on card10 ", p2card10
    print player2," dice on card5 ", p2card15, "\n"
 
def rolling1(): # player1 rolls dice
    player1Sum()
    print player1,
    ask=raw_input("press ENTER to roll dice") #executes 6 dice rolls on any press of any key on the keyboard
    diceAmount = len(p1Dice)
    for x in range (0, diceAmount):
        p1Dice[x]=random.randrange(1,7);
    return p1Dice
 
#p1d= rolling1()
#print "p1 dice tag"
def rolling2(): #player2 rolls dice
    player2Sum()
    print player2,
    ask2=raw_input("press ENTER to roll dice") #executes 6 dice rolls on any press of any key on the keyboard
    diceAmount = len(p2Dice)
    for x in range (0, diceAmount):
        p2Dice[x]=random.randrange(1,7);
    return p2Dice
 
p1profile=[0,0,0]
 
def p1DiceCheck():
    tag=1 
    #while(tag==1):
    position1=raw_input("Which card? (card1 or card2 card3)") #Position 1 refers to the 3 cards displayed
    #Card 1
    if position1=="card1":
        position2=input("What number?") #Position 2 refers to the *location* of the numbers/dices displayed on the cards
        if position2 in p1Dice:
            #print "match"
            p1card5.append(position2)
            p1Dice.remove(position2)
        else:
            print "Your dice does not match card"
        tag=2
    #CARD 2      
    elif position1=="card2":
        position2=input("What number? ")
        if position2 in p1Dice:
            #print "match"
            p1card10.append(position2)
            p1Dice.remove(position2)
        else:
            print "Your dice does not match card"
        tag=2
            
    #CARD 3
    elif position1=="card3":
        position2=input("What number? ") #Position 2 refers to the *location* of the numbers/dices displayed on the cards
        if position2 in p1Dice:
            #print "match"
            p1card15.append(position2)
            p1Dice.remove(position2)
        else:
            print "Your dice does not match card"
            tag=2
    else:
        tag=1
        print "Invalid input"
    #print "Left Dice: ", p1Dice
            
def p2DiceCheck():
    tag=1 
    #while(tag==1):
    position1=raw_input("Which card? (card1 or card2 or card3) ") #Position 1 refers to the 3 cards displayed
    #Card 1
    if position1=="card1":
        position2=input("What number?") #Position 2 refers to the *location* of the numbers/dices displayed on the cards
        if position2 in p2Dice:
           # print "match"
            p2card5.append(position2)
            p2Dice.remove(position2)
        else:
            print "Your dice does not match card"
        tag=2
    #CARD 2      
    elif position1=="card2":
        position2=input("What number?")
        if position2 in p2Dice:
            #print "match"
            p2card10.append(position2)
            p2Dice.remove(position2)
        else:
            print "Your dice does not match card"
        tag=2
    #CARD 3
    elif position1=="card3":
        position2=input("What number? ") #Position 2 refers to the *location* of the numbers/dices displayed on the cards
        if position2 in p2Dice:
           # print "match"
            p2card15.append(position2)
            p2Dice.remove(position2)
        else:
            print "Your dice does not match card"
            tag=2
    else:
        tag=1
        print "Invalid input"
        


def sort(list1):
    for x in range (1, len(list1)):
        value = list1[x]
        indexCompare = x-1
        while (value < list1[indexCompare] and indexCompare>=0):
               list1[indexCompare+1] = list1[indexCompare]
               indexCompare = indexCompare-1;
        list1[indexCompare+1] = value
    return list1;

def areSame (list1,list2):
               #list1 = sort(list1)
               #list2 = sort(list2)
               temp1 = []
               temp2 = []
               for a in range (len(list1)):
                   temp1.append(0)
                   temp1[a] = list1[a];
               #temp1 = list1
               for a in range (len(list2)):
                   temp2.append(0)
                   temp2[a] = list2[a];
               #temp2 = list2
               x = False
               for a in range (len(temp2)):
                   x=False
                   for b in range (len(temp1)):
                       if temp2[a]==temp1[b]:
                           x=True
                           temp1[b]=-1
                       if x==True:
                           break
                    
                                   
                        
                   if x==False:
                       return x

               #print "lists are same"
               return True
               

                
 
################################### MAIN
 
while (p1Points<40 or p2Points<40):#p1Points<=40 or p2Points<=40): # main loop starts here. this loop will end if one of the players reaches 40 points
    
    rolling1() #Calls and executes function for rolling dice of player1
    print player1,"rolled",p1Dice
    continuechoice="yes"
    while (continuechoice!="no"):
        p1DiceCheck()
        print ""
        player1Sum()
        #print player1, " on card5 ", p1card5;
       # print "card5", card5;
               
            
        if len(p1card15) >= 6:
            if areSame(p1card15, card15):
                p1Points=p1Points+15
                card15 = []
                card_1()
                for x in range (6-len(p1card15),6):
                    p1Dice.append(0)
                    p1Dice[x]=random.randrange(1,7)
                for x in range (6-len(p2card15),6):
                    p2Dice.append(0)
                    p2Dice[x]=random.randrange(1,7)
                p1card15=[]
                p2card15 = []

        elif len(p1card10)>=4:
            if areSame(p1card10, card10):
                p1Points=p1Points+10
                card10 = []
                card_2()
                for x in range (6-len(p1card10),6):
                    p1Dice.append(0)
                    p1Dice[x]=random.randrange(1,7)
                for x in range (6-len(p2card10),6):
                    p2Dice.append(0)
                    p2Dice[x]=random.randrange(1,7)
                p1card10=[]
                p2card10 = []

        elif (len(p1card5)>=3):
            #print "entered 1card 5"
            if areSame(p1card5,card5):
                #print "hllo"
                p1Points=p1Points+5
                card5 = [];
                card_3()
                for x in range (6-len(p1card5),6):
                    p1Dice.append(0)
                    p1Dice[x]=random.randrange(1,7)
                for x in range (6-len(p2card5),6):
                    p2Dice.append(0)
                    #p2Dice[x]=random.randrange(1,7)
                p1card5=[]
                p2card5 = []
                

        print "Left Dice: ", p1Dice
            
        continuechoice=raw_input("Place more dice? ") #Calls and executes function for rolling dice of player1
        print "\n"

    print  player1," has ", p1Points,"points"
    print player2," has ", p2Points,"points\n\n"
    rolling2() #Calls and executes function for rolling dice of player2
    print player2,"rolled",p2Dice
    continuechoice = "yes"
    while (continuechoice!="no"):
        p2DiceCheck()
        print ""
        player2Sum()
        #print player2," on card5 ", p2card5;
        #print "card5", card5;
        
        
        
        if len(p2card15)  >=6:
            if areSame(p2card15,card15):
                p2Points=p2Points+15
                card15 = []
                card_1()
                for x in range (6-len(p2card15),6):
                    p2Dice.append(0)
                    p2Dice[x]=random.randrange(1,7)
                for x in range (6-len(p1card15),6):
                    p1Dice.append(0)
                    p1Dice[x]=random.randrange(1,7)
                p2card15=[]
                p1card15 = []

        elif len(p2card10) >=4:
            if areSame(p2card10, card10):
                p2Points=p2Points+10
                card10 = []
                card_2()
                for x in range (6-len(p2card10),6):
                    p2Dice.append(0)
                    p2Dice[x]=random.randrange(1,7)
                for x in range (6-len(p1card10),6):
                    p1Dice.append(0)
                    p1Dice[x]=random.randrange(1,7)
                p2card10=[]
                p1card10 = []

        elif len(p2card5) >=3:
            #print "entered card 5"
            if areSame (p2card5, card5):
                #print "yes same"
                p2Points=p2Points+5
                card5 = []
                card_3()
                for x in range (6-len(p2card5),6):
                    p2Dice.append(0)
                    p2Dice[x]=random.randrange(1,7)
                for x in range (6-len(p1card5),6):
                    p1Dice.append(0)
                    #p1Dice[x]=random.randrange(1,7)
                p2card5=[]
                p1card5 = []
                
        print "Left Dice: ", p2Dice
        
        continuechoice=raw_input("Place more dice? ")
        print "\n"
        
    print  player1," has ", p1Points,"points"
    print player2," has ", p2Points,"points\n"
    print "__________________________________________\n"
        
#After one or both players reach 40 points
if (p1Points == 40 and p2Points == 40): #if the game is a tie
    print "Game Over"
    print "Congratulations Both players reached 40 points" 
    print "It is a Tie"
 
elif (p1Points == 40): #if player 1 wins
    print "Game Over"
    print "Congratulations to",player1, "You Won"
    print "Player 1 Points =",p1Points 
    print "Player 2 Points =",p2Points
 
elif (p2Points == 40): #if player 1 wins
    print "Game Over"
    print "Congratulations to",player2, "You Won"
    print "Player 1 Points =",p1Points 
    print "Player 2 Points =",p2Points
    
  
  
  
  
  
  
  
  
  
  
  
 
 
 
