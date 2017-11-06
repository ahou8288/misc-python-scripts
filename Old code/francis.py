import os
import re
os.chdir(r'C:\Users\ahoug_000\Downloads')
f=open('TEST 4.txt','r')
a=f.read()

a=re.sub('\n\n','\n',a) #remove line gaps
a=re.sub('Deg C','', a) #remove Degrees at end of line
b=sorted([i.strip().split('  ') for i in a.strip().split('\n')]) #split into an array of lines, then split each line based on the space character.
#.strip() is used to remove spaces at the beginning and end of lines.

c={} #get everything into a dictionary
for j in b:
    if j[0] in c.keys():
        c[j[0]].append(j[1])
    else:
        c[j[0]]=[j[1]]

for j in sorted(c.keys()): #print out in the right format.
    print j+' '+', '.join(c[j])
