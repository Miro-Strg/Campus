Geheimezahl = 47
Versuche = 3
#Test 123
while Versuche > 0:
    print('Errate die Zahl zwischen 1 und 100\nDu hast', str(Versuche) + ' Versuche')
    eingabe = input('Deine Eingabe: ')

    try:
        geratene_zahl = int(eingabe)
        
        if geratene_zahl < 1 or geratene_zahl > 100:
            print('Die Zahl liegt zwischen 1 und 100!')
            continue

        if geratene_zahl > Geheimezahl:
            print('Zu hoch, versuch es nochmal!')
        elif geratene_zahl < Geheimezahl:
            print('Zu niedrig, versuch es nochmal!')
        else:
            print('Richtig! Du hast die Zahl erraten!')
            break  # Beende die Schleife, wenn die Zahl richtig erraten wurde
            
    except ValueError:
        print('Bitte nur Zahlen :D')
    
    Versuche -= 1  # Reduziere die Anzahl der Versuche nach jedem Versuch

if Versuche == 0:
    print('Du hast die Zahl nach 3 Versuchen nicht erraten. Die gesuchte Zahl war:', Geheimezahl)