# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 01:04:24 2022

@author: Vedant Manelkar
"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
ps = PorterStemmer()
lm=WordNetLemmatizer()  
sentence = "Programmers program with programming languages"
words = word_tokenize(sentence)  
for w in words:
    print(w, " : ", ps.stem(w))
    print(w,":",lm.lemmatize(w))