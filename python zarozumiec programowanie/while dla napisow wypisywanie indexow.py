# nick = input('wpisz swój nickname: ')
# nick_index = 0
# while nick_index < len(nick):
#     print(f"[{nick_index}] -> {nick[nick_index]}")
#     nick_index += 1

Nickname = input ("jaki jest Twoj nickname")
for index, letter in enumerate(Nickname):
    print(f"[{index}] -> {letter}")

