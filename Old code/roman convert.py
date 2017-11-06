s=raw_input("Enter roman numerals: ")

romanNumeralMap = (('M',  1000),('CM', 900),('D',  500),('CD', 400),('C',  100),('XC', 90),('L',  50),('XL', 40),('X',  10),('IX', 9),('V',  5),('IV', 4),('I',  1))
result = 0
index = 0
for numeral, integer in romanNumeralMap:
    while s[index:index+len(numeral)] == numeral:
        result += integer
        index += len(numeral)
print result
