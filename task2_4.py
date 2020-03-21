words = input('Enter a few words: ').split()
s = 1
for word in words:
    print(s, word[:10])
    s += 1

