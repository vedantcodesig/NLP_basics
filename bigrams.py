# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 01:05:31 2022

@author: Vedant Manelkar
"""

import nltk
from nltk.tokenize import word_tokenize
text='Hi how are you? IT deparmen won dance lmao xd IT lmao xd dance op'
nltk_tokens = nltk.word_tokenize(text)  	
bigrams=list(nltk.bigrams(nltk_tokens))
print(bigrams)
no_bigrams=len(bigrams)
iT_count=text.count('IT')
bg_count = bigrams.count(('IT', 'deparmen'))


# probabily of 'deparmen' given 'IT' P(bigram | IT)
p1=bg_count/iT_count
print(p1)
# probabilty of bigram in text P(some text)
# i.e. pick a bigram at random, what's the probability it's your bigram:
p2=bg_count/no_bigrams    
print(p2)