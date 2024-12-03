import random
words={
    "hello":"a word to say hi",
    "world":"the planet",
    "python":"a powerful programming language"}
wordFound=False
choice=random.choice(list(words.keys()))
print(choice)
while wordFound==False:
    userChoise=input('essayez de devinez')
    if userChoise==choice :
        wordFound=True
        print('bravo')
        break
    if userChoise !=choice:
        print(words[choice])
