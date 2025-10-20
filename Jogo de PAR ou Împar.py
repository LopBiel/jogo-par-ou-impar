import os
from random import randint
from colorama import Fore, Style, init
from time import sleep

#! Fazer tratamento de erros caos o usuario usar letras em vez de numeros

# Inicializa o colorama
init(autoreset=True)

# Função de configuração de cores
def cores():
    return {
        "titulo": Fore.YELLOW + Style.BRIGHT,
        "borda": Fore.CYAN + Style.BRIGHT,
        "texto": Fore.WHITE,
        "erro": Fore.RED,
        "sucesso": Fore.GREEN,
        "neutro": Fore.MAGENTA,
        "carregando": Fore.BLUE,
        "valor": Fore.YELLOW,
    }

# Função para criar linhas (agora usa valores padrão)
def linha():
    print(Fore.CYAN + Style.BRIGHT + '-' * 40)

#  Função para limpar tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#  Função principal do jogo
def jogar():
    c = cores()
    vitorias = 0

    while True:
        limpar_tela()
        linha()
        print(c["titulo"] + "🎮 BEM-VINDO AO JOGO PAR OU ÍMPAR 🎲")
        linha()
        print(c["texto"] + f"Vitórias consecutivas: {c['sucesso']}{vitorias}\n")

        # Entrada do jogador (sem tratamento de erro)
        jogador = str(input(c["sucesso"] + "Digite um valor de 0 a 10: "))
        if jogador.isdigit():
            jogador = int(jogador)
            if jogador < 0 or jogador > 10:
                print(c["erro"] + "Número inválido! Digire números entre 0 e 10.")
                sleep(1.5)
                continue

        else:
            print(c["erro"] + " Número inválido! Tente novamente.")
            sleep(1.5)
            continue
        
        # Escolha do tipo
        tipo = " "
        while tipo not in "PI":
            tipo = input(c["neutro"] + "Você escolhe PAR ou ÍMPAR? [P/I] ").strip().upper()[0]

        # Efeito de carregamento
        print(c["carregando"] + "\nCalculando resultado", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            sleep(0.7)
        print()
        sleep(0.5)

        limpar_tela()

        # Computador e resultado
        computador = randint(0, 10)
        total = jogador + computador

        linha()
        print(
            c["texto"] + f"Você jogou {c['valor']}{jogador}{c['texto']} e o computador {c['valor']}{computador}{c['texto']}\n" +
            c["texto"] + f"Total = {c['borda']}{total}{c['texto']} -> " +
            (c["carregando"] + "PAR" if total % 2 == 0 else c["carregando"] + "IMPAR")
        )
        linha()
        sleep(1.5)

        # Verifica o vencedor
        if (tipo == "P" and total % 2 == 0) or (tipo == "I" and total % 2 == 1):
            print(c["sucesso"] + "✨ Você VENCEU! Parabéns!")
            vitorias += 1
        else:
            print(c["erro"] + "💀 Você PERDEU!")
            break

        print(c["valor"] + "\nAperte ENTER para jogar novamente...")
        input()

    # Fim do jogo
    sleep(1)
    limpar_tela()
    print(c["erro"] + Style.BRIGHT + "💀 GAME OVER!!! 💀")
    print(c["borda"] + f"Você venceu {c['valor']}{vitorias}{c['borda']} vezes consecutivas! 🏆\n")

    # Opção para tentar novamente
    while True:
        print(c["neutro"] + "Deseja tentar novamente?")
        print(c["valor"] + "[1] Sim, quero jogar de novo")
        print(c["borda"] + "[2] Não, quero sair")
        opcao = input(c["texto"] + "Escolha: ").strip()

        if opcao == "1":
            jogar()
            break
        elif opcao == "2":
            limpar_tela()
            print(c["sucesso"] + "👋 Obrigado por jogar! Até a próxima!")
            sleep(2)
            limpar_tela()
            exit()
        else:
            print(c["erro"] + "Opção inválida! Tente novamente.")
            sleep(1)
            limpar_tela()

# Inicia o jogo
jogar()