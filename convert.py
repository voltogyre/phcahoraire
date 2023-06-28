# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility


#
# voir readme.md pour la génération du fichier à partir de excel
#

import re

import glob
import os

for fichier in glob.glob('output-*.csv'):
    os.remove(fichier)

regex = r"##newentry##;(.*);(\d\d\d\d-\d\d-\d\d);(.*)"

with open('input.txt', 'r', encoding='utf-8') as file:
    test_str = file.read()

matches = re.finditer(regex, test_str, re.MULTILINE)

g = open("output-global.csv", mode='w', encoding='utf-8')
d = open("debug.txt", mode='w', encoding='utf-8')


for matchNum, match in enumerate(matches, start=1):
    # print("##begin##")
    fichier_sortie = "output-" + \
        re.sub(r" ", "", match.group(1), 0, re.IGNORECASE) + ".csv"
    ladate = match.group(2)
    # print(fichier_sortie)
    # print(ladate)
    # print(match.group(3))
    regex2 = r"\D(\d+)h(\d+)"
    ladescription = match.group(3)
    lesheures = re.finditer(regex2, ladescription, re.IGNORECASE)
    lesheures2 = []

    for heureNum, heure in enumerate(lesheures, start=1):
        lesheures2.append(int(heure.group(1))*60+int(heure.group(2)))

    # print(lesheures2)
    duree = int(max(lesheures2)) - int(min(lesheures2))
    start = min(lesheures2)
    startheure = start // 60
    startminute = start % 60
    startlib = '' + '{:02d}'.format(startheure) + \
        ":" + '{:02d}'.format(startminute)
    # print(startlib)
    # print(duree)
    description = re.sub(r";+", " - ", ladescription, 0)
    description = re.sub(r" +", " ", description, 0)
    description = re.sub(r"-( -)+", "-", description, 0)
    # on doit identifier le type
    if "DEK" in description:
        letype = "DEK"
    elif re.match("partie.*pr.*saison", description,  re.IGNORECASE):
        letype = "Partie pré-saison"
    elif "Partie" in description:
        letype = "Partie"
    elif "BSR" in description:
        letype = "Entraînement"
    elif "hors-glace" in description:
        letype = "Hors-glace"
    elif "Hors-glace" in description:
        letype = "Hors-glace"
    elif "HG" in description:
        letype = "Hors-glace"
    elif "Glace" in description:
        letype = "Entraînement"
    else:
        letype = "Autre"
        d.write("type -> ")
        d.write(description+"\n")

    # on doit identifier la catégorie et le groupe/équipe
    if "M13D1" in fichier_sortie:
        categ = "M13 D1"
        local = "Corsaires M13 D1"
    elif "M15D1" in fichier_sortie:
        categ = "M15 D1"
        local = "Corsaires M15 D1"
    elif "M18D1" in fichier_sortie:
        categ = "M18 D1"
        local = "Corsaires M18 D1"
    elif "M15D2" in fichier_sortie:
        categ = "M15 D2"
        local = "Corsaires M15 D2"
    elif "M18D2" in fichier_sortie:
        categ = "M18 D2"
        local = "Corsaires M18 D2"
    elif "PHCASec.1" in fichier_sortie:
        categ = "Secondaire 1"
        local = "Sec. 1"
    elif "PHCASec.2-3" in fichier_sortie:
        categ = "Secondaire 2-3"
        local = "Sec. 2-3"
    elif "PHCASec.4-5" in fichier_sortie:
        categ = "Secondaire 4-5"
        local = "Sec. 4-5"
    elif "Primaire" in fichier_sortie:
        categ = "Primaire"
        local = "Primaire"
    else:
        categ = match.group(1)
        local = match.group(1)

    # on doit identifier le lieu
    if "BSR" in description:
        lieu = "Aréna de Bernières Saint-Rédempteur"
    elif "PATRO" in description:
        lieu = "Patro"
    elif "Glace St-Henri" in description:
        lieu = "Aréna Saint-Henri"
    elif "Glace - St-Henri" in description:
        lieu = "Aréna Saint-Henri"
    elif "Glace - LAUZON" in description:
        lieu = "Aréna André Lacroix"
    elif "Glace - Lévis" in description:
        lieu = "Aréna municipal de Lévis"
    elif "CÉGEP DE LÉVIS" in description:
        lieu = "CÉGEP de Lévis"
    else:
        lieu = "indéterminé"
        d.write("lieu -> ")
        d.write(description+"\n")

    # print("##end##\n\n")

    f = open(fichier_sortie, mode='a', encoding='utf-8')
    chaine = "\"{id}\";\"{saison}\";\"{cat}\";\"{type}\";\"{datestart}\";\"{heurestart}\";\"{duree}\";\"{desc}\";\"{lieu}\";\"{visiteur}\";\"{local}\";\"{datepub}\";\"{tempeval}\";\"{alerte}\";\"{prive}\"\n".format(
        id="", saison="2023-24", cat=categ, type=letype, datestart=ladate, heurestart=startlib, duree=duree, desc=description, lieu=lieu, visiteur="", local=local, datepub="", tempeval="", alerte="", prive="")
    f.write(chaine)
    g.write(chaine)
    f.close

g.close
d.close
