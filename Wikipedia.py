# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:12:17 2020

@author: VK
"""


import wikipedia
Search1=input("What you want to search about: ")
result = wikipedia.summary(Search1, sentences = 5)

print("Here you Go!!{}".format(result))
