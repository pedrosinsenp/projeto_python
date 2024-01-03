from random import randint, choice, shuffle
from time import sleep
from math import factorial, sin, cos, tan, radians, hypot
from datetime import date, datetime
from funções import funcoes
from funções import operacoes_mat
from webbrowser import open
import urllib.request

    # PROGRAMA PRINCIPAL
funcoes.titulo(sem_iniciar_secao=True, msg='PrOJeTO V1.0', cor='amarelo')
print('Olá! Bem vindo ao projeto v1.0!'.replace("Da", "da").replace("De", 'de').replace("Dos", "dos").replace("Das", "Das"))

while True:
    funcoes.menu('Jogos', 'Matemática', 'Gerador', 'Sortear',
                'Brasileirão', 'Alistamento', 'Caixa eletrônico',
                'Conversão', 'Desconto', 'Aumento', 'Juros', 'Sistema de ajuda', 'Finalizar programa')

    funcoes.escolha_user('Qual sua seção?', 13)

    if funcoes.escolha_usuario == 1:    # SEÇÃO DE JOGOS
        funcoes.titulo('seção de jogos', 'SEÇÃO DE JOGOS', 'roxo')

        while True:
            funcoes.menu('Pedra, Papel e Tesoura', 'Jogo da Advinhação',
                         'Palíndromo', 'Palíndromo', 'Sair da seção de jogos')

            funcoes.escolha_user('Qual seu jogo?', 5)
            
            if funcoes.escolha_usuario == 1:   # PEDRA, PAPEL E TESOURA
                funcoes.titulo('Pedra, papel e tesoura', 'JOGO DE PEDRA, PAPEL E TESOURA', 'azul')

                while True:
                    funcoes.menu('PEDRA', 'PAPEL', 'TESOURA',
                                 'Sair da seção de jogo de pedra, papel e tesoura')

                    funcoes.escolha_user('Qual sua jogada?', 4)
                    
                    if funcoes.escolha_usuario == 4:
                        sleep(0.7)
                        break

                    bot = randint(0, 2)
                    sleep(0.5)
                    print('\n\033[93mJO')
                    sleep(0.5)
                    print('KEN')
                    sleep(0.5)
                    print('PO!!!\033[m')

                    if funcoes.escolha_usuario == 1:
                        print('\nJogador jogou \033[32mPEDRA\033[m')
                    elif funcoes.escolha_usuario == 2:
                        print('\nJogador jogou \033[32mPAPEL\033[m')
                    else:
                        print('\nJogador jogou \033[32mTESOURA\033[m')

                    if bot == 1:
                        print('Computador jogou \033[32mPEDRA\033[m')
                    elif bot == 2:
                        print('Computador jogou \033[32mPAPEL\033[m')
                    else:
                        print('Computador jogou \033[32mTESOURA\033[m')

                    if funcoes.escolha_usuario == 1 and bot == 3 or funcoes.escolha_usuario == 2 and bot == 1 or funcoes.escolha_usuario == 3 and bot == 2:
                        print('\n\033[94mVocê venceu!🎉\033[m', end=' ')
                        funcoes.continuar_def('Vamos jogar novamente')
                        
                        if funcoes.continuar == 'N':
                            sleep(0.6)
                            break
                        else:
                            funcoes.linha('azul', '50')
                    
                    elif funcoes.escolha_usuario == bot:
                        print('\n\033[93mEmpatamos!\033[m', end=' ')
                        funcoes.continuar_def('Vamos jogar novamente')
                        
                        if funcoes.continuar == 'N':
                            sleep(0.6)
                            break
                        else:
                            funcoes.linha('azul', '50')
                    
                    else:
                        print('\n\033[94m\033[94mVocê perdeu😔\033[m', end=' ')
                        funcoes.continuar_def('Vamos jogar novamente')
                        
                        if funcoes.continuar == 'N':
                            sleep(0.6)
                            break
                        else:
                            funcoes.linha('azul', '50')

                funcoes.sair_secao('pedra, papel e tesoura', 'roxo')

            elif funcoes.escolha_usuario == 2: # JOGOS DA ADIVINHÇÃO
                funcoes.titulo('Jogo da Adivinhação', 'JOGO DA ADIVINHAÇÃO', 'azul')

                while True:
                    funcoes.menu('Jogo da Adivinhação v1.0',
                                 'Jogo da Adivinhação v2.0',
                                 'Voltar')
                        
                    funcoes.escolha_user('Qual sua opção?', 3)

                    if funcoes.escolha_usuario == 1:    # jogo 1
                        funcoes.titulo('Jogo da Adivinhação v1.0', 'JOGO DA ADIVINHAÇÃO v1.0', 'vermelho')

                        while True:
                            funcoes.menu('Facil', 'Normal', 'Difícil', 'Voltar')

                            funcoes.escolha_user('Qual seu nível?', 4)
                            
                            if funcoes.escolha_usuario == 1:     # Nível 1
                                print('\033[mVou pensar em um número entre \033[94m1 e 5\033[m. Tente adivinhar...')
                                bot = randint(1, 5)
                                print('\033[mEstou escolhendo um número...')
                                sleep(1)
                                escolha_jogador = funcoes.verificar_num('Qual número eu pensei? ', 5, forcar_valor_int=True)
                                sleep(0.7)

                                if escolha_jogador == bot:
                                    print('\n\033[94mPARABÉNS!\033[m Você conseguiu me vencer!', end=' ')
                                else:
                                    print(f'\n\033[94mGANHEI!\033[m Eu pensei no número \033[94m{bot}\033[m e não no \033[94m{escolha_jogador}\033[m!', end=' ')
                                    
                                funcoes.continuar_def('Vamos continuar')
                                if funcoes.continuar == 'N':
                                    funcoes.linha('azul')
                                    sleep(0.6)
                                    break
                                else:
                                    funcoes.linha('vermelho')
                                
                            elif funcoes.escolha_usuario == 2:   # Nível 2
                                print('\033[mVou pensar em um número entre \033[94m1 e 10\033[m. Tente adivinhar...')
                                bot = randint(1, 10)
                                print('\033[mEstou escolhendo um número...')
                                sleep(1)
                                escolha_jogador = funcoes.verificar_num('Qual número eu pensei? ', 10, forcar_valor_int=True)
                                sleep(0.7)

                                if escolha_jogador == bot:
                                    print('\n\033[94mPARABÉNS!\033[m Você conseguiu me vencer!', end=' ')
                                else:
                                    print(f'\n\033[94mGANHEI!\033[m Eu pensei no número \033[94m{bot}\033[m e não no \033[94m{escolha_jogador}\033[m!', end=' ')
                                    
                                funcoes.continuar_def('Vamos continuar')
                                if funcoes.continuar == 'N':
                                    funcoes.linha('azul')
                                    sleep(0.6)
                                    break
                                else:
                                    funcoes.linha('vermelho')

                            elif funcoes.escolha_usuario == 3:   # nível 3
                                print('\033[mVou pensar em um número entre \033[94m1 e 20\033[m. Tente adivinhar...')
                                bot = randint(1, 20)
                                print('\033[mEstou escolhendo um número...')
                                sleep(1)
                                escolha_jogador = funcoes.verificar_num('Qual número eu pensei? ', 20, forcar_valor_int=True)
                                sleep(0.7)

                                if escolha_jogador == bot:
                                    print('\n\033[94mPARABÉNS!\033[m Você conseguiu me vencer!', end=' ')
                                else:
                                    print(f'\n\033[94mGANHEI!\033[m Eu pensei no número \033[94m{bot}\033[m e não no \033[94m{escolha_jogador}\033[m!', end=' ')
                                    
                                funcoes.continuar_def('Vamos continuar')
                                if funcoes.continuar == 'N':
                                    funcoes.linha('azul')
                                    sleep(0.6)
                                    break
                                else:
                                    funcoes.linha('vermelho')
                                
                            else:
                                funcoes.sair_secao('jogo da Adivinhação v1.0', 'azul')

                    elif funcoes.escolha_usuario == 2:  # Jogo 2
                        funcoes.titulo('Jogo da Adivinhação v2.0', 'JOGO DA ADIVINHAÇÃO v2.0', 'vermelho')

                        while True:
                            funcoes.menu('Facil', 'Normal', 'Difícil', 'Voltar')

                            funcoes.escolha_user('Qual sua nivel?\033[92m', 4)
                            
                            if funcoes.escolha_usuario == 1:     # Nível 1
                                bot = randint(1, 10)
                                print('\033[mAcabei de pensar em um número entre \033[94m1 a 10\033[m.')
                                print('Será que você consegui adivinhar qual foi?')
                                cont = 0
                                escolha_jogador = funcoes.verificar_num('Qual número eu pensei? ', 10, forcar_valor_int=True)

                                while escolha_jogador != bot:
                                    cont += 1
                                    if escolha_jogador > bot:
                                        print('\033[3;94mMenos... Tente mais uma vez.')
                                        escolha_jogador = funcoes.verificar_num('\033[mQual é seu palpite? ', 10, forcar_valor_int=True)
                                    else:
                                        print('\033[3;94mMais... Tente mais uma vez.')
                                        escolha_jogador = funcoes.verificar_num('\033[mQual é seu palpite? ', 10, forcar_valor_int=True)

                                print(f'\033[mAcertou com \033[92m{cont}\033[m tentativas. Parabéns!')

                                funcoes.continuar_def('Quer jogar novamente', True)
                                    
                                if funcoes.continuar == 'N':
                                    funcoes.linha('azul')
                                    sleep(0.6)
                                    break
                                else:
                                    funcoes.linha('vermelho')

                            elif funcoes.escolha_usuario == 2:   # Nível 2
                                bot = randint(0, 20)
                                print('\033[mAcabei de pensar em um número entre \033[94m1 a 20\033[m.')
                                print('Será que você consegui adivinhar qual foi?')
                                cont = 0
                                escolha_jogador = funcoes.verificar_num('Qual número eu pensei? ', 20, forcar_valor_int=True)

                                while escolha_jogador != bot:
                                    cont += 1
                                    if escolha_jogador > bot:
                                        print('\033[3;94mMenos... Tente mais uma vez.')
                                        escolha_jogador = funcoes.verificar_num('\033[mQual é seu palpite? ', 20, forcar_valor_int=True)
                                    else:
                                        print('\033[3;94mMais... Tente mais uma vez.')
                                        escolha_jogador = funcoes.verificar_num('\033[mQual é seu palpite? ', 20, forcar_valor_int=True)

                                print(f'\033[mAcertou com \033[92m{cont}\033[m tentativas. Parabéns!')

                                funcoes.continuar_def('Quer jogar novamente', True)
                                    
                                if funcoes.continuar == 'N':
                                    funcoes.linha('azul')
                                    sleep(0.6)
                                    break
                                else:
                                    funcoes.linha('vermelho')
                            
                            elif funcoes.escolha_usuario == 3:   # Nível 3
                                bot = randint(0, 30)
                                print('\033[mAcabei de pensar em um número entre \033[94m1 a 30\033[m.')
                                print('Será que você consegui adivinhar qual foi?')
                                cont = 0
                                escolha_jogador = funcoes.verificar_num('Qual número eu pensei? ', 30, forcar_valor_int=True)

                                while escolha_jogador != bot:
                                    cont += 1
                                    if escolha_jogador > bot:
                                        print('\033[3;94mMenos... Tente mais uma vez.')
                                        escolha_jogador = funcoes.verificar_num('\033[mQual é seu palpite? ', 30, forcar_valor_int=True)
                                    else:
                                        print('\033[3;94mMais... Tente mais uma vez.')
                                        escolha_jogador = funcoes.verificar_num('\033[mQual é seu palpite? ', 30, forcar_valor_int=True)

                                print(f'\033[mAcertou com \033[92m{cont}\033[m tentativas. Parabéns!')

                                funcoes.continuar_def('Quer jogar novamente', True)
                                    
                                if funcoes.continuar == 'N':
                                    funcoes.linha('azul')
                                    sleep(0.6)
                                    break
                                else:
                                    funcoes.linha('vermelho')

                            else:
                                funcoes.sair_secao('jogo da adivinhação v2.0', 'azul')
                                break

                    else:
                        funcoes.sair_secao('jogo da adivinhação', 'roxo')
                        break

            elif funcoes.escolha_usuario == 3: # PAR OU ÍMPAR
                funcoes.titulo('Par ou Ímpar', 'JOGO DE PAR OU ÍMPAR', 'azul')

                while True:
                    funcoes.menu('Iniciar jogos', 'Sair da seção do jogo par ou ímpar')

                    funcoes.escolha_user('Qual sua opção', 2)

                    if funcoes.escolha_usuario == 1:
                        cont = 0
                        bot = par_impar = ''

                        while True:
                            escolha_usuario = funcoes.verificar_num('\n\033[mDiga um valor: ', forcar_valor_int=True)
                            usuario = str(input('\033[mPar ou Ímpar? [P/I]\033[92m ')).upper()
                            while usuario != 'P' and usuario != 'I':
                                print('\033[91mOpção inválida\033[m. Tente novamente')
                                usuario = str(input('\033[mPar ou Ímpar? [P/I]\033[92m ')).upper()

                            if usuario == 'P':
                                bot = 'I'
                            else:
                                bot = 'P'

                            bot_num = randint(1, 10)
                            tot = escolha_usuario + bot_num

                            if tot % 2 == 0:
                                vencedor = 'PAR'
                            else:
                                vencedor = 'IMPAR'

                            print(f'\n\033[mVocê jogou \033[95m{escolha_usuario}\033[m e o computador jogou \033[95m{bot_num}\033[m. Total de \033[95m{tot}\033[m DEU \033[94m{vencedor}\033[m')
                            funcoes.linha('azul', '40')

                            if vencedor[0] == usuario:
                                print('\033[94mVocê venceu!\033[m')
                            else:
                                print('\033[91mVocê perdeu!\033[m')
                                
                            funcoes.continuar_def('Quer jogar novamente')

                            if funcoes.continuar == 'N':
                                sleep(0.6)
                                break
                            else:
                                funcoes.linha('azul', '40')


                    funcoes.sair_secao('par ou ímpar', 'roxo')
                    break

            elif funcoes.escolha_usuario == 4: # PALÍNDROMO
                funcoes.titulo('Palíndromo', 'JOGO DE PALÍNDROMO', 'azul')

                while True:
                    funcoes.menu('Iniciar jogo', 'Sair da seção de palíndromo')

                    funcoes.escolha_user('Qual sua opção?', 2)

                    if funcoes.escolha_usuario == 1:
                        while True:
                            frase = str(input('\033[mDigite uma frase:\033[92m ')).upper().replace(' ', '')
                            inverso = frase[::-1]
                            print(f'\033[mO inverso de \033[94m{frase}\033[m é \033[94m{inverso}\033[m')
                            if frase == inverso:
                                print('\nA frase digitada \033[95mÉ UM PALÍNDROMO\033[m')
                            else:
                                print('\nA frase digitada \033[95mNÃO É UM PALÍNDROMO\033[m')
                            
                            funcoes.continuar_def('Vamos continuar')
                                
                            if funcoes.continuar == 'N':
                                sleep(0.6)
                                break
                            else:
                                funcoes.linha('azul')

                    funcoes.sair_secao('palíndromo', 'roxo')
                    break

            else:
                funcoes.sair_secao('jogos', 'amarelo')
                break

    elif funcoes.escolha_usuario == 2:  # SEÇÃO DE MATEMÁTICA
        funcoes.titulo('seção de matemática', 'SEÇÃO DE MATEMÁTICA', 'roxo')

        while True:
            funcoes.menu('Operações Matemáticas', 'calcular média', 'Par ou Ímpar',
                         'Tabuada', 'Sequência de Fibonacci', 'Progressão Aritmética',
                         'Fatorial', 'Índice de Massa Corporal', 'Análise de Triângulos',
                         'Seno, Cosseno e Tangente', 'Hipotenusa', 'Sair da seção de matemática')
            
            funcoes.escolha_user('Qual sua opção?', 12)

            if funcoes.escolha_usuario == 1:      # OPERAÇÕES MATEMÁTICAS
                funcoes.titulo('Operações Matemáticas', 'SEÇÃO DE OPERAÇÕES MATEMÁTICAS', 'azul')

                while True:
                    funcoes.menu('Soma', 'Subtração', 'Multiplicação',
                                 'Divisão', 'Sair da seção de operadores matemáticos')

                    funcoes.escolha_user('Qual sua opção?', 5)

                    if funcoes.escolha_usuario == 1:    # Soma
                        funcoes.titulo('Soma', 'SEÇÃO DE SOMA', 'cinza')

                        cont = tot_zero_soma = 0
                        numeros = []

                        while True:
                            funcoes.menu('Iniciar programa', 'Sair da seção de soma')
                            
                            funcoes.escolha_user('Qual sua opção?', 2)
                            print('')

                            if funcoes.escolha_usuario == 1:
                                operacoes_mat.soma()

                            funcoes.sair_secao('soma', 'azul')
                            break

                    elif funcoes.escolha_usuario == 2:  # Subtração
                        funcoes.titulo('Subtração', 'SEÇÃO DE SUBTRAÇÃO', 'cinza')

                        while True:
                            funcoes.menu('Iniciar programa', 'Sair da seção de subtração')
                            
                            funcoes.escolha_user('Qual sua opção?', 2)
                            
                            if funcoes.escolha_usuario == 1:
                                while True:
                                    operacoes_mat.subtracao()

                                    funcoes.continuar_def('Quer continuar', True)
                                        
                                    if funcoes.continuar == 'N':
                                        sleep(0.7)
                                        break
                                    else:
                                        funcoes.linha('azul', '50')
                                        
                            funcoes.sair_secao('subtração', 'azul')
                            break

                    elif funcoes.escolha_usuario == 3:  # Multiplicação
                        funcoes.titulo('Multiplicação', 'SEÇÃO DE MULTIPLIACAÇÃO', 'cinza')

                        while True:
                            funcoes.menu('Iniciar programa', 'Sair da seção de multiplicação')
                             
                            funcoes.escolha_user('Qual sua opção?', 2)
                            
                            if funcoes.escolha_usuario == 1:
                                while True:
                                    operacoes_mat.multiplicacao()

                                    funcoes.continuar_def('Quer continuar', True)
                                        
                                    if funcoes.continuar == 'N':
                                        sleep(0.7)
                                        break
                                    else:
                                        funcoes.linha('azul', '50')

                            funcoes.sair_secao('multiplicação', 'azul')
                            break

                    elif funcoes.escolha_usuario == 4:  # Divisão
                        funcoes.titulo('Divisão', 'SEÇÃO DE DIVISÃO' 'cinza')

                        while True:
                            funcoes.menu('Iniciar programa', 'Sair da seção de divisão')

                            funcoes.escolha_user('Qual sua opção?', 2)
                            
                            if funcoes.escolha_usuario == 1:
                                while True:
                                    operacoes_mat.divisao()

                                    funcoes.continuar_def('Quer continuar', True)
                                    
                                    if funcoes.continuar == 'N':
                                        sleep(0.7)
                                        break
                                    else:
                                        funcoes.linha('azul', '50')

                            funcoes.sair_secao('divisão', 'azul')
                            break

                    else:
                        funcoes.sair_secao('operações matemáricas', 'roxo')
                        break

            elif funcoes.escolha_usuario == 2:    # CALCULAR MÉDIA
                funcoes.titulo('Calcular média', 'SEÇÃO DE CALCULAR MÉDIA', 'azul')

                while True:
                    funcoes.menu('Iniciar programa', 'Sair da seção de calcular média')
                        
                    funcoes.escolha_user('Qual sua opção?', 2)

                    if funcoes.escolha_usuario == 1:
                        while True:
                                lista = []
                                usuarios = []
                                aprovados = []
                                reprovados = []

                                while True:
                                    usuarios.append(str(input('\n\033[mNome:\033[92m ')).strip().title().replace("Da", "da").replace("De", 'de').replace("Dos", "dos").replace("Das", "das"))
                                    nota01 = funcoes.verificar_num('\033[mNota 1:\033[92m ', 10)
                                    usuarios.append(nota01)
                                    nota02 = funcoes.verificar_num('\033[mNota 2:\033[92m ', 10)
                                    usuarios.append(nota02)

                                    lista.append(usuarios[:])
                                    usuarios.clear()

                                    print()
                                    funcoes.continuar_def('\033[94mQuer continuar')
                                    
                                    if funcoes.continuar == 'N':
                                        break

                                print(f'\n\033[1m{"No.":<3} {"NOME":<15} {"MÉDIA":<9} {"RESULTADO":<0}\033[m')
                                funcoes.linha('azul', '39')
                                for i, c in enumerate(lista):
                                    if ((c[1] + c[2]) / 2) < 6:
                                        reprovados.append(c[0])
                                        print(f'{i:<3} \033[3m{c[0]:<15}\033[m \033[91m{((c[1] + c[2]) / 2):<9}\033[m \033[1m{"[Reprovado]":<0}\033[m'.replace('.', ','))
                                    else:
                                        aprovados.append(c[0])
                                        print(f'{i:<3} \033[3m{c[0]:<15}\033[m \033[94m{((c[1] + c[2]) / 2):<9}\033[m \033[1m{"[Aprovado]":<0}\033[m'.replace('.', ','))
                                funcoes.linha('azul', '39')

                                if len(aprovados) == 0:
                                    print('Não ouve nenhum aluno aprovado!')
                                else:
                                    print('\033[mOs alunos aprovados foram:')
                                    for c in aprovados:
                                        print(f'\033[94m{c}\033[m')

                                print()

                                if len(reprovados) == 0:
                                    print('Não ouve nenhum aluno reprovado!')
                                else:
                                    print('E os reprovados:')
                                    for c in reprovados:
                                        print(f'\033[91m{c}\033[m')

                                funcoes.linha('azul', '36')
                                
                                funcoes.continuar_def('Quer ver as notas de algum aluno')
                                    
                                if funcoes.continuar == 'S':
                                    while True:
                                        aluno = funcoes.verificar_num('\n\033[mQuer mostrar as notas de qual aluno? [999 interromper]:\033[92m ', forcar_valor_int=True)
                                        if aluno == 999:
                                                break
                                        else:
                                            print(f'\033[mAs notas de \033[3m{lista[aluno][0]}\033[m são {lista[aluno][1]} e {lista[aluno][2]}'.replace('.', ','))
                                funcoes.linha('azul', '36')
                                break

                    else:
                        funcoes.sair_secao('calcular média', 'roxo')
                        break

            elif funcoes.escolha_usuario == 3:    # PAR OU ÍMPAR
                funcoes.titulo('Par ou Ímpar', 'SEÇÃO DE PAR OU ÍMPAR', 'azul')

                while True:
                    funcoes.menu('Iniciar programa', 'Sair da seção de par ou ímpar')
                    
                    funcoes.escolha_user('Qual sua opção?', 2)

                    if funcoes.escolha_usuario == 1:
                        while True:
                            num = funcoes.verificar_num('\n\033[mMe diga um número qualquer:\033[92m ')
                            
                            if num % 2 == 0:
                                print(f'\033[m O número {num} é \033[3;94mPAR\033[m')
                            else:
                                print(f'\033[m O número {num} é \033[3;94mÍmpar\033[m')

                            funcoes.continuar_def('Quer continar', True)
                                
                            if funcoes.continuar == 'N':
                                funcoes.linha('azul')
                                break
                           
                    else:        
                        funcoes.sair_secao('par ou ímpar', 'roxo')
                        break

            elif funcoes.escolha_usuario == 4:    # TABUADA
                funcoes.titulo('Tabuada', 'SEÇÃO DE TABUADA', 'azul')

                while True:
                    funcoes.menu('Iniciar programa', 'Sair da seção de tabuada')
                        
                    funcoes.escolha_user('Qual sua opção?', 2)

                    if funcoes.escolha_usuario == 1:
                        while True:
                            num = funcoes.verificar_num('\033[mDigite um número para a tabuada [0 -> parar]:\033[92m ', sem_num_min=True, forcar_valor_int=True)
                            if num == 0:
                                funcoes.continuar_def('\033[mDeseja realmente finalizar o programa')
                                
                                if funcoes.continuar == 'S':
                                    break
                                else:
                                    funcoes.linha('azul', '40')

                            else:
                                print('')
                                for c in range(1, 11):
                                    print(f'\033[m{num} x {c} = \033[94m{num * c}\033[m')
                                print('')
                                funcoes.linha('azul', '40')

                    funcoes.sair_secao('tabuada', 'roxo')
                    break

            elif funcoes.escolha_usuario == 5:    # SEQUÊNCIA DE FIBONACCI
                funcoes.titulo('Sequência de Fibonacci', 'SEÇÃO DE SEQUÊNCIA DE FIBONACCI', 'azul')

                while True:
                    funcoes.menu('Iniciar programa', 'Sair da seção de Fibonacci')
                        
                    funcoes.escolha_user('Qual sua opção?', 2)

                    if funcoes.escolha_usuario == 1:
                        num = funcoes.verificar_num('\033[mQuantos termos você quer mostrar?\033[92m ', forcar_valor_int=True)
                        num -= 2
                        funcoes.linha('verde')
                        t1 = 0
                        t2 = 1
                        print(f'0 \033[92m->\033[m 1 \033[92m->\033[m ', end="")
                        while True:
                            cont = 0
                            while cont != num:
                                t3 = t1 + t2
                                print(t3, end=' \033[92m->\033[m ')
                                t1 = t2
                                t2 = t3
                                cont += 1
                            print('\033[3;92mFIM\033[m')
                            funcoes.linha('verde')
                            
                            funcoes.continuar_def('Quer ver mais')
                                
                            if funcoes.continuar == 'N':
                                break
                            else:
                                num = funcoes.verificar_num('\033[mQuantos termos você quer ver a mais?\033[92m ', forcar_valor_int=True)
                                funcoes.linha('verde')
                            
                    funcoes.sair_secao('sequência de Fibonacci', 'roxo')
                    break

            elif funcoes.escolha_usuario == 6:    # PROGRESSÃO ARITMÉTICA
                funcoes.titulo('Prograssão Aritmética', 'SEÇÃO DE PROGRESÃO ARITMÉTICA', 'azul')

                while True:
                    funcoes.menu('Iniciar programa', 'Sair da seção de progressão aritmética')
                        
                    funcoes.escolha_user('Qual sua opção?', 2)

                    if funcoes.escolha_usuario == 1:
                        termo = funcoes.verificar_num('\n\033[mPrimeiro termo:\033[32m ', sem_num_min=True, forcar_valor_int=True)
                        razao = funcoes.verificar_num('\033[mRazão de PA:\033[32m ', forcar_valor_int=True)
                        cont = 0
                        cont_termos = 0
                        quantidade = 10
                        while True:
                            funcoes.linha('verde')
                            for cont in range(termo, (termo + (quantidade * razao)), razao):
                                print(f'\033[m{termo}', end=' \033[92m->\033[m ')
                                termo += razao
                                cont += 1
                            print('\033[3;92mFIM\033[m')
                            funcoes.linha('verde')
                            
                            funcoes.continuar_def('Quer ver mais')
                            
                            if funcoes.continuar == 'N':
                                break
                            
                            quantidade = funcoes.verificar_num('\n\033[mQuantos termos você quer mostrar a mais?\033[92m ', forcar_valor_int=True)
                            cont_termos += 1

                    funcoes.sair_secao('progressão aritmética', 'roxo')
                    break

            elif funcoes.escolha_usuario == 7:    # FATORIAL
                funcoes.titulo('Fatorial', 'SEÇÃO DE FATORIAL', 'azul')

                while True:
                    funcoes.menu('Iniciar programa', 'Sair da seção de fatorial')
                        
                    funcoes.escolha_user('Qual sua opção?', 2)
                    
                    if funcoes.escolha_usuario == 1:
                        while True:
                            num = funcoes.verificar_num('\n\033[mDigite um número para seu Fatorial:\033[92m ', forcar_valor_int=True)
                            funcoes.linha('verde', '50')
                            print(f'\033[mCalculando \033[94m{num}!\033[m = ', end=' ')
                            for c in range(num, 0, -1):
                                if c == 1:
                                    print(c, end=' = ')
                                else:
                                    print(f'{c} x', end=' ')
                            print(f'\033[94m{factorial(num)}\033[m')
                            funcoes.linha('verde', '50')

                            funcoes.continuar_def('Quer ver mais')

                            if funcoes.continuar == 'N':
                                break

                    funcoes.sair_secao('fatorial', 'roxo')
                    break

            elif funcoes.escolha_usuario == 8:    # IMC
                funcoes.titulo('Índice de Massa Corporal', 'SEÇÃO DE IMC', 'roxo')

                while True:
                    funcoes.menu('Iniciar programa', 'Sair da seção de IMC')

                    funcoes.escolha_user('Qual sua opção?', 2)
                    
                    if funcoes.escolha_usuario == 1:
                        try:
                            urllib.request.urlopen('https://pedrosinsenp.github.io/calculadora-imc/')
                        except:
                            usuario = 2
                        else:
                            funcoes.linha('azul')
                            funcoes.menu('Site', 'Programa')
                            usuario = funcoes.verificar_num('Deseja acessar o site ou ir pelo programa?\033[92m ', 2)
                        while True:
                            if usuario == 1:
                                try:
                                    urllib.request.urlopen('https://pedrosinsenp.github.io/calculadora-imc/')
                                except:
                                    print('\033[91mOcorreu algum erro ao acessar o site\033[m')
                                    usuario = 2
                                    continue
                                else:
                                    open('https://pedrosinsenp.github.io/calculadora-imc/')
                                    break
                            else:
                                peso = funcoes.verificar_num('\n\033[mQual seu peso?\033[92m ')
                                altura = funcoes.verificar_num('\033[mQual sua altura?\033[92m ')
                                if altura > 100:
                                    altura /= 100
                                imc = peso / (altura ** 2)

                                if imc <= 18.5:
                                    print(f'\n\033[mSeu IMC é \033[3;94m{(imc):.1f}\033[m'.replace('.' , ','))
                                    print('Você está \033[91mABAIXO DO PESO!\033[m')
                                elif imc < 25:
                                    print(f'\n\033[mSeu IMC é \033[3;94m{(imc):.1f}\033[m'.replace('.' , ','))
                                    print('Você está no \033[94mPESO IDEAL\033[m (parabéns)')
                                elif imc < 30:
                                    print(f'\n\033[mSeu IMC é \033[3;94m{(imc):.1f}\033[m'.replace('.' , ','))
                                    print('Você está \033[91mACIMA DO PESO\033[m')
                                elif imc < 35:
                                    print(f'\n\033[mSeu IMC é \033[3;94m{(imc):.1f}\033[m'.replace('.' , ','))
                                    print('Você está em \033[91mOBESIDADE GRAU I!\033[m')
                                elif imc < 40:
                                    print(f'\n\033[mSeu IMC é \033[3;94m{(imc):.1f}\033[m'.replace('.' , ','))
                                    print('Você está em \033[91mOBESIDADE GRAU II!\033[m (severa)')
                                elif imc >= 40:
                                    print(f'\n\033[mSeu IMC é \033[3;94m{(imc):.1f}\033[m'.replace('.' , ','))
                                    print('Você está \033[3;91mOBESIDADE GRAU III!\033[m (mórbida)')
                                else:
                                    print('\n\033[91mErro!\033[m Verifique sua credenciais!')

                                funcoes.continuar_def('Quer ver mais', True)
                                    
                                if funcoes.continuar == 'N':
                                    break
                                else:
                                    funcoes.linha('azul', '50')

                    funcoes.sair_secao('IMC', 'roxo')
                    break

            elif funcoes.escolha_usuario == 9:    # SEÇÃO DE ANÁLISE DE TRINÂNGULOS
                funcoes.titulo('Análose de Triângulos', 'SEÇÃO DE ANÁLISE DE TRIÂNGULOS', 'azul')

                while True:
                    funcoes.menu('Análise de Triângulos v1.0', 'Análise de Triângulos v2.0', 'Sair da seção de análise de triângulos')

                    funcoes.escolha_user('Qual sua opção?', 3)
                    
                    if funcoes.escolha_usuario == 1:      # Análise de Triângulos v1.0
                        while True:
                            s1 = funcoes.verificar_num('\n\033[mPrimeiro segmento:\033[92m ')
                            s2 = funcoes.verificar_num('\033[mSegundo segmento:\033[92m ')
                            s3 = funcoes.verificar_num('\033[mTerceiro segmento:\033[92m ')
                            if s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2:
                                print('\n\033[mOs segmentos acima \033[3;94mPODEM FORMAR triângulo!\033[m')
                            else:
                                print('\n\033[mOs segmentos acima \033[3;91mNÃO PODEM FORMAR triângulo!\033[m')

                            funcoes.continuar_def('Quer análisar mais algum')
                            funcoes.linha('azul', '50')
                            
                            if funcoes.continuar == 'N':
                                break

                    elif funcoes.escolha_usuario == 2:     # Análise de Triângulos v2.0
                        while True:
                            s1 = funcoes.verificar_num('\n\033[mPrimeiro segmento:\033[92m ')
                            s2 = funcoes.verificar_num('\033[mSegundo segmento:\033[92m ')
                            s3 = funcoes.verificar_num('\033[mTerceiro segmento:\033[92m ')
                            
                            if s1 == s2 and s2 == s3 and s1 == s3:
                                print('\n\033[mOs segmentos acima podem formar um\033[3;94m TRIÂNGULO EQUILÁTERO (todos os lados iguais)\033[m')
                            elif s1 == s2 and s1 != s3 or s2 == s3 and s2 != s1 or s3 == s1 and s3 != s2:
                                print('\n\033[mOs segmentos acima podem formar um\033[̣3;94m TRIÂNGULO ISÓCELES (dois lados iguais)\033[m')
                            elif s1 != s2 and s1 != s3 or s2 != s3 or s3 != s1:
                                print('\n\033[mOs segmentos acima podem formar um\033[3;94m TRIÂNGULO ESCALENO (todos os lados difetentes)\033[m')
                            
                            funcoes.continuar_def('Quer análisar mais algum')
                            funcoes.linha('azul', '50')
                            
                            if funcoes.continuar == 'N':
                                break

                    else:
                        funcoes.sair_secao('análise de triângulos', 'roxo')
                        break

            elif funcoes.escolha_usuario == 10:   # SEÇÃO DE SENO, COSSENO E TANGENTE
                funcoes.titulo('Seno, Cosseno e Tangente', 'SEÇÃO DE SENO, COSSENO E TANGENTE', 'azul')

                while True:
                    angulo = funcoes.verificar_num('\033[mDigite o ângulo que você deseja calcular:\033[92m ')

                    funcoes.menu('Seno', 'Cosseno', 'Tangente', 'Sair da seção de seno, cosseno e tangente')
                        
                    funcoes.escolha_user('Qual sua opção?', 4)
                    
                    if funcoes.escolha_usuario == 1:  # Seno
                        print(f'\033[mO ângulo de \033[94m{angulo}°\033[m tem o SENO de \033[3;94m{(sin(radians(angulo))):.2f}\033[m')

                        funcoes.continuar_def('Quer calcular mais algum', True)
                        
                        if funcoes.continuar == 'N':
                            break
                        else:
                            funcoes.linha('azul', '50')
                            print('')

                    elif funcoes.escolha_usuario == 2:    # Cosseno
                        print(f'\033[mO ângulo de \033[94m{angulo}°\033[m tem o COSSENO de \033[3;94m{(cos(radians(angulo))):.2f}\033[m')
                        
                        funcoes.continuar_def('Quer calcular mais algum', True)
                            
                        if funcoes.continuar == 'N':
                            break
                        else:
                            funcoes.linha('azul', '50')
                            print('')

                    elif funcoes.escolha_usuario == 3:    # Tangente
                        print(f'\033[mO ângulo de \033[94m{angulo}°\033[m tem o TANGENTE de \033[3;94m{(tan(radians(angulo))):.2f}\033[m')
                        
                        funcoes.continuar_def('Quer calcular mais algum', True)
                            
                        if funcoes.continuar == 'N':
                            break
                        else:
                            funcoes.linha('azul', '50')
                            print('')
                            
                    else:
                        break
                    
                funcoes.sair_secao('seno, cosseno e tangente', 'roxo')

            elif funcoes.escolha_usuario == 11:   # SEÇÃO DE HIPOTENUSA
                funcoes.titulo('Hipotenusa', 'SEÇÃO DE HIPOTENUSA', 'azul')

                funcoes.menu('Iniciar programa', 'Sair da seção de hipotenusa')

                funcoes.escolha_user('Qual sua opção?', 2)
            
                if funcoes.escolha_usuario == 1:
                    while True:
                        co = funcoes.verificar_num('\n\033[mComprimento do cateto oposto:\033[92m ')
                        ca = funcoes.verificar_num('\033[mComprimento do cateto adjacente:\033[92m ')

                        print('')
                        funcoes.linha('azul', '50')
                        print(f'\033[mA hipotenusa vai medir \033[3;94m{(hypot(co, ca)):.2f}\033[m')
                        funcoes.linha('azul', '50')

                        funcoes.continuar_def('Quer calcular mais algum', True)
                        
                        if funcoes.continuar == 'N':
                            break
                        else:
                            funcoes.linha('azul', '50')
                        
                funcoes.sair_secao('hipotenusa', 'roxo')

            else:
                funcoes.sair_secao('matemática', 'amarelo')
                break

    elif funcoes.escolha_usuario == 3:  # SEÇÃO DE GERADORES
        funcoes.titulo('Seção de Geradores', 'SEÇÃO DE GERADORES', 'roxo')

        while True:
            funcoes.menu('Gerador de valores', 'Gerador de senhas',
                         'Gerador de nomes', 'Gerar palpites para Mega Sena',
                         'sair da seção de geradores')
            
            funcoes.escolha_user('Qual sua opção?', 5)

            if funcoes.escolha_usuario == 1:      # GERADOR DE VALORES
                funcoes.titulo('Gerador de valores', 'SEÇÃO DE GERADOR DE VALORES', 'azul')

                while True:
                    funcoes.menu('Números até 10', 'Números até 100', 'Números até 200',
                                 'Personalizar', 'Sair da seção de gerador de valores')
                    
                    funcoes.escolha_user('Qual sua opção?', 5)

                    if funcoes.escolha_usuario != 5:
                        quant_valores_usuario = funcoes.verificar_num('\033[mQuantos valores vão ser gerados?\033[92m ', forcar_valor_int=True)

                    if funcoes.escolha_usuario == 1:      # <= 10
                        print(f'\n\033[mOs valores gerados foram:', end=' ')

                        for c in range(0, quant_valores_usuario):
                            num = randint(0, 10)
                            if quant_valores_usuario > 1:
                                if c == quant_valores_usuario - 1:
                                    print(f'\033[3;94m{num}\033[m')
                                else:
                                    print(f'\033[3;94m{num}\033[m', end=' | ')
                            else:
                                print(f'{num}')

                        funcoes.continuar_def('Quer gerar mais algum valor')
                            
                        if funcoes.continuar == 'N':
                            break

                        funcoes.linha('azul', '50')
                        print('')

                    elif funcoes.escolha_usuario == 2:    # <= 100
                        print(f'\n\033[mOs valores gerados foram:', end=' ')

                        for c in range(0, quant_valores_usuario):
                            num = randint(0, 100)
                            if quant_valores_usuario > 1:
                                if c == quant_valores_usuario - 1:
                                    print(f'\033[3;94m{num}\033[m')
                                else:
                                    print(f'\033[3;94m{num}\033[m', end=' | ')
                            else:
                                print(f'{num}')
                                
                        funcoes.continuar_def('Quer gerar mais algum valor')
                            
                        if funcoes.continuar == 'N':
                            break

                        funcoes.linha('azul', '50')
                        print('')

                    elif funcoes.escolha_usuario == 3:    # <= 200
                        print(f'\n\033[mOs valores gerados foram:', end=' ')

                        for c in range(0, quant_valores_usuario):
                            num = randint(0, 200)
                            if quant_valores_usuario > 1:
                                if c == quant_valores_usuario - 1:
                                    print(f'\033[3;94m{num}\033[m')
                                else:
                                    print(f'\033[3;94m{num}\033[m', end=' | ') 
                            else:
                                print(f'{num}')

                        funcoes.continuar_def('Quer gerar mais algum valor')
                            
                        if funcoes.continuar == 'N':
                            break

                        funcoes.linha('azul', '50')
                        print('')

                    elif funcoes.escolha_usuario == 4:    # Personalizado
                        menor = funcoes.verificar_num('\033[mSeu valor vai começar com qual número?\033[92m ', forcar_valor_int=True)

                        maior = funcoes.verificar_num('\033[mE vai até que número?\033[92m ', forcar_valor_int=True)

                        print(f'\n\033[mOs valores gerados foram:', end=' ')

                        for c in range(0, quant_valores_usuario):
                            num = randint(menor, maior)
                            if quant_valores_usuario > 1:
                                if c == quant_valores_usuario - 1:
                                    print(f'\033[3;94m{num}\033[m')
                                else:
                                    print(f'\033[3;94m{num}\033[m', end=' | ')
                            else:
                                print(f'{num}')

                        funcoes.continuar_def('Quer gerar mais algum valor')
                            
                        if funcoes.continuar == 'N':
                            break

                        funcoes.linha('azul', '50')
                        print('')
                        
                    else:
                        break
                    
                funcoes.sair_secao('gerador de valores', 'roxo')

            elif funcoes.escolha_usuario == 2:    # GERADOR DE SENHAS
                funcoes.titulo('Gerador de senhas', 'SEÇÃO DE GERADOR DE SENHAS', 'azul')

                while True:
                    funcoes.menu('Senha fraca', 'Senha média', 'Senha forte', 'Sair da seção de gerador de senhas')
                        
                    funcoes.escolha_user('Qual sua opção?', 4)

                    senha = ''
                    verificar_carac = 0
                    verificar_maiu = 0
                    verificar_minu = 0
                    verificar_num = 0
                    
                    if funcoes.escolha_usuario == 1:   # SENHA FRACA
                        senha_carac = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz'
                        tamanho_senha = funcoes.verificar_num('\033[mQual o tamanho da senha?\033[92m ', forcar_valor_int=True, senha=True)
                            
                        print('\033[3mGerando senha...\033[m')
                        sleep(1)

                        while True:
                            for c in range(0, tamanho_senha):
                                escolha = choice(senha_carac)
                                senha += escolha
                                if escolha.isupper():
                                    verificar_maiu = 1
                                if escolha.islower():
                                    verificar_minu = 1
                                    
                            if verificar_minu and verificar_maiu == 1:
                                break
                            else:
                                senha = ''
                                verificar_minu = 0
                                verificar_maiu = 0

                        print(f'\n\033[mA senha gerada foi \033[94m{senha}\033[m')

                        funcoes.continuar_def('Quer gerar mais alguma senha')
                            
                        if funcoes.continuar == 'N':
                            break

                        funcoes.linha('azul', '50')
                        print('')

                    elif funcoes.escolha_usuario == 2: # SENHA MÉDIA
                        senha_carac = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz' + '1234567890'
                        tamanho_senha = funcoes.verificar_num('\033[mQual o tamanho da senha?\033[92m ', forcar_valor_int=True, senha=True)
                            
                        print('\033[3mGerando senha...\033[m')
                        sleep(0.9)

                        while True:
                            for c in range(0, tamanho_senha):
                                escolha = choice(senha_carac)
                                senha += escolha
                                if escolha.isnumeric():
                                    verificar_num = 1
                                if escolha.isupper():
                                    verificar_maiu = 1
                                if escolha.islower():
                                    verificar_minu = 1

                            if verificar_minu and verificar_maiu and verificar_num == 1:
                                break
                            else:
                                senha = ''
                                verificar_minu = 0
                                verificar_maiu = 0
                                verificar_num = 0

                        print(f'\n\033[mA senha gerada foi \033[94m{senha}\033[m')

                        funcoes.continuar_def('Quer gerar mais alguma senha')
                        
                        if funcoes.continuar == 'N':
                            break

                        funcoes.linha('azul', '50')
                        print('')
                    
                    elif funcoes.escolha_usuario == 3: # SENHA FORTE
                        senha_carac = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz' + '1234567890' + '!#$&@'
                        tamanho_senha = funcoes.verificar_num('\033[mQual o tamanho da senha?\033[92m ', forcar_valor_int=True, senha=True)
                            
                        print('\033[3mGerando senha...\033[m')
                        sleep(0.9)

                        while True:
                            for c in range(0, tamanho_senha):
                                escolha = choice(senha_carac)
                                senha += escolha
                                if escolha.isnumeric():
                                    verificar_num = 1
                                if escolha.isupper():
                                    verificar_maiu = 1
                                if escolha.islower():
                                    verificar_minu = 1
                                if escolha in '!#$&@':
                                    verificar_carac = 1
                                    
                            if verificar_minu and verificar_carac and verificar_maiu and verificar_num == 1:
                                break
                            else:
                                senha = ''
                                verificar_carac = 0
                                verificar_minu = 0
                                verificar_maiu = 0
                                verificar_num = 0
                            
                        print(f'\n\033[mA senha gerada foi \033[94m{senha}\033[m')

                        funcoes.continuar_def('Quer gerar mais alguma senha')
                            
                        if funcoes.continuar == 'N':
                            break

                        funcoes.linha('azul', '50')
                        print('')
                        verificar_carac = 0
                        verificar_maiu = 0
                        verificar_minu = 0
                        verificar_num = 0
                        
                    else:
                        break                    
                    
                funcoes.sair_secao('gerador de senhas', 'roxo')

            elif funcoes.escolha_usuario == 3:    # GERADOR DE NOMES
                funcoes.titulo('Gerador de nomes', 'SEÇÃO DE GERADOR DE NOMES', 'azul')

                while True:
                    funcoes.menu('Nome masculino', 'Nome feminino', 'Sair da seção de gerador de nomes')

                    funcoes.escolha_user('Qual sua opção?', 3)

                    nomes_masculinos = ['João', 'Lucas', 'Pedro', 'Mateus', 'Davi', 'Arthur', 'Bernardo', 'Heitor', 'Rafael', 'Miguel', 'Enzo', 'Ethan', 'Gabriel', 'Lucca', 'Benjamin', 'Nicolas', 'Guilherme', 'Gustavo', 'Murilo', 'Felipe', 'Samuel', 'Henrique', 'Lorenzo', 'Vinicius', 'Joaquim', 'Leonardo', 'Ryan', 'Ian', 'Antônio', 'Victor', 'Bruno', 'Carlos', 'Davi Lucas', 'Kaique', 'Patrick', 'Igor', 'Diego', 'Alexandre', 'Mateus Henrique', 'Gustavo Henrique', 'Gabriel', 'Luiz Miguel', 'Felipe', 'Lucas Gabriel', 'Pedro Henrique', 'Leonardo', 'Vinicius', 'Vicente', 'Eduardo', 'Fillipi', 'Paulo', 'Willian', 'Fernando', 'José', 'Wesley', 'Murilo']
                    
                    nomes_femininos = ['Helena', 'Alice', 'Laura', 'Manuela', 'Valentina', 'Sophia', 'Isabella', 'Heloísa', 'Luiza', 'Júlia', 'Lorena', 'Lívia', 'Maria', 'Luiza', 'Cecília', 'Giovanna', 'Maria Clara', 'Maria Eduarda', 'Mariana', 'Lara', 'Beatriz', 'Antonella', 'Maria Júlia', 'Emanuelly', 'Isadora', 'Ana', 'Clara', 'Melissa', 'Ana Luiza', 'Ana Júlia', 'Esther', 'Lavínia', 'Maitê', 'Maria Cecília', 'Maria Alice', 'Sarah', 'Elisa',' Liz', 'Yasmin', 'Isabelly', 'Alícia', 'Clara', 'Isis', 'Rebeca', 'Rafaela', 'Marina', 'Ana Laura', 'Maria Helena', 'Agatha', 'Gabriela', 'Catarina', 'Letícia', 'Mirella', 'Nicole', 'Luna', 'Maria Vitória', 'Olívia', 'Vitória', 'Maria', 'Maria Fernanda', 'Ana Beatriz', 'Allana', 'Maria Valentina', 'Milena', 'Emilly', 'Ayla', 'Maria', 'Flor', 'Maya', 'Bianca', 'Clarice', 'Aurora', 'Larissa', 'Mariah', 'Pietra', 'Laís', 'Stella', 'Eduarda', 'Maria Heloísa', 'Ana Lívia', 'Ana Sophia', 'Maria', 'Laura', 'Carolina', 'Ana', 'Vitória', 'Malu', 'Gabrielly', 'Ana Liz', 'Analu', 'Maria Sophia', 'Ana Cecília', 'Amanda', 'Louise', 'Heloise', 'Fernanda', 'Ana', 'Melina', 'Maria Isis','Bella', 'Joana', 'Isabel', 'Melinda','Pérola']

                    if funcoes.escolha_usuario == 1:    # Nome masculino
                        nome_escolhido = choice(nomes_masculinos)
                        print(f'\n\033[mO nome gerado foi \033[1;94m{nome_escolhido}\033[m')
                        funcoes.linha('roxo')
                        
                    elif funcoes.escolha_usuario == 2:  # nome Feminino
                        nome_escolhido = choice(nomes_femininos)
                        print(f'\n\033[mO nome gerado foi \033[1;94m{nome_escolhido}\033[m')
                        funcoes.linha('roxo')
                        
                    else:
                        funcoes.sair_secao('gerador de nomes', 'roxo')
                        break
                    
            elif funcoes.escolha_usuario == 4:    # GERADOR DE PALPITES PARA MEGA SENA
                funcoes.titulo('Gerador de palpites para Mega Sena', 'JOGO DA MEGA SENA', 'azul')
                lista = []
                valor = []

                while True:
                    palpites = funcoes.verificar_num('\n\033[mQuantos jogos você quer que eu sorteie?\033[92m ', forcar_valor_int=True)
                    print()

                    print(f'\033[3;94m{(f" SORTEANDO {palpites} JOGOS "):~^60}\033[m')
                    print()

                    for l in range(0, palpites):
                        for c in range(0, 6):
                            num = randint(1, 60)
                            if num not in valor:
                                valor.append(num)
                            else:
                                while num in valor:
                                    num = randint(1, 60)
                                valor.append(num)
                        lista.append(valor[:])
                        valor.clear()
                        
                    for pos, c in enumerate(lista):
                        print(f'Jogo {pos + 1}: \033[94m{c}\033[m')
                        
                    print()
                    print(f'\033[3;94m{(f" < BOA SORTE! > "):~^60}\033[m')
                    
                    funcoes.continuar_def('Quer gerar mais palpites')
                    
                    if funcoes.continuar == 'N':
                        funcoes.linha('roxo')
                        break

            else:
                funcoes.sair_secao('geradores', 'amarelo')
                break

    elif funcoes.escolha_usuario == 4:  # SEÇÃO DE SORTEAR
        funcoes.titulo('Seção de sortear', 'SEÇÃO DE SORTEAR', 'roxo')

        while True:
            funcoes.menu('Sortear nomes', 'Embaralhar', 'Colocar em ordem alfabética', 'Sair da seção de sortear')
            
            funcoes.escolha_user('Qual sua opção?', 4)
            
            if funcoes.escolha_usuario == 1:    # Sortear nomes
                funcoes.titulo('Sortear nomes', 'SEÇÃO DE SORTEAR NOMES', 'azul')

                while True:
                    funcoes.menu('Iniciar programa', 'Sair da seção de sortear nomes')

                    funcoes.escolha_user('Qual sua opção?', 2)

                    if funcoes.escolha_usuario == 1:
                        lista = []
                        cont = 0
                        while True:
                            cont += 1
                            nomes = str(input(f'\n\033[m{cont}ª nome:\033[92m '.replace("Da", "da").replace("De", 'de').replace("Dos", "dos").replace("Das", "Das"))).title().strip()
                            while nomes.isalpha() == False:
                                nomes = str(input(f'\033[91mERRO! "{nomes}" não é válido.\033[m {cont}ª nome:\033[92m '.replace("Da", "da").replace("De", 'de').replace("Dos", "dos").replace("Das", "Das"))).strip().title()
                                
                            nomes = lista.append(nomes)
                            
                            funcoes.continuar_def('\033[94mQuer continuar')
                                
                            if funcoes.continuar == 'N':
                                break
                        quant_sorteados = funcoes.verificar_num(f'\n\033[mDos {cont} nomes, quantos serão sorteados?\033[92m ', (len(lista) - 1), forcar_valor_int=True)

                        if quant_sorteados == 1:
                            for c in range(0, quant_sorteados):
                                sorteado = choice(lista)
                            print(f'\033[mO nome sorteado foi...')
                            sleep(0.9)
                            print('\n\033[93m3')
                            sleep(0.9)
                            print('2')
                            sleep(0.9)
                            print('1\033[m')
                            sleep(0.9)
                            print(f'\n{sorteado}'.replace("'", "").replace('[', '').replace(']', '').replace("Da", "da").replace("De", 'de').replace("Dos", "dos").replace("Das", "Das"))
                            funcoes.linha('azul', '50')
                            
                        else:
                            sorteados = []
                            for c in range(0, quant_sorteados):
                                sort = choice(lista)
                                escolhidos = sorteados.append(sort)
                                lista.remove(sort)
                            print(f'\033[mOs nomes sorteados foram...')
                            sleep(0.9)
                            print('\n\033[94m3')
                            sleep(0.9)
                            print('2')
                            sleep(0.9)
                            print('1\033[m')
                            sleep(0.9)
                            print(f'\n{sorteados}'.replace("'", "").replace('[', '').replace(']', '').replace("Da", "da").replace("De", 'de').replace("Dos", "dos").replace("Das", "Das"))
                            funcoes.linha('azul', '50')

                    else:
                        funcoes.sair_secao('sortear nomes', 'roxo')
                        break

            elif funcoes.escolha_usuario == 2:  # Embaralhar
                funcoes.titulo('Embaralhar', 'SEÇÃO DE EMBARALHAR', 'azul')

                while True:
                    funcoes.menu('Iniciar programa', 'Sair da seção de embaralhar')
                    
                    funcoes.escolha_user('Qual sua opção?', 2)

                    if funcoes.escolha_usuario == 1:
                        lista = []
                        cont = 0
                        while True:
                            cont += 1
                            individuo = str(input(f'\n\033[m{cont}ª indivíduo:\033[92m '.replace("Da", "da").replace("De", 'de').replace("Dos", "dos").replace("Das", "Das"))).title().strip()
                            while individuo.isalpha() == False:
                                individuo = str(input(f'\033[91mERRO! "{individuo}" não é válido.\033[m {cont}ª indivíduo:\033[92m '.replace("Da", "da").replace("De", 'de').replace("Dos", "dos").replace("Das", "Das"))).strip().title()
                                
                            individuo = lista.append(individuo)
  
                            funcoes.continuar_def('Quer continuar')

                            if funcoes.continuar == 'N':
                                break
                        print(f'\033[3mEmbaralhando...\033[m')
                        sleep(0.9)
                        shuffle(lista)
                        cont = 0
                        for c in lista:
                            cont += 1
                            print(f'\033[3;94m{cont}º\033[m {c}'.replace("Da", "da").replace("De", 'de').replace("Dos", "dos").replace("Das", "Das"))
                        funcoes.linha('azul', '50')

                    else:
                        funcoes.sair_secao('embaralhar', 'roxo')
                        break

            elif funcoes.escolha_usuario == 3:  # Ordem alfabética
                funcoes.titulo('Ordem alfabética', 'SEÇÃO DE ORDEM ALFABÉTICA', 'azul')

                while True:
                    funcoes.menu('Iniciar programa', 'Sair da seção de ordem alfabética')
                        
                    funcoes.escolha_user('Qual sua opção?', 2)
                    
                    if funcoes.escolha_usuario == 1:
                        lista = []
                        cont = 0
                        while True:
                            cont += 1
                            individuo = str(input(f'\n\033[m{cont}ª indivíduo:\033[92m '.replace("Da", "da").replace("De", 'de').replace("Dos", "dos").replace("Das", "Das"))).title().strip()
                            while individuo.isalpha() == False:
                                individuo = str(input(f'\033[91mERRO! "{individuo}" não é válido.\033[m {cont}ª indivíduo:\033[92m '.replace("Da", "da").replace("De", 'de').replace("Dos", "dos").replace("Das", "Das"))).strip().title()
                                
                            individuo = lista.append(individuo)
                            
                            funcoes.continuar_def('Quer continuar')
                                
                            if funcoes.continuar == 'N':
                                break
                        print(f'\033[3mOrdenando...\033[m')
                        print('')
                        sleep(0.9)
                        lista = sorted(lista)
                        cont_list = 0
                        for c in lista:
                            cont_list += 1
                            print(f'\033[94m{cont_list}º\033[m \033[3m{c}\033[m'.replace("Da", "da").replace("De", 'de').replace("Dos", "dos").replace("Das", "Das"))
                        print('')
                        funcoes.linha('azul', '50')

                    else:
                        funcoes.sair_secao('ordem alfabética', 'roxo')
                        break

            else:
                funcoes.sair_secao('sortear', 'amarelo')
                break

    elif funcoes.escolha_usuario == 5:  # SEÇÃO DO BRASILEIRÃO
        funcoes.titulo('Seção do brasileirão', 'TABELA BRASILEIRÃO | desatualizada', 'roxo')

        cont = cont2 = cont4 = 0
        cont3 = 21
        tabela = [{'Botafofo':'\033[91m'}, {'Bragantino':'\033[90m'}, {'Flamengo':'\033[91m'}, {'Grêmio':'\033[94m'},  {'Palmeiras':'\033[92m'},
                {'Athletico-PR':'\033[91m'}, {'Athletico-MG':'\033[90m'}, {'Fortaleza':'\033[94m'}, {'Fluminense':'\033[92m'},
                {'Cuiabá':'\033[92m'}, {'Sâo Paulo':'\033[91m'}, {'Internacional':'\033[91m'}, {'Corinthians':'\033[90m'}, {'Bahia':'\033[94m'},
                {'Cruzeiro':'\033[94m'}, {'Vasco':'\033[91m'}, {'Santos':'\033[90m'}, {'Goiás':'\033[92m'}, {'Coritiba':'\033[92m'}, {'América-MG':'\033[92m'}]

        while True:
            funcoes.menu('Tabela', 'Ranking dos top 5', 'Ranking dos últimos',
                         'Tabela em ordem alfabética', 'Procurar time', 'Sair da seção do brasileirão')

            funcoes.escolha_user('Qual sua opção?', 6)

            if funcoes.escolha_usuario == 1:    # Tabela
                funcoes.titulo(msg='TABELA', cor='amarelo', sem_iniciar_secao=True)
                for c in tabela:
                    for i in c:
                        cont += 1
                        print(f'\033[94m{cont}.\033[m \033[3m{i}\033[m')
                        sleep(0.4)
                funcoes.linha('amarelo')
                sleep(0.7)

            elif funcoes.escolha_usuario == 2:  # Top 5
                funcoes.titulo(msg='TOP 5', cor='amarelo', sem_iniciar_secao=True)
                for c in tabela[:5]:
                    for i in c:
                        cont2 += 1
                        print(f'\033[94m{cont2}.\033[m \033[3m{i}\033[m')
                        sleep(0.6)
                funcoes.linha('amarelo')
                sleep(0.7)

            elif funcoes.escolha_usuario == 3:  # 4 últimos
                funcoes.titulo(msg='5 ÚLTIMOS', cor='amarelo', sem_iniciar_secao=True)
                num = len(tabela)
                for c in tabela[-5:]:
                    for i in c:
                        cont3 -= 1
                        print(f'\033[94m{cont3}.\033[m \033[3m{i}\033[m')
                        sleep(0.6)
                funcoes.linha('amarelo')
                sleep(0.7)

            elif funcoes.escolha_usuario == 4:  # Ordem alfabética
                funcoes.titulo(msg='ORDEM ALFABÉTICA', cor='amarelo', sem_iniciar_secao=True)
                for c in sorted(tabela):
                    for i in c:
                        cont4 += 1
                        print(f'\033[94m{cont4}.\033[m \033[3m{i}\033[m')
                        sleep(0.4)
                funcoes.linha('amarelo')
                sleep(0.7)

            elif funcoes.escolha_usuario == 5:  # Procurar time
                lista = []
                for p, c in enumerate(tabela):
                    for i in c:
                        lista.append(i)
                funcoes.linha('amarelo')
                time = str(input('\033[mQue time deseja procurar?\033[92m ')).strip().title()
                
                    # Times com acentos
                if time == 'Botafogo':
                    time = 'Botafofo'
                if time == 'Athletico-pr':
                    time = 'Athletico-PR'
                if time == 'Cuiaba':
                    time = 'Cuiabá'
                if time == 'Gremio':
                    time = 'Grêmio'
                if time == 'Sao Paulo':
                    time = 'São Paulo'
                if time == 'Goias':
                    time = 'Goiás'
                if time == 'Athletico-mg':
                    time = 'Athletico-MG'
                if time == 'America-MG':
                    time = 'América-MG'
                
                    # Decidir cor
                if time in lista:
                    for p, c in enumerate(tabela):
                        for i in c:
                            if time == i:
                                print(f'\n\033[mO time \033[3m{c[i]}{i}\033[m está na {p + 1}ª posição')
                                funcoes.linha('amarelo')
                                sleep(0.7)
                else:
                    print('\033[91mDesculpe! Time não encontrado\033[m')
                    funcoes.linha('amarelo')
                    sleep(0.7)

            else:
                funcoes.sair_secao('brasileirão', 'amarelo')
                break

    elif funcoes.escolha_usuario == 6:  # SEÇÃO DE ALISTAMENTO
                funcoes.titulo('Alistamento', 'SEÇÃO DE ALISTAMENTO', 'roxo')

                while True:
                    funcoes.menu('Iniciar programa', 'Sair da seção de alistamento')
                        
                    funcoes.escolha_user('Qual sua opção?', 2)

                    if funcoes.escolha_usuario == 1:
                        ano_atual = date.today().year
                        ano = funcoes.verificar_num('\n\033[mAno de nascimento:\033[92m ', ano_atual, forcar_valor_int=True)
                        idade = ano_atual - ano
                        print(f'\033[mQuem nasceu em {ano} tem \033[94m{idade}\033[m anos em {ano_atual}.')
                        if idade < 18:
                            print(f'Ainda faltam \033[94m{18 - idade}\033[m anos para seu alistamento')
                            print(f'Seu alistamento será em \033[94m{ano_atual + (18 - idade)}\033[m')
                        elif idade > 18:
                            print(f'Você já deveria ter se alistado há \033[91m{(idade - 18)}\033[m anos.')
                            print(f'Seu alistamento foi em \033[91m{ano_atual - (idade - 18)}\033[m.')
                        else:
                            print('Você tem que se alistar \033[91mIMEDIATAMENTE!')
                        funcoes.linha('azul', '50')

                    else:
                        funcoes.sair_secao('alistamento', 'amarelo')
                        break

    elif funcoes.escolha_usuario == 7:  # SEÇÃO DE CAIXA ELETRÔNICO
                funcoes.titulo('Caixa eletrônico', 'CAIXA ELETRÔNICO', 'roxo')

                while True:
                    funcoes.menu('Iniciar programa', 'Sair da seção de caixa eletrônico')
                        
                    funcoes.escolha_user('Qual sua opção?', 2)

                    if funcoes.escolha_usuario == 1:
                        cont_senha = n50 = n20 = n10 = n1 = saldo_usuario = tot_depositado = tot_saque = 0

                        senha = funcoes.verificar_num('\033[mBem vindo! Digite a senha do cartão [1000]:\033[92m ', sem_num_min=True, forcar_valor_int=True)
                        while senha != 1000:
                            cont_senha += 1
                            if cont_senha == 1:
                                senha = funcoes.verificar_num('\033[91mSenha inválida! (1 de 3 tentativas)\033[m Digite a senha do cartão:\033[92m ', sem_num_min=True, forcar_valor_int=True)
                            elif cont_senha == 2:
                                senha = funcoes.verificar_num('\033[91mSenha inválida! (2 de 3 tentativas)\033[m Digite a senha do cartão:\033[92m ', sem_num_min=True, forcar_valor_int=True)
                            elif cont_senha == 3:
                                senha = funcoes.verificar_num('\033[91mSenha inválida! (3 de 3 tentativas)\033[m Digite a senha do cartão:\033[92m ', sem_num_min=True, forcar_valor_int=True)
                            else:
                                print('\033[91mTentativas esgotadas!\033[m aguarde 10 segundos e tente novamente.')
                                sleep(10)
                                senha = funcoes.verificar_num('Bem vindo! Digite a senha do cartão:\033[92m ', sem_num_min=True ,forcar_valor_int=True)
                        print('\033[94mAcesso liberado!\033[m')

                        while True:
                            funcoes.menu('Saque', 'Depósito', 'Saldo', 'Sair')

                            funcoes.escolha_user('\nQual sua operação?', 4)
                            funcoes.linha('roxo', '10')

                            if funcoes.escolha_usuario == 1:
                                saque = funcoes.verificar_num('\033[mDigite o valor que deseja sacar: R$\033[92m ', forcar_valor_int=True)
                                if saldo_usuario < saque:
                                        print('\033[91mSaldo insuficiente!\033[m')
                                        sleep(0.6)
                                else:
                                    tot_saque += saque
                                    saldo_usuario -= saque
                                    while True:
                                            if saque >= 50:
                                                saque -= 50
                                                n50 += 1
                                            else:
                                                if saque >= 20:
                                                    saque -= 20
                                                    n20 += 1
                                                else:
                                                    if saque >= 10:
                                                        saque -= 10
                                                        n10 += 1
                                                    else:
                                                        if saque >= 1:
                                                            saque -= 1
                                                            n1 += 1
                                            if saque == 0:
                                                print('Contando notas...')
                                                sleep(0.9)
                                                if n50 > 0:
                                                    if n50 > 1:
                                                        print(f'\033[mVocê sacou {n50} notas de R$ \033[94m50\033[m')
                                                    else:
                                                        print(f'\033[mVocê sacou 1 nota de R$ \033[94m50\033[m')
                                                if n20 > 0:
                                                    if n20 > 1:
                                                        print(f'\033[mVocê sacou {n20} notas de R$ \033[94m20\033[m')
                                                    else:
                                                        print(f'\033[mVocê sacou 1 nota de R$ \033[94m20\033[m')
                                                if n10 > 0:
                                                    if n10 > 1:
                                                        print(f'\033[mVocê sacou {n10} notas de R$ \033[94m10\033[m')
                                                    else:
                                                        print(f'\033[mVocê sacou 1 nota de R$ \033[94m10\033[m')
                                                if n1 > 0:
                                                    if n1 > 1:
                                                        print(f'\033[mVocê sacou {n1} moedas de R$ \033[94m1\033[m')
                                                    else:
                                                        print(f'\033[mVocê sacou 1 moeda de R$ \033[94m1\033[m')
                                                funcoes.linha('roxo', '16')
                                                sleep(0.6)
                                                break

                            elif funcoes.escolha_usuario == 2:
                                deposito = funcoes.verificar_num('\033[mQuanto deseja depositar? R$\033[92m ')
                                print(f'\033[mVocê tinha um total de R$ {saldo_usuario} e adicionou R$ \033[94m{deposito}\033[m')
                                saldo_usuario += deposito
                                tot_depositado += deposito
                                funcoes.linha('roxo', '16')
                                sleep(0.6)

                            elif funcoes.escolha_usuario == 3:
                                print(f'\033[mSeu saldo é de R$ \033[94m{saldo_usuario}\033[m')
                                funcoes.linha('roxo', '16')
                                sleep(0.6)
                                
                            else:
                                sleep(0.6)
                                break

                        print(f'Você depositou R$ \033[94m{tot_depositado}\033[m.')
                        print(f'Seu saldo está em R$ \033[94m{saldo_usuario}\033[m')
                        print(f'Você sacou R$ \033[94m{tot_saque}\033[m')
                        print('\033[3mObrigado por utilizar o caixa eletrônico!💳 \033[94mVolte sempre!\033[m')
                        funcoes.linha('azul')

                    else:
                        funcoes.sair_secao('caixa eletrônico', 'amarelo')
                        break

    elif funcoes.escolha_usuario == 8:  # SEÇÃO DE CONVERÇÃO
        funcoes.titulo('Converção', 'SEÇÃO DE CONVERÇÃO', 'roxo')

        while True:
            funcoes.menu('Real', 'Dolar', 'Celsius', 'Fahrenheit', 'Kelvin', 'Sair da seção de converção')
                
            funcoes.escolha_user('Qual sua opção?', 6)

            if funcoes.escolha_usuario == 1:      # R$ -> US$
                valor_dolar = funcoes.verificar_num('\033[mQual o valor do dolar atualmente? US$\033[92m ')
                real = funcoes.verificar_num('\033[mQuantos reais você quer converter para dólar? R$\033[92m ')
                convertido = real / valor_dolar
                print(f'\n\033[mR$ {(real):.2f} convertido para dólar fica US$ \033[94m{(convertido):.2f}\033[m'.replace('.', ','))
                
                funcoes.continuar_def('Deseja continuar convertendo')
                    
                if funcoes.continuar == 'N':
                    funcoes.linha('amarelo')
                    break
                else:
                    funcoes.linha('roxo')
            
            elif funcoes.escolha_usuario == 2:    # US$ -> R$
                valor_dolar = funcoes.verificar_num('\n\033[mQual o valor do dolar atualmente? US$\033[92m ')
                dolar = funcoes.verificar_num('\033[mQuantos dolares você quer converter para real? US$\033[92m ')
                convertido = dolar * valor_dolar
                print(f'\n\033[mUS$ {(dolar):.2f} convertido para real fica R$ \033[94m{(convertido):.2f}\033[m'.replace('.', ','))
                
                funcoes.continuar_def('Deseja continuar convertendo')
                
                if funcoes.continuar == 'N':
                    funcoes.linha('amarelo')
                    break
                else:
                    funcoes.linha('roxo')

            elif funcoes.escolha_usuario == 3:    # Celcius
                funcoes.linha('azul', '50')
                while True:
                    funcoes.menu('Celsius -> Fahrenheit', 'Celsius -> Kelvin', 'Sair de seção de Celsius')

                    funcoes.escolha_user('Qual sua opção?', 3)

                    if funcoes.escolha_usuario == 1:
                        celsius = funcoes.verificar_num('\n\033[mQual a temperatura em °C\033[92m ')
                        convercao = (9 * celsius) / 5 + 32
                        print(f'\n\033[mA temperatura de {celsius}°C convertida para Fahrenheit é \033[94m{convercao}°F\033[m')

                        funcoes.continuar_def('Deseja continuar convertendo graus Celsius')
                        
                        if funcoes.continuar == 'N':
                            funcoes.linha('roxo')
                            break
                        else:
                            funcoes.linha('azul')

                    elif funcoes.escolha_usuario == 2:
                        celsius = funcoes.verificar_num('\n\033[mQual a temperatura em °C\033[92m ')
                        convercao = 273.15 + celsius
                        print(f'\n\033[mA temperatura de {celsius}°C convertida para Kelvin é \033[94m{convercao}°K\033[m')
                    
                        funcoes.continuar_def('Deseja continuar convertendo graus Celsius')
                        
                        if funcoes.continuar == 'N':
                            funcoes.linha('roxo')
                            break
                        else:
                            funcoes.linha('azul')

                    else:
                        funcoes.sair_secao('graus celcius', 'roxo')
                        break

            elif funcoes.escolha_usuario == 4:    # Fahrenheit
                print('\033[94m~\033[m'*50)
                while True:
                    funcoes.menu('Fahrenheit -> Celsius', 'Fahrenheit -> Kelvin', 'Sair da seção de Fahrenheit')

                    funcoes.escolha_user('Qual sua opção?', 3)

                    if funcoes.escolha_usuario == 1:
                        fahrenheit = funcoes.verificar_num('\033[mQual a temperatura em °F\033[92m ')
                        convercao = (fahrenheit - 32) / 1.8
                        print(f'\033[mA temperatura de {fahrenheit}°F convetida para Celsius fica \033[94m{(convercao):.1f}°C\033[m')

                        funcoes.continuar_def('Deseja continuar convertendo graus Fahrenheit')
                        
                        if funcoes.continuar == 'N':
                            funcoes.linha('roxo')
                            break
                        else:
                            funcoes.linha('azul')

                    elif funcoes.escolha_usuario == 2:
                        fahrenheit = funcoes.verificar_num('\033[mQual a temperatura em °F\033[92m ')
                        convercao = (fahrenheit - 32) * 5/9 + 273
                        print(f'\033[mA temperatura de {fahrenheit}°F convetida para Kelvin fica \033[94m{(convercao):.1f}°K\033[m')

                        funcoes.continuar_def('Deseja continuar convertendo graus Fahrenheit')
                        
                        if funcoes.continuar == 'N':
                            funcoes.linha('roxo')
                            break
                        else:
                            funcoes.linha('azul')

                    else:
                        funcoes.sair_secao('graus Fahrenheit', 'roxo')
                        break

            elif funcoes.escolha_usuario == 5:    # Kelvin
                print('\033[94m~\033[m'*50)
                while True:
                    funcoes.menu('Kelvin -> Celsius', 'Kelvin -> Fahrenheit', 'Sair da seção de Kelvin')

                    funcoes.escolha_user('Qual sua opção?', 3)

                    if funcoes.escolha_usuario == 1:
                        kelvin = funcoes.verificar_num('\033[mQual a temperatura em °K\033[92m ')
                        convercao = kelvin - 273
                        print(f'\033[mA temperatura de {kelvin}°K convetida para Celsius fica \033[94m{(convercao):.1f}°C\033[m')

                        funcoes.continuar_def('Deseja continuar convertendo graus Kelvin')
                        
                        if funcoes.continuar == 'N':
                            funcoes.linha('roxo')
                            break
                        else:
                            funcoes.linha('azul')

                    elif funcoes.escolha_usuario == 2:
                        kelvin = funcoes.verificar_num('\033[mQual a temperatura em °K\033[92m ')
                        convercao = (kelvin - 273) * 1.8 + 32
                        print(f'\033[mA temperatura de {kelvin}°K convetida para Fahrenheit fica \033[94m{(convercao):.1f}°F\033[m')

                        funcoes.continuar_def('Deseja continuar convertendo graus Kelvin')
                        
                        if funcoes.continuar == 'N':
                            funcoes.linha('roxo')
                            break
                        else:
                            funcoes.linha('azul')

                    else:
                        funcoes.sair_secao('graus Kelvin', 'roxo')
                        break
            
            else:
                funcoes.sair_secao('converção', 'amarelo')
                break

    elif funcoes.escolha_usuario == 9:  # SEÇÃO DE DESCONTO
        funcoes.titulo('Desconto', 'SEÇÃO DE DESCONTO', 'roxo')

        while True:
            funcoes.menu('Iniciar programa', 'Sair da seção de desconto')

            funcoes.escolha_user('Qual sua opção?', 2)

            if funcoes.escolha_usuario == 1:
                while True:
                    usuario_porcentagem = funcoes.verificar_num('\n\033[mQual a porcentagem do desconto?\033[92m ')
                    usuario_valor = funcoes.verificar_num('\033[mQual o valor do produto/indivíduo?\033[92m ')
                    if usuario_porcentagem >= 1:
                        usuario_porcentagem /= 100
                    desconto = usuario_porcentagem * usuario_valor

                    print(f'\n\033[mO valor {(usuario_valor):.2f} teve um desconto de {(desconto):.2f} e no total ficou \033[94m{(usuario_valor - desconto):.2f}\033[m no final'.replace('.', ','))

                    funcoes.continuar_def('Deseja continuar')
                        
                    if funcoes.continuar == 'N':
                        break
                    else:
                        funcoes.linha('azul')

            funcoes.sair_secao('desconto', 'amarelo')
            break

    elif funcoes.escolha_usuario == 10: # SEÇÃO DE AUMENTO
        funcoes.titulo('Aumento', 'SEÇÃO DE AUMENTO', 'roxo')

        while True:
            funcoes.menu('Iniciar programa', 'Sair da seção de aumento')

            funcoes.escolha_user('Qual sua opção?', 2)

            if funcoes.escolha_usuario == 1:
                while True:
                    usuario_porcentagem = funcoes.verificar_num('\n\033[mQual a porcentagem do aumento?\033[92m ')
                    usuario_valor = funcoes.verificar_num('\033[mQual o valor do produto/indivíduo?\033[92m ')
                    if usuario_porcentagem >= 1:
                        usuario_porcentagem /= 100
                    desconto = usuario_porcentagem * usuario_valor

                    print(f'\n\033[mO valor de {(usuario_valor):.2f} teve um aumento de {(desconto)} e no total ficou \033[94m{(usuario_valor + desconto):.2f}\033[m'.replace('.', ','))

                    funcoes.continuar_def('Deseja continuar')
                        
                    if funcoes.continuar == 'N':
                        break
                    else:
                        funcoes.linha('azul')

            funcoes.sair_secao('aumento', 'amarelo')
            break

    elif funcoes.escolha_usuario == 11: # SEÇÃO DE JUROS
        funcoes.titulo('Juros', 'SEÇÃO DE JUROS', 'roxo')

        while True:
            funcoes.menu('Juros Simples', 'Juros Composto', 'Sair da seção de juros')

            funcoes.escolha_user('Qual sua opção?', 2)

            if funcoes.escolha_usuario == 1:      # Juros Simples
                funcoes.titulo('Juros Simples', 'SEÇÃO DE JUROS SIMPLES', 'azul')

                usuario_valor_total = funcoes.verificar_num('\n\033[mQual o preço total do seu produto? R$\033[92m ')
                usuario_parcelas = funcoes.verificar_num('\033[mVai parcelar em quantas vezes?\033[92m ', forcar_valor_int=True)
                usuario_juros = funcoes.verificar_num('\033[mQual a porcentagem de juros?\033[92m ')
                if usuario_juros >= 1:
                    usuario_juros /= 100
                parcelas = usuario_valor_total / usuario_parcelas
                juros = usuario_juros * usuario_valor_total

                print(f'\n\033[mSeu produto de R$ {(usuario_valor_total):.2f} foi parcelado em {usuario_parcelas} vezes. Logo, R$ {(parcelas):.2f} acompanhado de um juros de R$ {(juros):.2f}, que totaliza R$ {parcelas + juros} ao mês. No final, o produto custará um total de R$ \033[94m{(usuario_valor_total + (juros * usuario_parcelas)):.2f}\033[m')
                funcoes.linha('azul')

            elif funcoes.escolha_usuario == 2:    # Juros Composto
                funcoes.titulo('Juros Composto', 'SEÇÃO DE JUROS COMPOSTO', 'azul')

                produto = funcoes.verificar_num('\033[mPreço total do produto: R$ \033[92m ')
                parcelas_usuario = funcoes.verificar_num('\033[mIrá parcelar em quantas vezes?\033[92m ', forcar_valor_int=True)
                juros_usuario = funcoes.verificar_num('\033[mQual a porcentagem de juros?\033[92m ')
                if juros_usuario >= 1:
                    juros_usuario /= 100

                tot = produto * ((juros_usuario + 1)**parcelas_usuario)

                print('')
                for c in range(1, parcelas_usuario + 1):
                    juros = (produto * juros_usuario) + produto
                    produto += (produto * juros_usuario)
                    print(f'\033[3;94m{c}ª Parcela:\033[m R$ {(juros):.2f}')
                print('')

                print(f'No final seu produto custará R$ \033[94m{(tot):.2f}\033[m')
                funcoes.linha('azul', '50')

            else:
                funcoes.sair_secao('juros', 'amarelo')
                break

    elif funcoes.escolha_usuario == 12:
        funcoes.titulo('Sistema de ajuda', 'SEÇÃO DE SISTEMA DE AJUDA', 'roxo')

        while True:
            try:
                comando = str(input('\n\033[mCom qual Função/Biblioteca posso ajudar? [0 para interromper]\033[92m '))
                if comando == '0':
                    funcoes.sair_secao('sistema de ajuda', 'amarelo')
                    break
            except KeyboardInterrupt:
                funcoes.interromper()
            else:
                print()
                funcoes.linha('azul')
                print('\033[3m')
                help(comando)
                funcoes.linha('azul')

    else:
        sleep(0.7)
        print('\n\033[mObrigado por ultilizar este programa.\033[3;94m Volte Sempre!')
        print('https://github.com/pedrosinsenp\033[m')
        print('Para contato >> \033[3;94mpedrosinsenp@gmail.com\033[m')

        funcoes.tempo()

        try:
            urllib.request.urlopen('https://github.com/pedrosinsenp')
        except:
            print('Acessa lá meu github!')
        else:
            open('https://github.com/pedrosinsenp')
        break