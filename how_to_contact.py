# Es wird allen Namen eine zufällige Kontaktmöglichkeit hinzugefügt
import random

# kontaktmöglichkeiten
kontakt = ['Telefon', 'Brief', 'Mail', 'Whatsapp', 'Signal']
# Dictionary mit Namen und Kontaktmöglichkeiten
kontaktliste = {}

# Schleife, die alle Namen durchgeht und zufällig einen Kontaktmöglichkeit aus der Liste hinzugefügt
with open('namensliste.txt', 'r', encoding='utf-8') as gaesteliste:
    for name in gaesteliste:
        name = name.strip()
        kontaktliste[name] = random.choice(kontakt)

print(kontaktliste)
