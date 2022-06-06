# -*- coding: utf-8 -*-
"""
@author: Vedant Manelkar
"""
import nltk

sample_text10="""
Rama killed Ravana to save Sita from Lanka.The legend of the Ramayan is the most popular Indian epic.A lot of movies and serials have already
been shot in several languages here in India based on the Ramayana.
"""

words=nltk.word_tokenize(sample_text10)
  # print(words)
tagged_words=nltk.pos_tag(words)
  # print(tagged_words)
chunkGram=r"""NN: {}"""
chunkParser=nltk.RegexpParser(chunkGram)
chunked=chunkParser.parse(tagged_words)
chunked.draw()