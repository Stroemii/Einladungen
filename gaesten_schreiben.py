import os
import shutil
import sys

from how_to_contact import kontaktliste

FOLDER = os.path.join(r'C:\Users\Stroemi\Desktop\Python-Einstieg\Erstes Projekt - Einladungen\Einladungen', 'Einladungen')


# Wenn es einen Ordner gibt, soll er gelöscht werden (Einladungen sollen neu angelegt werden)
if os.path.isdir(FOLDER):
    shutil.rmtree(FOLDER)

# Ordner, der Einladungen enthalten soll, neu anlegen:
os.mkdir(FOLDER)

# Einladungstext wird in Variable geschrieben
with open('Einladungstext.txt', 'r', encoding='utf-8') as einladungstext:
    einladungstext = einladungstext.read()


for name, contact in kontaktliste.items():
    personalisierte_einladung = einladungstext.format(name=name)     # die Namen des Dict. werden durchlaufen und nacheinander in den Text eingesetzt
    dateiname = f'Einladung an {name}_{contact}.txt'                  # der Dateiname wird zusammengesetzt aus Name und Kontaktmöglichkeit
    with open(os.path.join(FOLDER, dateiname), 'w', encoding='utf-8') as datei:             # die Textfile wird erstellt
        datei.write(personalisierte_einladung)
    
    if not os.path.isdir(os.path.join(FOLDER, contact)):                # Je Kontaktmöglichkeit wird genau ein Ordner erstellt
        os.mkdir(os.path.join(FOLDER, contact))


FILELIST = os.listdir(FOLDER)   # Liste aller Dateien im FOLDER

for file in FILELIST:           # jede Datei, die entsprechend endet wird in den passenden Ordner verschoben
    if file.endswith('Brief.txt'):
        shutil.move(os.path.join(FOLDER, file), os.path.join(FOLDER, 'Brief'))
    elif file.endswith('Mail.txt'):
        shutil.move(os.path.join(FOLDER, file), os.path.join(FOLDER, 'Mail'))
    elif file.endswith('Signal.txt'):
        shutil.move(os.path.join(FOLDER, file), os.path.join(FOLDER, 'Signal'))
    elif file.endswith('Telefon.txt'):
        shutil.move(os.path.join(FOLDER, file), os.path.join(FOLDER, 'Telefon'))
    elif file.endswith('Whatsapp.txt'):
        shutil.move(os.path.join(FOLDER, file), os.path.join(FOLDER, 'Whatsapp'))
