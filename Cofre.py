def entrada_validação():
    senha = []
    for _ in range(4):
        caracter_numerico = int(input("Insira um numero entre 0 e 9: "))
        while caracter_numerico < 0 or caracter_numerico > 9: 
            caracter_numerico = int(input("Número inválido! Insira um número entre 0 e 9: "))
    
        senha.append(caracter_numerico)
                
    return senha

def destranca_cofre(senha):
    resultado = list()
    valida_3 = int(senha[0]) + int(senha[1])
    valida_4 = int(senha[1]) + int(senha[2])    
    
    if senha[2] == valida_3 and senha[3] == valida_4:
        for i in senha:
            resultado.append(i)
        print(f"Cofre Desbloqueado{resultado}")
    
    elif senha[2] == valida_3 and senha[3] != valida_4:
        for i in senha:
            resultado.append(i)
        print (f"Erro, somente 3 digitos estão corretos,{resultado[0], resultado[1], resultado[2]}")

    elif senha[2] != valida_3 and senha[3] == valida_4:
        for i in senha:
            resultado.append(i)
        print(f'terceiro Número incorreto {senha[3]}')

    elif senha[2] != valida_3 and senha[3] != valida_4:
        for i in senha:
            resultado.append(i)
        print(f'Nenhum número correto!')
    return resultado

senha = entrada_validação()
destranca_cofre(senha)
