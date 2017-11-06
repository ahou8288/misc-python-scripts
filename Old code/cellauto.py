rules={
'***':'.',
'**.':'*',
'*.*':'.',
'*..':'*',
'.**':'*',
'.*.':'.',
'..*':'*',
'...':'.'}
outstring=""
numlines=raw_input("Number of lines: ")
row1=raw_input("Start line: ")
ln=len(row1)
print row1
for i in xrange(int(numlines)-1):
 trow1=row1[ln-1]+row1+row1[0]
 for j in xrange(ln):
  outstring=outstring+rules[trow1[j:j+3]]
 print outstring
 row1=outstring
 outstring=""
