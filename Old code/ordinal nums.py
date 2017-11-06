num = raw_input('Enter the number: ')
ln=len(num)
rchar=num[ln-1]
if rchar == "1":
    print num+"st"
elif rchar == "2":
    print num+"nd"
elif rchar == "3":
    print num+"rd"
else:
    print num+"th"
