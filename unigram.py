import numpy as np
import random
import parser

print ("Creating unigram probability table")
train_words_pow=0
d1,power=0.75,0.75
table_size=int(1e8)
table=[] # this table stores indices to pick words from vocab
for a in parser.vocab_cn:
    train_words_pow+=a**power
i=0
d1=(parser.vocab_cn[i]**power)/train_words_pow
for a in range(table_size):
    table.append(i)
    if float(a/table_size) > d1:
        i+=1
        d1+=(parser.vocab_cn[i]**power)/train_words_pow
    if i>=parser.vocabSize:
        i=parser.vocabSize-1

def pick(K,contexts):
    Wneg=[]
    # cw=[]
    # for c in contexts:
    #     cw.append(parser.getkey(c,parser.lookup))
    for k in range(K):
        flag=True
        while flag:
            pos=table[random.randint(0,table_size-1)] # index of word in vocab
            chosenword=parser.vocab[pos]
            try:
                if contexts.index(chosenword):
                    continue
            except ValueError:
                Wneg.append(chosenword)
                flag=False
    return Wneg