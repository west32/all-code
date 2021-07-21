# liczba = int(input('podaj parzystą liczbe  liczbe'))
# liczba_prob = 10
# proba = 0
# while proba < liczba_prob or liczba %2==0:
#     if not liczba  %2==0:
#         print(f'no chyba {liczba} to jednak nie jest parzysta liczba, sprobuj jeszcze raz \n')
#         liczba = int(input('podaj parzystą liczbe  liczbe'))
#
# if proba > liczba:
#     print ('przekroczyles liczbe dostepnych 10 prob')
# if liczba %2==0:
#     print('brawo')
#
# lub

liczba = int(input('wporwadz parzystą liczbe '))
proba = 1
while proba < 10 and liczba %2!=0:
    print(f"jestes pewien, że {liczba} to parzysta liczba? sprobuj ponownie... \n")
    proba += 1
    liczba = int(input('wporwadz parzystą liczbe '))
if proba >= 10:
    print('przykro im wykorzystałes 10 prób')
else:
    print('brawo')