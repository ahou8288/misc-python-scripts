sentence = raw_input('Enter some text: ')
vowels = ('a','e','i','o','u','A','E','I','O','U')
out=[]
for word in sentence.split():
 ln=len(word)
 if not word.startswith(vowels):
  out.append(word[1:]+word[0]+'ay')
 else:
  out.append(word+'way')
print ' '.join(out)
