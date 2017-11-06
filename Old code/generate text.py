import re
lm={}
f=open('physics.txt','r')
data=f.read()
regexp='[a-z]+'
words=re.findall(regexp,data)
print words
