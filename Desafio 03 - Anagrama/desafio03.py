def grupoDeAnagramas(word):

    grupo_anagramas = dict()
    anagramas = list()

    for n in range(1, len(word)+1):
        for i in range(0, len(word)):
            sorted_word = "".join(sorted(word[i: i+n]))

            if len(sorted_word) < n:
                break

            if sorted_word not in grupo_anagramas:
                grupo_anagramas[sorted_word] = [word[i: i + n]]
            else:
                grupo_anagramas[sorted_word].append(word[i: i + n])

            if len(grupo_anagramas[sorted_word]) >= 2:
                anagramas.append(grupo_anagramas[sorted_word])

    return len(anagramas), anagramas

#ifailuhkqq
word = 'ifailuhkqq'
print(grupoDeAnagramas(word))
