def last_word(s):
    for i in s:
        if i == " ":
            separate = s.split()
    print(separate)
    for j in separate:
        last_word_len = len(j)
    print(last_word_len)
s = "helloo world  "
last_word(s)


