import random
from PyDictionary import PyDictionary

dictionary=PyDictionary()
file=open("words.txt","r")
words=file.readline().lower()
used_words=[]
new_words=[]
new=""

def generate_word_easy(word):
    gen_word=list(word)
    char='a'
    for i in range(0,4):
        for j in range(0,26):
            gen_word[i]=chr(ord(char)+j)
            new_word=''.join(gen_word)
            #print(new_word)
            if(new_word in words and new_word not in used_words):
                used_words.append(new_word)
                return new_word
                break
        gen_word[i]=word[i]
    return "Word Doesn't Exist!"

def generate_word_medium(word):
    gen_word=list(word)
    char='a'
    for i in range(0,4):
        for j in range(0,26):
            gen_word[i]=chr(ord(char)+j)
            new_word=''.join(gen_word)
            #print(new_word)
            if(new_word in words and new_word not in used_words):
                new_words.append(new_word)
        gen_word[i]=word[i]
    index=random.randint(0,len(new_words))
    if len(new_words)!=0:
        used_words.append(new_words[index])
        return new_words[index]
    else:
        return "Word Doesn't Exist!"

def check_word_validity(word):
    if(word in used_words):
        #print("Word is already used!")
        return False
    if(word not in words):
        #print("Word is not a valid word!")
        return False
    if(word == "Exit Game"):
        return False
    return True

def check_new_word_validity(new):
    new=generate_word_easy(new)
    if(word not in new_words):
        print("Invalid Word!")
        return False
    return True


def main(word):
    #word=input("Player : ")
    new=word
    while(word != "Exit Game"):
        del new_words
        new_words=[]
        if(new != "Word Doesn't Exist!" and check_word_validity(word) != False and check_new_word_validity(new) != False):
            used_words.append(word)
            new=generate_word_easy(word)
            #print("Computer : ",new)
            word=input("Player : ")
        else:
            word=input("Player : ")

    #print("Thank You for playing Addictionary!")