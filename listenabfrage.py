# Funktion: Zeigt an, ob ein Produkt vorhanden ist
def produkt_abfrage(produkt_input):

    if produkt_input in produkte:
        print("Das Produkt ist vorhanden")

    else:
        print("""Das Produkt ist nicht vorhanden
        
        Aktuell haben wir folgende Produkte im Angebot:""
        
        """)
        produkt_liste(produkte, menge)

# Funktion: Gibt eine Liste mit Produkten und Mengen aus
def produkt_liste(produkte, menge):
    for produkt, menge in zip(produkte, menge):
        print(f'Es gibt noch {menge} {produkt} im Kühlschrank')



# Listen mit Produkten und Mengen
produkte = ["Apfel", "Birne", "Kirsche", "Banane"]
menge = [5, 3, 4, 10]

# Abfrage des Produktes
abfrage = input("Welches Produkt möchtest du kaufen? ")

# Aufruf der Funktion
produkt_abfrage(abfrage)