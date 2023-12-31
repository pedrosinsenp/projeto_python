from funções import funcoes
from time import sleep

def soma():
    """
    \033[3;93m-> Função de soma
    """
    cont = tot_zero_soma = 0
    numeros = []
    while True:
        try:
            cont += 1
            usuario_num = funcoes.verificar_num(f'\033[m{cont}º Valor [0 -> parar]:\033[92m ', sem_num_min=True)
            numeros.append(usuario_num)

            if usuario_num == 0:
                print('')
                    
                funcoes.continuar_def('\033[mRealmente deseja parar')
                if funcoes.continuar == 'S':
                    for i, c in enumerate(numeros):
                        if c == 0:
                            numeros.pop(i)
                    break
                else:
                    continue
        except KeyboardInterrupt:
            print('\033[3;91mO usuário preferiu finalizar o programa.\033[m')
            sleep(0.8)
            exit()

    print(f'\n\033[mOs números digitados foram {numeros}')
    print(f'A soma entre os {len(numeros)} valores é igual a \033[94m{sum(numeros)}\033[m')
    sleep(0.8)


def subtracao():
    """
    \033[3;93m-> Função de subtração
    """
    n1 = funcoes.verificar_num('\n\033[mPrimeiro valor:\033[92m ', sem_num_min=True)
    n2 = funcoes.verificar_num('\033[mSegundo valor:\033[92m ', sem_num_min=True)
    print(f'\033[m{n1} - {n2} é igual a {(n1 - n2):.2f}')


def multiplicacao():
    """
    \033[3;93m-> Função de multiplicação
    """
    n1 = funcoes.verificar_num('\n\033[mPrimeiro valor:\033[92m ', sem_num_min=True)
    n2 = funcoes.verificar_num('\033[mSegundo valor:\033[92m ', sem_num_min=True)
    print(f'\033[m{n1} x {n2} é igual a {(n1 * n2):.2f}')


def divisao():
    """
    \033[3;93m-> Função de divisão
    """
    n1 = funcoes.verificar_num('\n\033[mPrimeiro valor:\033[92m ', sem_num_min=True)
    n2 = funcoes.verificar_num('\033[mSegundo valor:\033[92m ', sem_num_min=True)
    try:
        print(f'\033[m{n1} / {n2} é igual a {(n1 / n2):.2f}')
    except ZeroDivisionError:
        print(f'\033[91mERRO!\033[m Não é possivel dividir um valor por 0.')