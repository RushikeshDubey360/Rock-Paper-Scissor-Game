
# ROCK PAPER SCISSOR GAME :-

import random                    #''' rock vs paper    -> paper win
a=['Rock','Paper','Scissor']     #    rock vs scissor  -> rock win
                                 #    paper vs scissor -> scissor win '''
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game Start......
1 Yes
2 No | Exit
    '''))                                 
    if uc==1:
        for b in range (1,6):
            userInput=int(input('''
1 Rock
2 Paper
3 Scissor            
            '''))
            if userInput==1:
                uchoice='Rock'
            elif userInput==2:
                uchoice='Paper'
            elif userInput==3:
                uchoice='Scissor'
            Cchoice=random.choice(a)
            if Cchoice==uchoice:
               print('Computer Value :-',Cchoice)
               print('Your Value :-',uchoice)
               print('Game Draw.....')
               ucount=ucount+1
               ccount=ccount+1
            elif (uchoice=='Rock'and Cchoice=='Scissor') or (uchoice=='Paper'and Cchoice=='Rock') or (uchoice=='Scissor'and Cchoice=='Paper'):
               print('Computer Value :-',Cchoice)
               print('Your Value :-',uchoice)
               print('You Win.....')
               ucount=ucount+1
            else:
                  print('Computer Value :-',Cchoice)
                  print('Your Value :-',uchoice)
                  print('Computer Win.....')
                  ccount=ccount+1
        if ucount==ccount:
            
            print('Opps! Game Draw.....')
            print('Your Score :-',ucount)
            print('Computer Score :-',ccount)
        elif ucount>ccount:
            
            print('Yes! You Win The Game.....')
            print('Your Score :-',ucount)
            print('Computer Score :-',ccount)
        else:
            
            print('Cumputer win the  Game.....')
            print('Your Score :-',ucount)
            print('Computer Score :-',ccount)

    else:
        break
        