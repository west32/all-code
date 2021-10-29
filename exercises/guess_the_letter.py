def guessing_logic(secret_word):
    secret_word= secret_word
    print("Welcome in Hangman Game!")
    listone=[]
    guessed_list=[]
    hidden_word= ""

    for _ in range(len(secret_word)):
        listone.append("_")
    for element in listone:
        hidden_word +=f" {element}"

    print(hidden_word)
    while True:
        listtwo = []
        guess=input("Guess the letter: ").upper()
        guessed_list.append(guess)
        if guess in guessed_list:
            print("You have already tried this one!")
        if guess in secret_word:
            for letter in secret_word:
                if guess== letter:
                    listtwo.append(letter)
                else:
                    listtwo.append("_")
            for index, element in enumerate(listone):

                if element != listtwo[index] and element == "_":
                    listone[index] = listtwo[index]
        else:
            print("Incorrect!")


        hidden_word=""
        for element in listone:
            hidden_word += f" {element}"
        print(hidden_word)
        if "_" not in listone:
            print(f"Congtatulations")
            break