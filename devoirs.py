import random
words=["hello","world","Python"]
wordchosen=''
hint=''
number=random.randint(0,2)
if number==0 :
    wordchosen=words[0]
    hint='a word to say hi'
if number==1 :
    wordchosen=words[1]
    hint='the planet'
if number==2 :
    wordchosen=words[2]
    hint='a powerful programming language'
def main() :
    utilisateur=input("devinez le mot")
    if utilisateur==number :
     print ('bravo')
    if utilisateur !=wordchosen: 
     print (hint)
     main()
main()
   
    
    
    