def paresAnagramas(string):


    grupo_anagramas = dict()
    anagramas = list()


    for y in range(1, len(string)+1):
        for x in range(0, len(string)):
            str_ordenada = "".join(sorted(string[x: x + y]))

            if len(str_ordenada) < y:
                break
            
            if str_ordenada not in grupo_anagramas:
                grupo_anagramas[str_ordenada] = [string[x: x + y]]
            else:
                grupo_anagramas[str_ordenada].append(string[x: x + y])

            if len(grupo_anagramas[str_ordenada]) >= 2 and grupo_anagramas[str_ordenada] not in anagramas:
                anagramas.append(grupo_anagramas[str_ordenada])

    return len(anagramas), anagramas

#ifailuhkqq
palavra = 'ifailuhkqq'
print(paresAnagramas(palavra))
