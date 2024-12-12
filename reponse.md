# Correction main.py
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

## 1.3 afficher uniquement une valeur 
``` python
employees={
    "Max":{
        "age":51,
        "job":"CEO"
    },
    "Francis":{
        "age":18,
        "job":"Secretary"
    }
    
}
employees["Max"]["age"]=23
#print(employees["Max"])
#for clefs,valeurs in employees.items():
#   print(valeurs["age"])
print(employees["Max"]["age"])

employees={
    "Max":{
        "age":51,
        "job":"CEO"
    },
    "Francis":{
        "age":18,
        "job":"Secretary"
    }
    
}
# J'affiche
print(employees["Max"]["age"])
```


## modifier
``` python
employees={
    "Max":{
        "age":51,
        "job":"CEO"
    },
    "Francis":{
        "age":18,
        "job":"Secretary"
    }
    
}
employees["Max"]["age"]=23
```

# Les listes
## Transformer une liste en chaîne de caractères.
```python
mot=["is","s"]
"".join(mot)
```
# Coventions
```python
nom_de_la_fonction
maVariable
MACONSTANTE

```

# fonction 
## On peut indiquer le type d'un argument et le result d'une foction
``` 



