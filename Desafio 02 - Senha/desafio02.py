def verificarSenha(senha):
    caracteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
    arr_senha = list(senha)

    if len(arr_senha) < 6:

        print(f'Sua senha precisa de mais {6 - len(arr_senha)} caracateres para ser considerada segura.')

    else:

        digito = False
        for dig in arr_senha:
            if dig.isnumeric():
                digito = True
                break

        if digito == False:

            print('Sua senha precisa ter pelo menos UM DÍGITO para ser considerada segura.')

        else:

            minuscula = False
            for letra in arr_senha:
                if letra.islower():
                    minuscula = True
                    break

            if minuscula == False:
                print('Sua senha precisa ter pelo menos UMA letra em MINÚSCULO para ser considerada segura.')

            else:

                maiuscula = False
                for dig in arr_senha:
                    if dig.isupper():
                        maiuscula = True
                        break

                if maiuscula == False:
                    print('Sua senha precisa ter pelo menos UMA letra em MAIÚSCULO para ser considerada segura.')

                else:

                    caractere = False
                    for carac in caracteres_especiais:
                        for dig in arr_senha:
                            if carac == dig:
                                caractere = True
                                break

                    if caractere == False:
                        print('Sua senha precisa ter pelo menos um desses caracateres especiais para ser considerada segura: !@#$%^&*()-+ ')

                    else:
                        print('Sua senha atende todos os critérios e é considerada segura.')


senha = "Ya3&ab"
verificarSenha(senha)
