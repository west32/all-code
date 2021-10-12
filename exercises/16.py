# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back
# to the user the same string, except with the words in backwards order. For example, say I type the string:


sentence= input("Enter multiple words sentence: ")



def reverse_order_sentenes(sentence):
    sentence_list= sentence.split(" ")
    sentence_list.reverse()
    reverse_sentence= " ".join(sentence_list)
    return(reverse_sentence)

# reverse_sentence= reverse_order_sentenes(sentence)



def reverseWord(sentence):
    return ' '.join(sentence.split()[::-1])

print(reverseWord(sentence))
