

def frequencies(items):
    frequencies = {}
    for i in items:
        if type(i) != str:
            n = items.index(i)
            items[n] = str(i)
    
    for i in items:
        frequencies[i] = items.count(i)

    return frequencies


print(f"The frequencies of each input are {frequencies(['a', 'a', 'b', 'b', 'b', 'c', '100', 100])}")
