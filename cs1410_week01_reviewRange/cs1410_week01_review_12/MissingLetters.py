def missingLetters(s):
    news = ""
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s:
            news += char
    return news
