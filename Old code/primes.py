maxnum=100
primes=[2]
i=3
while i < maxnum:
    test=False
    for j in primes:
        if i%j==0:
            test=True
    if test==False:
        primes.append(i)
    i=i+1
for prime in primes:
    print 'bing '*int(prime)
    
