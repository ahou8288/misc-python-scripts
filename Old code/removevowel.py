import re
f1=open('sms-phrases.txt','r')
f2=open('sms-message.txt','r')
data=f2.read()
print data
for line in f1:
    splitter=line.split(' ',1)
    word=splitter[0]
    replacement=splitter[1].rstrip()
    pat=re.compile(word)
    data=pat.sub(replacement,data)
print data
