rhymes = {"1":"fun","2":"blue", "3":"me", "4":"floor", "5":"live"}

n = input("Type a number:")
if n in rhymes:
    rhymes = rhymes[n]
    print(rhymes)
else:
    print("Not found.")
