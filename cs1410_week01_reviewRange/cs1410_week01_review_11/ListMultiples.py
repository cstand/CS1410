def listMultiples(num, length):
    newlist = []
    for i in range(length):
        newlist.append(num * (i + 1))
    return newlist
