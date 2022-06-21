def inverte(string):
    str0=''
    for e in range(len(string)-1,-1,-1):
        str0=str0+string[e]
    return str0
