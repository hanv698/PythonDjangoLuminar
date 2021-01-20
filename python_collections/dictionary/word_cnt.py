word="hello hai hello hai hello"

wrd=word.split(" ")

#for i in words:
 #   print(i,":",words.count(i))

words={}
for i in wrd:
    words[i]=wrd.count(i)
print(words)


