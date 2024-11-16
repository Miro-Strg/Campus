import random

Tipp = {'wzfgzgegf7': 'bewfbuzfwbz', 'MacBook': 'laptop', 'MacOS': 'Apple Betriebssystem', 'Linux': 'Grundlage vieler Betriebssysteme', 'Holzdecke': 'Holz oben'}
Wörterbuch = list(Tipp.keys())

def Galgenmännchen(geheimes_wort):
    versuche = 6
    geratene_buchstaben = []
    Tipp_anzeige = True

    print('Fals du Hilfe benötigt schreib Tipp')

    while versuche > 0:

        print('Wort:',"".join(buchstabe if buchstabe.lower() in geratene_buchstaben
                              else'_'for buchstabe in geheimes_wort))
        print('versuche übrig:', versuche)

        eingabe = input ('gib einen Buchstaben ein: ').lower()

        if eingabe == 'tipp': 
            print(chr(27) + "[2J")
            print (Tipp[geheimes_wort])
            continue

        if len(eingabe) == 0 or not eingabe.isalpha():
            print(chr(27) + "[2J")
            print('Bitte minedstend einen buchstaben eingeben')
            continue

        elif eingabe in geratene_buchstaben:
            print(chr(27) + "[2J")
            print('Den Buchtaben haben wir schon!')
            continue

        geratene_buchstaben .append(eingabe)
        print(chr(27) + "[2J")

        if eingabe in geheimes_wort.lower():
            print('Der Buchstabe '+ eingabe + ' ist drin!')

        else:
            versuche -= 1
            print('Falscher Buchstabe. Versuche es erneut')

        if all(buchstabe in geratene_buchstaben for buchstabe in geheimes_wort.lower()):
                print('Herzlichen Glückwunsch! Sie haben das Wort' +geheimes_wort+'erraten!')
                break
        
    print('Keine versuche mehr übrig! Das wort war ' + geheimes_wort +' Spiel vorbei.')

    nochmal_spielen = input('Möchtest du nochmal spielen? (Ja/nein): ')
    if nochmal_spielen.lower() == 'ja':
         
        Wort= random.choice (Wörterbuch)
        Galgenmännchen(Wort)
    
    else:
      print('Vielen Dank für das Spielen von Galgenmännchen!')

Wort= random.choice (Wörterbuch)
print(chr(27) + "[2J")
Galgenmännchen(Wort)