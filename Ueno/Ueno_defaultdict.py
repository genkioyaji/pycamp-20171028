import os
from collections import defaultdict

string= 'MPS python hello world MPS python bootcamp'
words = string.split(' ')
print(words)
words_dict=defaultdict(lambda:0)
for i in words:
    words_dict[i]+=1
print(dict(words_dict))
