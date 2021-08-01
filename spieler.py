# dies python Datei enthält die Klasse Spieler

class Spieler:
    def __init__(self, spielerName, gebieteTruppenListe, truppenStärke, kartenListe):
        # initialiesiere Klasse Spieler
        self.spielerName = spielerName
        self.gebieteTruppenListe = gebieteTruppenListe
        self.truppenStärke = truppenStärke
        self.kartenListe = kartenListe

    def platziereTruppen(self):
        # ermittel ob er karten einlösen kann
        # ermittel anschließend wieviel Truppen er erhält
        # lass ihn die Truppen platzieren
        pass


    def greifeAn(self):
        # solange er die Angriffsphase nicht beendet:
        # führe die Funktion angriffAusführen aus angriff.py aus
        pass

    def bewegeTruppen(self):
        # lass ihn ausgangsgebiet wählen
        # lass ihn zielgebiet wählen
        # lass ihn truppenzahl wählen 
        # führe die verschiebung aus
        pass     