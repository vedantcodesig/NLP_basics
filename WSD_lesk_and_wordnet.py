# -*- coding: utf-8 -*-
"""
@author: Vedant Manelkar
"""
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize

sentence9 = "I went to the bank to deposit money ."
token_sen9=word_tokenize(sentence9)
token_sen9
print(lesk(token_sen9,'bank','n'))

#wordnet flex
for ss in wn.synsets('bank'):
    print(ss,ss.definition())
