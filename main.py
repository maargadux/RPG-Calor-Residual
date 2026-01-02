from utils import escrever
from historia import capitulo_1
from historia import capitulo_2
from historia import capitulo_3
from historia import capitulo_4
from save_system import salvar_jogo, carregar_jogo
import time
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

jogador = {
    "nome": "",
    "energia": 2,
    "fome": 5,
    "inventario": [],
    "sanidade": 100,
    "viu_corpo": False,
    "atendeu_telefone": False
}


def menu():
    while True:
        print("\nSeja bem-vindo ao RPG: O sol mudou.")
        print("1 - Iniciar jogo")
        print("2 - Carregar jogo")
        print("3 - Instruções")
        print("4 - Créditos")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            escrever("Iniciando jogo...")
            time.sleep(1)

            jogador["nome"] = input("Qual é o seu nome? ")
            escrever(f"Olá, {jogador['nome']}...")
            escrever("Aqui começa sua aventura.")
            escrever("Não tenha medo.")
            escrever("Eles não existem.")
            time.sleep(1)
            clear()
            return {"capitulo": 1}

        elif escolha == "2":
            dados = carregar_jogo()
            if dados:
                jogador.update(dados["jogador"])
                escrever("Save carregado.")
                time.sleep(1)
                clear()
                return dados
            else:
                escrever("Nenhum save encontrado.")
                time.sleep(1)
                clear()

        elif escolha == "3":
            escrever("Instruções:")
            escrever("Tome suas decisões com calma.")
            time.sleep(0.45)
            escrever("Tome cuidado com sua sanidade.")
            time.sleep(0.45)
            escrever("Tome cuidado com as pessoas.")
            time.sleep(0.45)
            escrever("Tome cuidado com o sol.")
            time.sleep(0.45)
            escrever("Tome cuidado com os monstros.")
            time.sleep(0.45)
            input("Pressione Enter para voltar.")
            clear()

        elif escolha == "4":
            print("Desenvolvido por: Vdot")
            input("Pressione Enter para voltar.")
            clear()

        elif escolha == "5":
            exit()

        else:
            print("Opção inválida.")

# 🔽 EXECUÇÃO DO JOGO
estado = menu()               # CHAMA O MENU UMA VEZ
capitulo_atual = estado.get("capitulo", 1)

while True:
    if capitulo_atual == 1:
        capitulo_atual = capitulo_1(jogador)

    elif capitulo_atual == 2:
        capitulo_atual = capitulo_2(jogador)

    elif capitulo_atual == 3:
        capitulo_atual = capitulo_3(jogador)
        
    elif capitulo_atual == 4:
        capitulo_atual = capitulo_4(jogador)

    else:
        escrever("Fim da história.")
        break

    salvar_jogo({
        "capitulo": capitulo_atual,
        "jogador": jogador
    })