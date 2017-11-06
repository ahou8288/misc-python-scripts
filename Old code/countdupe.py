sources={}
with open('data.txt', 'r') as f:
    for line in f:
        val=line.split()[2]
        sources.update(val=1)
print sources
