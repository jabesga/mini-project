from random import randint
import random

print("======== ECHO | TR GENERATOR ========")
word = input("Insert a phrase or your email:\n\t")

if ' ' in word:
    print("Whitespaces are not accepted")
else:
    set1, set2 = [], []
    transformed = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuvwxyz0123456789@."
    
    for pos in range(0, len(word)):
        if word[pos] not in set2:
            alpha_rpos = randint(0,len(alphabet))
            while alphabet[alpha_rpos-1] in set1:
                alpha_rpos = randint(0,len(alphabet))

            set1.append(alphabet[alpha_rpos-1])
            set2.append(word[pos])
            transformed += alphabet[alpha_rpos-1]
        else:
            transformed += set1[set2.index(word[pos])]

    tuple_set = list(zip(set1, set2))
    random.shuffle(tuple_set)
    set1, set2 = zip(*tuple_set)

    print("Output:")
    print("\techo " + transformed + " | tr " + ''.join(set1) + " " + ''.join(set2))
    print("========================")