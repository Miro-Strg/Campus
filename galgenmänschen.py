def Galgenmännchen():
    geheimes_wort = "baumhaus"
    versuche = 6
    geratene_buchstaben = []

    while versuche > 0:
        print('wort:',"".join(buchstabe if buchstabe in geratene_buchstaben
                              else'_'for buchstabe in geheimes_wort))
        print('versuche übrig:', versuche)

        eingabe = input ('gib einen Buchstaben ein: ').lower()

        if len(eingabe) == 0 or not eingabe.isalpha():
            print('Bitte minedstend einen buchstaben eingeben')
            continue
        elif eingabe in geratene_buchstaben:
            print('Den Buchtaben haben wir schon!')
            continue

        geratene_buchstaben .append(eingabe)

        if eingabe in geheimes_wort:
            print('Der Buchstabe '+ eingabe + ' ist drin!')

        else:
            versuche -= 1
            print('Falscher Buchstabe. Versuche es erneut')

        if all(buchstabe in geratene_buchstaben for buchstabe in geheimes_wort):
                print('Herzlichen Glückwunsch! Sie haben das Wort' +geheimes_wort+'erraten!')
                break

    print('Keine versuche mehr übrig! Das wort war' + geheimes_wort +'Spiel vorbei.')

    nochmal_spielen = input('Möchtest du nochmal spielen? (Ja/nein): ')
    if nochmal_spielen.lower() == 'ja':
        Galgenmännchen()
    else:
        print('Vielen Dank für das Spielen von Galgenmännchen!')

Galgenmännchen()