def getlen(text: str):
    print(text)
    if text == '':
        return 0
    else:
        return 1 + getlen(text[1:])


a = getlen("Olá mundo")
print(a)
