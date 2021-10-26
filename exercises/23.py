def max_num(a,b,c):
    user_variables= (a,b,c)
    higher_num=0
    for num in user_variables:
        if int(num) > higher_num:
            higher_num=int(num)
    print(higher_num)

max_num(13,646,7889)
