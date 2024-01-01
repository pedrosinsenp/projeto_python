from time import sleep
from webbrowser import open
from datetime import datetime
import urllib.request

def interromper():
    """
    \033[3;93m-> Essa função será usada quando ocorrer um erro de "KeyboardInterrupt", para interromper o programa\033[m
    """

    print('\033[3;91mO usuário preferiu finalizar o programa.\033[m')
    print('\n\033[mObrigado por ultilizar este programa.\033[3;94m Volte Sempre!')
    print('https://github.com/pedrosinsenp\033[m')
    tempo()
    try:
        urllib.request.urlopen('https://github.com/pedrosinsenp')
    except:
        print('Acessa lá meu github!')
    else:
        open('https://github.com/pedrosinsenp')
    sleep(0.8)
    exit()


def titulo(iniciar_secao='<desconhecido>', msg='<desconhecido>', cor='nulo', sem_iniciar_secao=False):
    """
    \033[3;93m-> Mostra a mensagem de iniciando "", e logo após, mostra o titulo da seção escolhida.\033[m

    \033[93mArgs:
        \033[94m- iniciar_secao (str):\033[m Nome da seção que deseja. Defautls to '<desconhecido>'.
        \033[94m- msg (str):\033[m Nome da seção em forma de titulo. Defautls to '<desconhecido>'.
        \033[94m- cor (str, opcional):\033[m Nome da cor. Defaults to 'nulo'.
        \033[94m- sem_iniciar_secao:\033[m Pode ser ultilizado quando quer mostrar apenas a msg e a cor.
    
    \033[93mCores:\033[m
        - 'nulo'
        \033[93m- 'amarelo'
        \033[95m- 'roxo'
        \033[94m- 'azul'
        \033[91m- 'vermelho'
        \033[90m- 'cinza'\033[m
    """
    
    if sem_iniciar_secao == False:
        print(f'\033[m\033[3mIniciando "{iniciar_secao}"\033[m')
        sleep(0.8)

    cor = cor.lower()
    msg = msg.upper()

    while cor not in c:
        print('\033[91mERRO! \033[3mDigite uma cor válida.\033[m')
        try:
            cor = str(input('Digite uma cor:\033[92m ')).strip().lower()
        except KeyboardInterrupt:
            interromper()
        
    linha(cor)
    print(f'\033[3m{(msg):^60}\033[m')
    linha(cor)
    
    
def sair_secao(msg='<desconhecido>', cor='nulo'):
    """
    \033[3;93m-> Mostra a mensagem de saindo da seção de "".\033[m

    \033[93mArgs:
        \033[94m- msg (str):\033[m Nome da seção. Defautls to '<desconhecido>'.
        \033[94m- cor (str, optional):\033[m Nome da cor. Defaults to 'nulo'.
        
    \033[93mCores:\033[m
        - 'nulo'
        \033[93m- 'amarelo'
        \033[95m- 'roxo'
        \033[94m- 'azul'
        \033[91m- 'vermelho'
        \033[90m- 'cinza'\033[m
    """
    
    cor = cor.lower()
    while cor not in c:
        print('\033[91mERRO! \033[3mDigite uma cor válida.\033[m')
        try:
            cor = str(input('Digite uma cor:\033[92m ')).strip().lower()
        except KeyboardInterrupt:
            interromper()
        
    print(f'\033[m\033[3mSaindo da seção de {msg}\033[m')
    sleep(0.8)
    linha(cor)
    

def escolha_user(msg='<desconhecido>', num=0):
    """
    \033[3;93m-> Serve para o usuario escolher sua seção/jogada.\033[m

    \033[93mArgs:
        \033[94m- msg (str):\033[m Mensagem que aparecerá na pergunta. Defaults to '<desconhecido>'
        \033[94m- num (int):\033[m Quantidade de opções. Defaults to 0.
    """
    
    global escolha_usuario
    while True:
        try:
            escolha_usuario = str(input(f'\033[m{msg}\033[92m ')).strip()
            escolha_usuario = int(escolha_usuario)

            if escolha_usuario > num or escolha_usuario == 0:
                listagem = []
                for c in range(1, num + 1):
                    listagem.append(c)

                print(f'\033[91mERRO! \033[3m"{escolha_usuario}" não é válido.\033[m {msg} \033[1m{listagem}\033[m')
                continue
        except (TypeError, ValueError):
            print(f'\033[91mERRO! \033[3m"{escolha_usuario}" não é válido.')
            continue
        except KeyboardInterrupt:
            interromper()
        else:
            return escolha_usuario
    

def continuar_def(msg='<desconhecido>', pular=False):
    """
    \033[3;93m-> Pergunta ao usuario se deseja continuar.

    \033[93mArgs:
        \033[94m- msg (str):\033[m Mensagem que aparecerá na pergunta. Defaults to '<desconhecido>'.
        \033[94m- pular (bool, optional):\033[m Se verdadeira, irá dar quebra de linha. Defaults to False.
    """
    
    global continuar
    while True:
        try:
            if pular == False:
                continuar = str(input(f'{msg}? [S/N]\033[92m ')).upper().strip()[0]
            else:
                continuar = str(input(f'\n{msg}? [S/N]\033[92m ')).upper().strip()[0]
            
            if continuar != 'S' and continuar != 'N':
                print(f'\033[91mERRO! \033[3m"{continuar}" não é válido.\033[m')
                continue
        except KeyboardInterrupt:
            interromper()
        else:
            return continuar


def linha(cor='nulo', num='60'):
    """
    \033[3;93m-> Criar uma linha horizontal.\033[m

    \033[93mArgs:
        \033[94m- cor (str, optional):\033[m Cor da linha. Defaults to 'nulo'.
        \033[94m- num (str, optional):\033[m Tamanho da linha. Defaults to '60'.

    \033[93mReturns:
        \033[94m- linha:\033[m retorno da linha com a cor e tamanho.
        
    \033[93mCores:\033[m
        - 'nulo'
        \033[93m- 'amarelo'
        \033[95m- 'roxo'
        \033[94m- 'azul'
        \033[91m- 'vermelho'
        \033[90m- 'cinza'\033[m
    """
    
    while num.isnumeric() != True:
        print('\033[91mERRO! Digite um número inteiro.\033[m')
        try:
            num = str(input('Digite um número (tamanho da linha):\033[92m ')).strip()
        except KeyboardInterrupt:
            interromper()
            
    num = int(num)
    cor = cor.lower()

    while cor not in c:
        print('\033[91mERRO! Digite uma cor válida.\033[m')
        try:
            cor = str(input('Digite uma cor:\033[92m ')).strip().lower()
        except KeyboardInterrupt:
            interromper()
        
    return print(f'{c[cor]}~\033[m'*num)


def verificar_num(msg, num=0, sem_num_min=False, forcar_valor_int=False, senha=False):
    """
    \033[3;93m-> Essa função serve para garantir que o programa não de erro por conta de digitação.

    \033[93mArgs:
        \033[94m- msg (str):\033[m Mensagem que aparecerá ao usuario.
        \033[94m- num (int, optional):\033[m Deve ser colocado quando existir um limite de número máximo. Defaults to 0.
        \033[94m- sem_num_min (bool, optional):\033[m Deve ser modificado se o número 0 for válido na pergunta. Defaults to False.
        \033[94m- forcar_valor_int (bool, optional):\033[m Deve ser ultilizado se o número precisar necessariamente ser inteiro. Defaults to False.

    \033[93mReturns:
        \033[94m- resultado:\033[m Irá retornar o resultado que o usuario digitar
    """
    
    while True:
        try:
            a = str(input(f'{msg}\033[92m')).strip().replace(',', '.')
            if forcar_valor_int == False:
                a = float(a)
            else:
                a = int(a)

            if senha == True:
                    if a < 8:
                        print(f'\033[91mPara sua segurança, escolha uma senha com 8 ou mais caracteres.\033[m')
                        continue
            else:
                if sem_num_min == False:
                    if num == 0:
                        if a == 0:
                            print(f'\033[91mERRO! \033[3mDigite um número maior que 0\033[m')
                            continue
                    else:
                        if a > num:
                            print(f'\033[91mERRO! \033[3mDigite um número menor que {num + 1}\033[m')
                            continue
                        elif a == 0:
                            print(f'\033[91mERRO! \033[3mDigite um número maior que 0\033[m')
                            continue
        except (TypeError, ValueError):
            if forcar_valor_int == True:
                if '.' in a:
                    print(f'\033[91mERRO! \033[3mDigite um valor inteiro.\033[m')
                    continue
                else:
                    print(f'\033[91mERRO! \033[3m"{a}" não é válido.\033[m')
                    continue
            else:
                print(f'\033[91mERRO! \033[3m"{a}" não é válido.\033[m')
                continue
        except KeyboardInterrupt:
            interromper()
        else:
            return a


def menu(*n):
    """
    \033[3;93m-> Essa função serve para criar o menu onde o usuário irá fazer sua escolha

    \033[93mArgs:
        \033[94m- *n (str):\033[m Opções que o usuário terá de escolher
    """

    try:
        print()
        for i, c in enumerate(n):
            print(f'\033[94m{f"[{(i + 1):^5}]":>11}\033[m - \033[3m{c}\033[m')
        print()
    except:
        print('\033[91mERRO! Tivemos um pequeno erro no sistema\033[m')
        print('\n\033[mObrigado por ultilizar este programa.\033[3;94m Volte Sempre!')
        print('https://github.com/pedrosinsenp\033[m')
        tempo()
        try:
            urllib.request.urlopen('https://github.com/pedrosinsenp')
        except:
            print('Acessa lá meu github!')
        else:
            open('https://github.com/pedrosinsenp')
        sleep(0.8)
        exit()

    
def tempo():
    """
    \033[3;93m-> Essa função serve para mostrar o tempo e data de maneira formatada\033[m
    """

    if len(str(datetime.now().hour)) == 1:
        print(f'0{datetime.now().hour}', end=':')
    else:
        print(f'{datetime.now().hour}', end=':')

    if len(str(datetime.now().minute)) == 1:
        print(f'0{datetime.now().minute}', end=':')
    else:
        print(f'{datetime.now().minute}', end=':')

    if len(str(datetime.now().second)) == 1:
        print(f'0{datetime.now().second}', end=' ')
    else:
        print(f'{datetime.now().second}', end=' ')

    if len(str(datetime.now().day)) == 1:
        print(f'0{datetime.now().day}', end='/')
    else:
        print(f'{datetime.now().day}', end='/')

    if len(str(datetime.now().month)) == 1:
        print(f'0{datetime.now().month}', end='/')
    else:
        print(f'{datetime.now().month}', end='/')

    print(datetime.now().year)


    # CORES
c = {'nulo': '\033[m',         # Sem cor
    'amarelo': '\033[93m',     # Amarelo
    'roxo': '\033[95m',        # Roxo
    'azul': '\033[94m',        # Azul
    'vermelho': '\033[91m',    # Vermelho
    'cinza': '\033[90m',       # Cinza
    'verde': '\033[92m'        # Verde
    }
