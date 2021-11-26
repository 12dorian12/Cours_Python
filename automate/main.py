#Header
"""
permet d'utiliser l'automate de syntaxe
Dorian ISSELIN
26/11/21
fini
"""

import automate as a

phrases = ["le joli chat joue.",
"le ,joli chat ; joue.",
"la grosse souris verte mange le joli petite chat blanc.",
"la grosse souris verte mange jean.",
"Jean joue.",
"Jean mange Martin.",
"Jean mange le chat.",
"la verte souris grosse petit mange le blanc verte chat petit."]

for i in phrases:
    a.verif_phrase(i)


thePhrase = input('entre une phrase : ')
a.verif_phrase(thePhrase)