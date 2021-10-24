# def max_num(a,b,c):
#     user_variables= (a,b,c)
#     higher_num=0
#     for num in user_variables:
#         if int(num) > higher_num:
#             higher_num=int(num)
#     print(higher_num)
#
# max_num(13,646,7889)
game=[["_","_","_"] for x in range(3)]
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
#
# rows= {
#         1:f"|{game[0][0]}|{game[0][1]}|{game[0][2]}|",
#         2:f"|{game[1][0]}|{game[1][1]}|{game[1][2]}|",
#         3:f"|{game[2][0]}|{game[2][1]}|{game[2][2]}|"}
#
# coordinates=(1,3)
# print(game[coordinates[0]-1][coordinates[0]-1])
#
# print(game)
# print(rows)
player1="bart"
# player1_coordinates=(input(f"{player1} enter coordinates: "))
# player1_row= int(player1_coordinates[0])-1
# player1_column = int(player1_coordinates[2])-1
# if game[player1_row][player1_column]=="_":
#     draw_board(player=1,coordinates=(player1_row,player1_column))
def player_one_move(player1):
    player1_coordinates=input(f"{player1} enter coordinates: ")
    player1_row = int(player1_coordinates[0])-1
    player1_column = int(player1_coordinates[2])-1

    if game[player1_row][player1_column] == "_":
        draw_board(player=1,coordinates=(player1_row,player1_column))
    else:
        print("sorry this place it's already taken")
player_one_move(player1)
