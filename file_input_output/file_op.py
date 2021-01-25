f=open("demo","r")

word=[]
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for w in words:
        word.append(w)
print(word)