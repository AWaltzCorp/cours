# Correction main .py
``` python
nombre_a_trouver = random.randint(1, 20)
reponse = None

while reponse != nombre_a_trouver:
    reponse = int(input("Devine le nombre (entre 1 et 20) : "))
    
    if reponse < nombre_a_trouver:
        print("Plus grand !")
    elif reponse > nombre_a_trouver:
        print("Plus petit !")
    else:
        print("Bravo, tu as trouvé le nombre !")
````
# Les dictionnaires
lien[https://courspython.com/dictionnaire.html]
## 1.1 initialisation
```python
nom_dictionnaire={}


```
## 1.2 afficher les clefs puis les valeurs
``` python
for clef,valeur in ulysse.items() :
    print('clef:',clef,'valeur:',valeur)
    
 ```
## Pand


# Devoirs 
- 1. Le programme choisit un mot au hasard d’un dictionnaire de mots et d’indices.
- 2. À chaque tour, le joueur reçoit un indice pour deviner un mot.
- 3. S’il trouve le mot, il gagne ! Sinon, il peut retenter jusqu'à épuiser les mots sans indices reçus.
        