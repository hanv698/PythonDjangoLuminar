word="hello hai hello hai hello"

wd=word.split(" ")

words={}
for i in wd:
    words[i]=wd.count(i)
print(words)


