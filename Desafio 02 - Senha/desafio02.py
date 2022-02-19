"""
Possui no mínimo 6 caracteres.
Contém no mínimo 1 digito.
Contém no mínimo 1 letra em minúsculo.
Contém no mínimo 1 letra em maiúsculo.
Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+"""


def verificarSenha(senha):
    caracteres_especiais = '!@#$%^&*()-+'
    carac_especial = False

    if len(senha) < 6:
        carac_faltantes = 6 - len(senha)
        print('- Sua senha precisa ter pelo menos 6 dígitos;', f'- Você precisa de mais {carac_faltantes} caractere(s);', sep='\n')
    elif senha.isalpha():
        print('- Sua senha precisa de pelo menos 1 número para ser considerada segura;')
    elif senha.isupper():
        print('- Sua senha precisa de pelo menos 1 letra em minúsculo;')
    elif senha.islower():
        print('- Sua senha precisa de pelo menos 1 letra em maiúsculo;')
    else:
        for letra in senha:
            if letra in caracteres_especiais:
                carac_especial = True
                break
        if carac_especial:
            print('- Sua senha é considerada segura de acordo com todos os critérios.')
        else:
            print('- Sua senha precisa de pelo menos 1 caractere especial: !@#$%^&*()-+')


senha = input('Digite sua senha: ')
verificarSenha(senha)
