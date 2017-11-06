def combinations(letters,word):
    if len(word)==6:
        print word
    else:
        for letter in letters:
            combinations([i for i in letters if i<>letter],word+letter)

combinations('catdog',"")
