import random

sentence = "the quick brown fox jumped over the lazy dog"

'''
the quick brown
quick brown fox
brown fox jumped
fox jumped over
jumped over the
over the lazy
the lazy dog
'''

new_content = {}
new_passage = " "

words = sentence.split()

for i in range(len(words)-2):
    try:
        next_word = random.randint(i+2,len(words)-1)
        new_content[words[i] + " " +words[i+1]] = words[next_word]
    except ValueError:
        print "value error"
        new_content[words[i] + " " +words[i+1]] = ""

print new_content
'''
for word in range(len(words)-1):
    tmp = words[word]+ " " +words[word+1]
   # print tmp
    if tmp in new_content:
        print new_content[tmp]
'''


