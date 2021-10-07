# word= input("gimme a word :D ")
#
# if word[0] == word[-1] and word [1] == word[-2]:
#     print("this is a palindrome")
# else:
#     print("it's not a palindrome")

word= str(input("enter a string"))
rvs_word = word[::-1]
if word == rvs_word:
    print("That word it is a palindrome..")
else:
    print("This word is not a palind..something")


    # def palind():
    #     my_string = input("Please enter a string: ")
    #
    #
    # return my_string[::] == my_string[::-1]

