from clipboard import copy


def tocopy(nome, end=1000):

    _nomes = nome.split()
    if len(_nomes) > 2:
        ValueError(
            "... Usarei somente o primeiro nome, pois só aceito nomes compostos por 2 nomes somente")
        _nomes = nome.split()
    elif len(_nomes) == 1:
        _nomes = [nome, nome]
    txt = ""
    if _nomes[0] != _nomes[1]:
        for i in range(1, 2+1):
            txt += f"{_nomes[0]} {_nomes[1]} CONTA {end}..."
            txt += "\n"  # if i == 1 else ". "

    else:
        for i in range(1, 2+1):
            txt += f"{_nomes[0]} {_nomes[1]} CONTA {end}..."
            txt += "\n"  # if i == 1 else ". "
    for i in range(1, end+1):
        txt += f"É {i}..."
        # print(txt, end=" ")

    txt += f"\n\n{_nomes[0]} VIVA {_nomes[1]}...\nVIVA {_nomes[1]}{''.join([_nomes[1][-1] for _ in range(10)])}..."
    print(txt)
    copy(txt)


# tocopy("ANA CAROLINA", )
tocopy("DAMILYS REGINA", 100)
