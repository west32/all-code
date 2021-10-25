


game= [["_","_","_"] for x in range(3)]


def draw_board(player=None,coordinates=None):
    mark=""


    if player == 1:
        mark = "x"
    elif player== 2:
        mark= "o"

    game[coordinates[0]][coordinates[1]]=mark


    rows= {
        1:f"|{game[0][0]}|{game[0][1]}|{game[0][2]}|",
        2:f"|{game[1][0]}|{game[1][1]}|{game[1][2]}|",
        3:f"|{game[2][0]}|{game[2][1]}|{game[2][2]}|"}


    celling=" _"

    row1=(rows[1])
    row2=(rows[2])
    row3=(rows[3])

    print(f'''
    {celling*3}
    {row1}
    {row2}
    {row3}''')
    return rows
# draw_board(player=2,coordinates=(2,2))

def get_players_names():
    player_one_name = input("Set name for player 1 ('x' mark):  ")
    player_two_name= input("Set name for player 2 ('o' mark):  ")
    return player_one_name,player_two_name


def player_one_move(player1):
    player1_coordinates=input(f"{player1} enter coordinates: ")
    player1_row = int(player1_coordinates[0])-1
    player1_column = int(player1_coordinates[2])-1

    if game[player1_row][player1_column] == "_":
        draw_board(player=1,coordinates=(player1_row,player1_column))
    else:
        print("sorry this place it's already taken")


def player_two_move(player2):
    player2_coordinates = input(f"{player2} enter coordinates: ")
    player2_row = int(player2_coordinates[0]) - 1
    player2_column = int(player2_coordinates[2]) - 1

    if game[player2_row][player2_column] == "_":
        draw_board(player=2, coordinates=(player2_row, player2_column))
    else:
        print("sorry this place it's already taken")

def check_for_p1():
    player1_won = False
    for index, list in enumerate(game):
        if game[index][0] == "x" and game[index][1] == "x" and game[index][2] == "x":
            player1_won = True
        elif game[0][index] == "x" and game[1][index] == "x" and game[2][index] == "x":
            player1_won = True
        elif game[0][0] == "x" and game[1][1] == "x" and game[2][2] == "x":
            player1_won = True
        elif game[0][2] == "x" and game[1][1] == "x" and game[2][0] == "x":
            player1_won = True
    if player1_won == True:
        print("Player1 WON!")



def check_for_p2():
    player2_won = False
    for index, list in enumerate(game):
        if game[index][0] == "o" and game[index][1] == "o" and game[index][2] == "o":
            player2_won = True
        elif game[0][index] == "o" and game[1][index] == "o" and game[2][index] == "o":
            player2_won = True
        elif game[0][0] == "o" and game[1][1] == "o" and game[2][2] == "o":
            player2_won = True
        elif game[0][2] == "o" and game[1][1] == "o" and game[2][0] == "o":
            player2_won = True
    if player2_won == True:
        print("Player2 WON!")



def run_game():
    print("""
Welcome in TIC TAC TOE GAME!""")
    player1,player2=get_players_names()
    counter = 0
    while counter !=9:

        player_one_move(player1)
        check_for_p1()
        counter +=1
        if counter <9:
            player_two_move(player2)
            check_for_p2()
            counter +=1
        else:
            print("GAME OVER")






if __name__=="__main__":
    run_game()


