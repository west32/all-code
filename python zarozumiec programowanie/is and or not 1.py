zakupy= input('podaj liste zakupów oddzielając ją przecinkami')
zakupy = zakupy.split(',')

if 'chleb' in zakupy and 'bulki' in zakupy:
    print('na liscie sa chleb i bulki')
elif 'chleb' in zakupy:
    print('chleb jest na liscie zakupów')
elif 'bulki' in zakupy:
    print('na liscie są bułki')
else:
    print('na liscie nie ma pieczywa')