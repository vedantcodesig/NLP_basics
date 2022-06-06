# -*- coding: utf-8 -*-
"""
@author: Vedant Manelkar
"""

import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence7 = """Today morning, Arthur felt very good."""
tokens = nltk.word_tokenize(sentence7)
tagged = nltk.pos_tag(tokens)
print(tagged)

