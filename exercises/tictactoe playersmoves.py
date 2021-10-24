game= [[0,0,0],
       [0,0,0],
       [0,0,0]]

player1= input("Set name of first player, your mark will be 'x' ")
player2= input("Set name of second player, your mark wull be 'o' ")


counter = 0
while counter != 9:

    plr1=input(f"{player1} set coordinates of your mark in order 'row,column' ")

    p1row=int(plr1.split(",")[0])-1
    p1column= int(plr1.split(",")[1])-1
    if game[p1row][p1column]==0:
        game[p1row][p1column]= "x"
        print(f"{game[0]}\n{game[1]}\n{game[2]}")
        counter += 1

    else:
        print("this place has been already taken")
        plr1 = input(f"{player1} set coordinates of your mark in order 'row,column' ")
        p1row = int(plr1.split(",")[0]) - 1
        p1column = int(plr1.split(",")[1]) - 1
        if game[p1row][p1column] == 0:
            game[p1row][p1column] = "x"
            print(f"{game[0]}\n{game[1]}\n{game[2]}")
            counter +=1
        else:
            print("this place has been already taken")
    if counter < 9:
        plr2=input(f"{player2} set coordinates for your mark in order 'row,column' ")
        p2row = int(plr2.split(",")[0]) - 1
        p2column = int(plr2.split(",")[1]) - 1
        if game[p2row][p2column]==0:
            game[p2row][p2column] = "o".strip()

            counter +=1
        else:
            print("this place has been already taken")
            plr2 = input(f"{player2} set coordinates for your mark in order 'row,column' ")
            p2row = int(plr2.split(",")[0]) - 1
            p2column = int(plr2.split(",")[1]) - 1
            if game[p2row][p2column] == 0:
                game[p2row][p2column] = "o".strip()
                print("this place has been already taken")
                counter +=1
            else:
                print("this place has been already taken")
        print(f"{game[0]}\n{game[1]}\n{game[2]}")

print("FINISH")

