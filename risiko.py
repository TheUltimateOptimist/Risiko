# dies ist der Ausganspunkt des CLI Programms Risiko

# importe:
from spielStand import spielStand
import spielfeld


# List mit allen Spielern in richtiger Reihenfolge
spielerListe = [] 

def validierterInput(hilfeText):
    # lässt den Benutzer etwas eingeben und prüft diese Eingabe
    # wenn die Eingabe nicht das anzeigen des Spielstands erfordert, wird sie zurückgegeben
    text = input(hilfeText)
    if text == "Spielstand":
        spielStand()
        validierterInput(hilfeText)
    else:
        return text


def spielVorbereiten():
    spielerZahl = int(input("Gib die Spielerzahl(2-6) ein: "))
    spielerDaten = []

    for i in range(spielerZahl):
        spielerName = input(f"Name von Spieler {i}: ")
        
        spielerListe.append()
    # fügt alle Spieler zur Spielerliste hinzu
    # verteilt die Gebiete
    # verteilt die Truppen
    # legt die Spielerreihenfolge fest  
     
    pass 


def spielen():
    # solange die Funktion gewinnerGefunden False zurück gibt:
         # lässt Spieler Truppen platzieren
         # lässt Spieler angreifen
         # lässt Spieler Truppen bewegen
    # ansonsten ehrt es den Gewinner was das Spiel beendet
    pass  


def main():
    # die erste Funktion die ausgeführt wird, wenn das Programm startet
    pass

main()          
    
