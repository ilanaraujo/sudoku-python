# Jogo de Sudoku em Python
# Autor: Ilan Araujo

# Armazena a coluna j da grade em uma lista
def Coluna(j, grade):
    coluna = []
    for i in grade:
        coluna.append(i[j])
    return coluna

# Verifica se o número já está presente na linha
def NumeroNaLinha(numero, linha, grade):
    for n in grade[linha]:
        if n == numero:
            return True
    return False

# Verifica se o número já está presente na coluna
def NumeroNaColuna(numero, j, grade):
    if numero in Coluna(j, grade):
        return True
    else:
        return False

# Verifica se o número já está presente no quadrado 3x3
def NumeroNoQuadrado(numero, linha, coluna, grade):
    linha_q = linha//3
    coluna_q = coluna//3
    for i in range(3*linha_q, 3*(linha_q + 1)):
        for j in range(3*coluna_q, 3*(coluna_q + 1)):
            if grade[i][j] == numero:
                return True
    return False

# Verifica se o número pode ser inserido na casa
def NumeroValido(n, i, j, grade):
    if(NumeroNaLinha(n, i, grade) or NumeroNaColuna(n, j, grade) or NumeroNoQuadrado(n,i, j, grade)):
        return False
    else:
        return True

# Retorna True se a grade tiver espaços vazios e False se ela estiver completa
def grade_vazia(grade):
    for i in range(9):
        for j in range(9):
            if grade[i][j] == 0:
                return True
    return False

# Imprime a grade na tela de forma organizada (prometo melhorar isso)
def imprime_grade(grade):
    for i in grade:
        print(i)

# Usuário insere a grade e joga sudoku
def main():
    print("Jogo de Sudoku.")
    print("-+-+-+-+-+-+-+-")
    print("Insira os números de cada linha. Coloque 0 nos espaços vazios")
    grade = []
    for i in range(9):
        linha = input("Insira os números da linha {a}: ".format(a = i + 1))
        linha = linha.split(" ")
        for j in range(len(linha)):
            linha[j] = int(linha[j])
        grade.append(linha)
    while grade_vazia(grade):
        imprime_grade(grade)
        numero = int(input("Escolha um número para colocar na grade: "))
        linha = int(input("Selecione a linha: ")) - 1
        coluna = int(input("Selecione a coluna: ")) - 1
        if not(grade[linha][coluna]) and NumeroValido(numero, linha, coluna, grade):
            grade[linha][coluna] = numero
        else:
            print("Número inválido.")
    print("Parabéns, você completou o jogo!")

if __name__ == "__main__":
    main()