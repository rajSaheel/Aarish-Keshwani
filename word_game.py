import random
words=["spike","ball","surroundings","mobile","pencil","psychology","cologne"]
for word in words:
    unique=[]
    while(len(unique)!=len(word)):
        index=random.randint(0,len(word)-1)
        if index not in unique:
            unique.append(index)
    jumble=""
    for i in unique:
        jumble+=word[i]
    response=input("Guess the word: "+jumble+"\n")
    if response==word:
        print("Congrats, you guessed the word correctly!")
    else:
        print("You guessed wrong.")
