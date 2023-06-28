# Génération du fichier input.txt

Pour générer le fichier à partir des entrées du fichier excel, on a besoin de excel et notepad++ ou autre éditeur de texte avancé

dans la cellule C15 on doit mettre la formule

~~~excel
=SI(C7<>"";CONCAT("##newentry##;";$B7:$B14;";";TEXTE(C$6;"aaaa-mm-jj");";";C7;";";;C8;";";;C9;";";;C10;";";;C11;";";;C12;";";;C13;";";C14);"")
~~~

et recopier la cellule C15 sur toute la ligne 15 de C à ~AA (jusqu'au dernier jour)

ensuite on peut copier la ligne 15 sur les lignes qui suivent un bloc (24,33,42,51)

on peut copier les lignes résultantes dans notepad++

quand c'est fait on devrait avoir de très longues lignes dans le fichier

on doit faire CTRL+H pour remplacer

s'assurer d'avoir le mode étendu ( qui permet l'utilisation de \n )

et remplacer tout

Recherche:

~~~text
##newentry##
~~~

par :

~~~text
\n##newentry##
~~~
