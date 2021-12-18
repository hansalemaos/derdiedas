from random import shuffle
with open(r'derdiedas.txt', encoding='utf-8') as file:
    daten = file.readlines()
daten = [[wort2.split('/') for wort2 in wort.strip(",\n'").split('\t')] for wort in daten]
shuffle(daten)
for artikel, wort in daten:
    print(wort[0])
    benutzereingabe = input('Bitte Artikel eingeben: ')
    benutzereingabe = benutzereingabe.lower().strip()
    if benutzereingabe in artikel:  
        print('Das ist richtig!')
    elif benutzereingabe not in artikel:
        print('Das ist falsch!')
    print(5*'\n')
