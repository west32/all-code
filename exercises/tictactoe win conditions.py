game = [[2,0,1],
        [1,2,0],
        [1,1,2]
        ]



def check_for_p1():
        player1_won = False
        for index, list in enumerate(game):
                if game[index][0] == 1 and game[index][1]== 1 and game[index][2]==1:
                        player1_won = True
                elif game[0][index] ==1 and game[1][index]==1 and game[2][index]==1:
                        player1_won= True
                elif game[0][0]==1 and game[1][1]==1 and game[2][2]==1:
                        player1_won=True
                elif game[0][2]==1 and game[1][1]==1 and game[2][0]==1:
                        player1_won= True
        if player1_won == True:
                print("Player1 WON!")
        else:
                print("player1 hasn't won")

def check_for_p2():
        player2_won = False
        for index, list in enumerate(game):
                if game[index][0] == 2 and game[index][1]== 2 and game[index][2]==2:
                        player2_won = True
                elif game[0][index] ==2 and game[1][index]==2 and game[2][index]==2:
                        player2_won= True
                elif game[0][0]==2 and game[1][1]==2 and game[2][2]==2:
                        player2_won=True
                elif game[0][2]==2 and game[1][1]==2 and game[2][0]==2:
                        player2_won= True
        if player2_won == True:
                print("Player2 WON!")
        else:
                print("player2 hasn't won")

check_for_p1()
check_for_p2()
