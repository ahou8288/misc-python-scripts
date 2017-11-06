start = int(raw_input('Enter start: '))
end = int(raw_input('Enter end: '))
import math
for x in range(start, end+1):
   # Check whether x is divisible by 5
   if math.fmod(x,5)==0:
      print x, x * 9 / 5 + 32
