import re
lm={}
f=open('physics.txt','r')
data=f.read()
regexp="""[a-zA-Z0-9']+|[^a-zA-Z0-9' ]+"""
words=re.findall(regexp,data)
print words
