def create_clef_valeur(dictionnaire,clef,valeur):
    dictionnaire[clef]=valeur
ulysse={}
nombreinformations = int(input('nombre informations'))

while nombreinformations > 0 :
    clefutilisateur = input('nom de la clef')
    valeurutilisateur = input('Entrez la valeur')
    create_clef_valeur(ulysse,clefutilisateur,valeurutilisateur)
    nombreinformations -=1
for clef,valeur in ulysse.items() :
    print('clef:',clef,'valeur:',valeur)
    
    
