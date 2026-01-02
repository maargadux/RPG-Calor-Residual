from utils import escrever
from hud import mostrar_hud
from save_system import salvar_jogo
import time
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def capitulo_1(jogador):
    escrever("📖 CAPÍTULO 1 — Calor Residual")

    escrever("\nVocê acorda como em qualquer outro dia.")
    escrever("O teto é o mesmo.")
    escrever("O silêncio também.")
    
    escrever("\nVocê vai ao banheiro.")
    escrever("Escova os dentes.")
    escrever("Evita se olhar por tempo demais no espelho.")

    escrever("\nO café da manhã é simples.")
    escrever("Pão, ovo e café.")
    escrever("O gosto não chama atenção.")
    escrever("Nada chama atenção.")

    escrever("\nVocê sai de casa para trabalhar.")
    escrever("O sol já está alto.")
    escrever("Quente demais para a hora.")

    # ───────────────── TRABALHO ─────────────────

    escrever("\nO expediente passa devagar.")
    escrever("Ar-condicionado fraco.")
    escrever("As pessoas falam baixo.")

    escrever("\nVocê começa a ouvir alguns murmurinhos.")
    escrever("Comentários soltos.")
    escrever("Algo sobre o sol.")
    escrever("Algo sobre o calor.")

    escrever("\nVocê ignora.")
    escrever("Continua trabalhando.")

    escrever("\nFaltam poucos minutos para as 20h.")
    escrever("Pedro chega perto da sua mesa.")

    escrever('\n"Você tem ouvido as notícias?"', velocidade=0.04)
    
    escrever('\nVocê responde que não.', velocidade=0.04)

    escrever('\nPedro parece desconfortável.', velocidade=0.04)
    escrever('"Está quente demais."', velocidade=0.04)
    escrever('"Não é normal."', velocidade=0.04)

    escrever('\nEle fala de pessoas passando mal.', velocidade=0.04)
    escrever('De gente que não aguenta ficar no sol.', velocidade=0.04)
    escrever('De algo errado.', velocidade=0.04)

    escrever("\nVocê não leva a sério.")
    escrever("Já está na hora de ir embora.")
    escrever("E o sol já se foi.")

    # ───────────────── VOLTA PARA CASA ─────────────────

    escrever("\nVocê sai do trabalho.")
    escrever("A rua parece normal.")
    escrever("Normal demais.")

    escrever("\nNo ponto de ônibus, você sente algo.")
    escrever("Não é um som.")
    escrever("Não é um movimento.")

    escrever("\nÉ a sensação de estar sendo observado.")

    escrever("\nEm algum ponto da rua.")
    escrever("Em alguma casa.")
    escrever("Você não sabe.")

    escrever("\nMas sente os olhos.")
    escrever("Quentes.")
    escrever("Atentos.")
    escrever("Famintos.")

    escrever("\nO ônibus chega.")
    escrever("Você entra sem olhar para trás.")

    # ───────────────── CASA ─────────────────

    escrever("\nA porta da sua casa se fecha atrás de você.")
    escrever("O ar lá dentro está abafado.")
    escrever("Preso.")

    escrever("\nVocê tem certeza de uma coisa:")
    escrever("Hoje, não deve abrir as janelas.")

    escrever("\nO telefone toca.")

    escrever("\nEle toca de novo.")

    escrever("\nE continua tocando.")

    escrever("\nO telefone continua tocando.")
    escrever("O som parece mais alto agora.")
    escrever("Mais próximo.")
    
    time.sleep(1)
    clear()
    
    while True:
        mostrar_hud(jogador)
        escrever("\nO que você faz?")
        print("\n1 - Atender o telefone")
        print("2 - Ignorar a ligação")
        print("3 - Descer e verificar a casa")

        escolha = input("Escolha: ")
        clear()
        # ───────────── OPÇÃO 1 ─────────────
        if escolha == "1":
            jogador["energia"] -= 1

            escrever("\nSua mão treme quando toca no telefone.")
            escrever("O plástico está quente.")
            escrever("Quente demais.")

            escrever("\nVocê encosta o aparelho no ouvido.")

            time.sleep(1)

            escrever("\nNada.")
            escrever("Por alguns segundos… nada.")

            time.sleep(1.2)

            escrever("\nEntão você ouve algo.")
            escrever("No começo, parece estática.")
            
            time.sleep(0.6)
            
            escrever("Depois, respiração.")
            escrever("Muito próxima.")
            escrever("Muito errada.")
            
            time.sleep(1)

            escrever("\nComo se alguém estivesse tentando não chorar.")
            escrever("Como se fosse um animal")
            escrever("Algo que não devia existir.")
            escrever("Algo que não devia estar ali.")

            time.sleep(1)

            escrever("\nA respiração falha.")
            escrever("Para.")
            escrever("Volta.")

            escrever(f'\n"{jogador["nome"]}."', velocidade=0.05)
            time.sleep(0.6)

            escrever(f'"Você não devia ter atendido."', velocidade=0.05)

            time.sleep(0.8)

            escrever("\nO arrepio sobe pelos seus braços.")
            escrever("Seu estômago afunda.")
            escrever("Seu corpo entende o perigo antes da sua mente.")

            escrever("\nA voz parece sorrir.")
            escrever("Mesmo sem som.")

            escrever('\n"Está quente aí também."', velocidade=0.05)

            time.sleep(0.8)

            escrever("\nUm clique seco.")
            escrever("A ligação cai.")

            escrever("\nO telefone fica mudo.")
            escrever("Mas a sensação não vai embora.")
            input("Pressione Enter para continuar...")

        # ───────────── OPÇÃO 2 ─────────────
        elif escolha == "2":
            escrever("\nVocê decide não atender.")
            escrever("Não hoje.")

            escrever("\nO telefone toca de novo.")
            escrever("E de novo.")
            escrever("Cada toque parece mais longo.")

            time.sleep(1)

            escrever("\nSeu coração acelera.")
            escrever("Você começa a contar os segundos entre os toques.")
            escrever("Sem perceber.")

            escrever("\nO som finalmente para.")

            time.sleep(1)

            escrever("\nO silêncio é absoluto.")
            escrever("Pesado.")
            escrever("Como se algo estivesse esperando.")

            escrever("\nVocê percebe que está prendendo a respiração.")
            escrever("E não lembra quando começou.")
            input("Pressione Enter para continuar...")

        # ───────────── OPÇÃO 3 ─────────────
        elif escolha == "3":
            if jogador["energia"] <= 0:
                escrever("\nSeu corpo não responde.")
                escrever("Você está cansado demais.")
                continue

            jogador["energia"] -= 1

            escrever("\nVocê sai do quarto.")
            escrever("O corredor parece mais longo.")

            time.sleep(0.8)

            escrever("\nCada passo ecoa.")
            escrever("Mesmo com o piso velho.")

            escrever("\nVocê desce para a sala.")

            time.sleep(1)

            escrever("\nO ambiente está escuro.")
            escrever("Mas você sente.")
            escrever("Alguém está ali.")

            escrever("\nNão vê.")
            escrever("Não ouve.")
            escrever("Mas sente.")

            escrever("\nComo se olhos percorressem suas costas.")
            escrever("Observando.")
            escrever("Avaliando.")
            escrever("O mesmo sentimento que você sentiu no ponto de ônibus.")

            time.sleep(1)

            escrever("\nVocê se vira rápido.")
            escrever("Nada.")

            escrever("\nMas a sensação continua.")
            escrever("Grudada.")

            time.sleep(1)

            escrever("\nVocê sobe de volta para o quarto.")
            escrever("Sem olhar para os lados.")

            time.sleep(0.8)

            escrever("\nO telefone não está mais tocando.")

            escrever("\nO quarto parece menor agora.")
  
        salvar_jogo({
    "capitulo": 1,
    "jogador": jogador
            })

        escrever("\n[Jogo salvo automaticamente]")
        escrever("\n[FIM DO CAPÍTULO 1]")
        input("Pressione Enter para continuar...")
        time.sleep(1)
        clear()
        return 2

        ##FIM DO CAPITULO 1 
        
        #INICIO CAPITULO 2

def capitulo_2(jogador):
    escrever("📖 CAPÍTULO 2 — O Sol Não Avisou")

    escrever("\nVocê acorda com o corpo pesado.")
    escrever("Dormiu mal.")
    escrever("Sonhou pior.")

    escrever("\nO dia já está claro demais.")
    escrever("O sol atravessa a cortina.")
    escrever("Quente.")
    escrever("Insistente.")

    escrever("\nAntes de ir ao trabalho, você decide passar no mercado.")
    escrever("Faltam algumas coisas em casa.")

    # ───────────── RUA ─────────────

    escrever("\nVocê anda pelas ruas.")
    escrever("Não vê ninguém.")
    escrever("Se sente sozinho.")

    escrever("\nNenhum carro.")
    escrever("Nenhuma conversa.")
    escrever("Nenhum som além dos seus passos.")

    escrever("\nO sol está quente.")
    escrever("Ainda suportável.")
    escrever("Mas você sua demais.")
    
    escrever("\nO suor escorre pelo rosto.")
    escrever("Pela nuca.")
    escrever("Pelas costas.")

    # ───────────── MERCADO ─────────────

    escrever("\nO mercado da esquina ainda está aberto.")
    escrever("As luzes piscam levemente.")

    escrever("\nLá dentro, o ar é mais fresco.")
    escrever("Quase um alívio.")

    escrever("\nVocê pega uma bebida gelada.")
    escrever("As mãos tremem um pouco ao tocar na garrafa.")

    escrever("\nNo caixa, a atendente te encara.")
    escrever("Por tempo demais.")

    escrever('\n"Você é louco?"', velocidade=0.05)
    escrever('"Andando assim."', velocidade=0.05)
    escrever('"Sem proteção."', velocidade=0.05)

    escrever("\nVocê franze a testa.")
    escrever("Não entende.")

    escrever("\nEla suspira.")
    escrever("E puxa algo debaixo do balcão.")

    escrever("\nUma sombrinha.")
    escrever("Simples.")
    escrever("Velha.")
    escrever("Mas da para o gasto.")

    escrever('\n"Leva."', velocidade=0.05)
    escrever('"Depois do jornal de ontem à noite..."', velocidade=0.05)
    escrever('"Coisas estranhas estão acontecendo com o sol."', velocidade=0.05)

    escrever('\n"Não é seguro ficar na rua."', velocidade=0.05)
    escrever('"O governo pediu pra gente ficar em casa."', velocidade=0.05)

    escrever('\n"Se faltar suplemento..."', velocidade=0.05)
    escrever('"Liga pra esse número."', velocidade=0.05)

    escrever("\nEla anota em um papel e empurra pra você.")
    escrever("808-4950")

    escrever('\n"E não ignora isso."', velocidade=0.05)

    escrever("\nVocê paga.")
    escrever("Agradece.")
    escrever("Sai.")

    # ───────────── VOLTA PARA CASA ─────────────

    escrever("\nNo caminho de volta, algo chama sua atenção.")
    escrever("No fundo da rua.")

    escrever("\nUm corpo.")
    escrever("Caído.")

    escrever("\nVocê se aproxima com cuidado.")

    escrever("\nA pele está seca.")
    escrever("Repuxada.")
    escrever("Colada nos ossos.")

    escrever("\nNão há sangue.")
    escrever("Não há ferimentos.")

    escrever("\nSó a sensação de que...")
    escrever("Algo foi drenado.")

    escrever("\nO sol bate direto no corpo.")
    escrever("Sem piedade.")

    escrever("\nO que você faz?")

    while True:
        print("\n1 - Se aproximar mais")
        print("2 - Se afastar rapidamente")
        print("3 - Cobrir o corpo com a sombrinha")

        escolha = input("Escolha: ")

        if escolha == "1":
            escrever("\nVocê dá mais um passo.")
            escrever("E mais outro.")

            time.sleep(1)

            escrever("\nO calor fica mais intenso.")
            escrever("Sua visão embaça por um segundo.")

            time.sleep(1)

            escrever("\nVocê sente tontura.")
            escrever("Medo.")
            escrever("Um aviso silencioso.")

            escrever("\nVocê recua instintivamente.")

            break

        elif escolha == "2":
            escrever("\nVocê se afasta.")
            escrever("Rápido.")

            time.sleep(1)

            escrever("\nSeu coração dispara.")
            escrever("Você não olha para trás.")

            break

        elif escolha == "3":
            escrever("\nVocê abre a sombrinha.")
            escrever("A sombra cobre o corpo.")

            time.sleep(1)

            escrever("\nPor um instante...")
            escrever("Você tem a estranha sensação")
            escrever("De que algo relaxa.")

            time.sleep(1)
            escrever("\nA sensação passa.")
            escrever("Mas a imagem fica.")
            break

        else:
            print("Escolha inválida.")

    escrever("\nVocê volta para casa.")
    escrever("Com mais perguntas do que respostas.")

    escrever("\nO telefone fixo está silencioso.")
    escrever("Por enquanto.")

    escrever("\nMas o sol...")
    escrever("Ainda está lá.")
    escrever("Com a coloração diferente.")
    escrever("Estranha.")
    escrever("Mas o sol ainda está lá.")

    escrever("\nVocê fecha a porta atrás de si.")
    escrever("Tranca duas vezes.")
    escrever("Mesmo sabendo que isso não significa muita coisa.")

    escrever("\nA casa está silenciosa.")
    escrever("Mas não confortável.")

    escrever("\nA sombrinha está encostada perto da porta.")
    escrever("Pingando suor.")
    escrever("Como se estivesse viva.")

    escrever("\nVocê sente sede.")
    escrever("A bebida gelada ainda está na sacola.")

    escrever("\nO telefone fixo está ali.")
    escrever("Quieto.")
    escrever("Observando.")

    escrever("\nO que você faz?")
    
    while True:
        print("\n1 - Beber a bebida gelada")
        print("2 - Ligar a TV")
        print("3 - Olhar pela fresta da janela")
        print("4 - Ligar para o número do papel (808-4950)")

        escolha = input("Escolha: ")

        # ───────────── OPÇÃO 1 ─────────────
        if escolha == "1":
            jogador["fome"] = max(0, jogador["fome"] - 1)

            escrever("\nVocê abre a garrafa.")
            escrever("O líquido desce rápido.")
            escrever("Frio.")
            escrever("Bom demais.")

            escrever("\nPor um momento...")
            escrever("O calor parece diminuir.")

            break
        # ───────────── OPÇÃO 2 ─────────────
        elif escolha == "2":
            escrever("\nVocê liga a TV.")

            escrever("\nA imagem falha.")
            escrever("Chiado.")
            escrever("Depois... um jornal.")

            escrever('\n"Autoridades reforçam o pedido para que a população..."', velocidade=0.04)
            escrever('"Evite exposição ao sol."', velocidade=0.04)
            escrever('"Casos de desidratação extrema continuam aumentando."', velocidade=0.04)

            escrever("\nA imagem trava.")
            escrever("Por um frame, algo aparece atrás do apresentador.")
            escrever("Algo alto.")
            escrever("Magro.")
            escrever("Parado.")

            escrever("\nA TV desliga sozinha.")

            jogador["sanidade"] -= 5
            break
        # ───────────── OPÇÃO 3 ─────────────
        elif escolha == "3":
            escrever("\nVocê se aproxima da janela.")
            escrever("Devagar.")

            escrever("\nAfasta a cortina só o suficiente.")

            escrever("\nA rua está vazia.")
            escrever("Mas o corpo não está mais lá.")

            escrever("\nNo lugar...")
            escrever("Marcas no chão.")
            escrever("Como se algo tivesse sido arrastado.")

            jogador["viu_corpo"] = True
            jogador["sanidade"] -= 3

            break
        # ───────────── OPÇÃO 4 ─────────────
        elif escolha == "4":
            escrever("\nVocê segura o papel.")
            escrever("O número está borrado de suor.")

            escrever("\nDisca.")

            escrever("\nChama.")
            escrever("Chama de novo.")

            escrever("\nAlguém atende.")

            escrever('\n"Central de Suplementos."', velocidade=0.05)
            escrever('"Fique dentro de casa."', velocidade=0.05)
            escrever('"O sol não é seguro."', velocidade=0.05)

            escrever("\nAntes que você fale qualquer coisa...")
            escrever('\n"A gente já sabe onde você mora."', velocidade=0.05)

            jogador["atendeu_telefone"] = True
            jogador["sanidade"] -= 10

            break

        else:
            print("Escolha inválida.")
            continue

    escrever("\nA ligação cai.")
    escrever("O silêncio volta.")

    escrever("\nDo lado de fora...")
    escrever("Algo passa em frente à sua casa.")

    escrever("\nVocê não vê.")
    escrever("Mas sente a sombra atravessar a parede.")

    escrever("\nO sol ainda está lá.")
    escrever("E parece mais próximo.")

    salvar_jogo({
        "capitulo": 2,
        "jogador": jogador
    })

    escrever("\n[Jogo salvo automaticamente]")
    escrever("\n[FIM DO CAPÍTULO 2]")
    input("Pressione Enter para continuar...")
    time.sleep(1)
    clear()
    return 3

def capitulo_3(jogador):
    escrever("📖 CAPÍTULO 3 — A Sombra Também Queima")

    escrever("\nO calor não diminuiu durante a noite.")
    escrever("Ele apenas mudou de lugar.")
    
    escrever("\nO ar dentro da casa está pesado, parado, como se não tivesse permissão para circular.")
    escrever("Você acorda suando, mesmo sem se mexer.")
    escrever("A cama está quente.")
    
    escrever("\nO silêncio não traz conforto.")
    escrever("— ele observa.")

    escrever("\nA TV liga sozinha.")
    escrever("O volume está baixo.")
    escrever("Quase um sussurro.")
    
    escrever("\nMesmo assim, você entende cada palavra.")

    escrever("\nO símbolo do governo ocupa a tela.")
    escrever("Distorcido.")
    escrever("Pulsando levemente, como se fosse algo vivo.")

    escrever('\n"Esta é uma transmissão de emergência."')
    escrever('"A situação atual exige calma."')

    escrever("\nA imagem corta.")
    
    escrever("\nAgora são gravações de celulares.")
    escrever("Câmeras de segurança.")
    escrever("Fragmentos de um mundo quebrando.")
    
    escrever("\nOs ultimos fragmentos da humanidade.")
    
    escrever("\nPessoas brigam nas ruas.")
    escrever("Gritos sem motivo claro.")
    escrever("Alguém corre.")
    
    escrever("\nOutro cai.")
    escrever("Ninguém ajuda.")
    
    escrever("\nUma loja é arrombada.")
    escrever("Nao por comida.")
    escrever("Garrafas vazias são disputadas como ouro.")
    
    escrever("\nA transmissao retorna ao estudio.")
    escrever("O apresentador está mais pálido agora.")
    escrever("Sua voz falha por um instante.")
    
    escrever("\n“Casos de violência estão aumentando.”")
    escrever("“Conflitos não provocados.”")
    escrever("“A população está cada vez mais desesperada.”")
    
    escrever("\nEles lutam por água, por comida, por qualquer coisa que possa salvar sua vida.")
    escrever("Ele engole seco.")
    
    escrever("\n“O governo reforça a recomendação.”")
    escrever("“Fique em casa.”")
    escrever("Evitem exposição direta ao sol")
    escrever("Evitem permanecer no escuro por longos períodos.")
    
    escrever("\nA imagem congela.")
    escrever("Uma mensagem aparece na tela.")
    while True:
        clear()
        mostrar_hud(jogador)
    
        escrever('\n"DESEJA SOLICITAR SUPLEMENTO AO GOVERNO PARA TENTAR SOBREVIVER?"')

        print("\n1 - Solicitar suplemento")
        print("2 - Não solicitar")
        print("3 - Desligar a TV")

        escolha = input("Escolha: ")

        if escolha == "1":
            jogador["sanidade"] -= 5
            jogador["suplemento"] = True

        elif escolha == "2":
            jogador["sanidade"] -= 3
            jogador["ficou_no_escuro"] = True

        elif escolha == "3":
            jogador["sanidade"] -= 2
            jogador["negacao"] = True

        else:
            escrever("Nenhuma resposta registrada.")

        # ───────── ESCOLHA CENTRAL ─────────
        escrever("\nDentro de casa, a sombra parece mais densa.")
        escrever("Errada.")

        while True:
            clear()
            mostrar_hud(jogador)

            print("\n1 - Permanecer no escuro")
            print("2 - Abrir a cortina")
            print("3 - Sair de casa rapidamente")

            escolha = input("Escolha: ")

            if escolha == "1":
                jogador["ficou_no_escuro"] = True
                jogador["sanidade"] -= 4
                break

            elif escolha == "2":
                jogador["sanidade"] -= 6
                break

            elif escolha == "3":
                jogador["energia"] -= 1
                jogador["sanidade"] -= 3
                break

            else:
                print("Escolha inválida.")

    # ───────── CONSEQUÊNCIA ─────────
        if jogador["sanidade"] <= 50:
            escrever("\nVocê sente que algo mudou.")
            escrever("Não no ambiente.")
            escrever("Em você.")

        salvar_jogo({
            "capitulo": 3,
            "jogador": jogador
        })

        escrever("\n[Jogo salvo automaticamente]")
        escrever("\n[FIM DO CAPÍTULO 3]")
        input("Pressione Enter para continuar...")
        time.sleep(1)
        clear()
        return 4
        
def capitulo_4(jogador):
    escrever("\n=== CAPÍTULO 4 — ISOLAMENTO ===\n")

    escrever("Os dias passam, mas o relógio parece quebrado.")
    escrever("O sol ainda nasce… mas ninguém mais sai para vê-lo.")
    escrever("As ruas estão silenciosas demais.")
    escrever("O rádio só repete avisos antigos.")
    escrever("A televisão transmite a mesma imagem há horas.")

    escrever("\nVocê está isolado dentro de casa.")
    escrever("O mundo lá fora parece ter acabado.")
    escrever("E o pior… é que sua mente começa a acompanhar esse fim.")

    escrever("\nSua sanidade atual é: " + str(jogador['sanidade']))

    mostrar_hud(jogador)
    
    escrever("\nO que você decide fazer?")
    escrever("1 - Manter a rotina (limpar a casa, organizar coisas)")
    escrever("2 - Ignorar tudo e dormir o máximo possível")
    escrever("3 - Ficar observando a janela")
    escrever("4 - Ligar a televisão novamente")

    escolha = input("> ")

    # CAMINHO 1 — ROTINA
    if escolha == "1":
        escrever("\nVocê decide manter uma rotina.")
        escrever("Arruma a casa. Organiza objetos.")
        escrever("Por alguns minutos, você quase esquece o caos.")
        escrever("Quase.")

        jogador["sanidade"] -= 5
        escrever("A rotina ajuda… mas o silêncio cobra seu preço.")
        return 4
    
    # CAMINHO 2 — DORMIR
    elif escolha == "2":
        escrever("\nVocê dorme.")
        escrever("E dorme.")
        escrever("E dorme novamente.")
        escrever("Os sonhos são confusos.")
        escrever("Você acorda cansado, mas o tempo passou mais rápido.")

        jogador["energia"] += 1
        jogador["sanidade"] -= 10
        escrever("Dormir ajudou o corpo, mas não a mente.")

    # CAMINHO 3 — JANELA
    elif escolha == "3":
        escrever("\nVocê observa a rua pela janela.")
        escrever("Um corpo está caído na calçada.")
        escrever("Ninguém se aproxima.")
        escrever("Ninguém ajuda.")
        escrever("O vento move algo que parece… um jornal antigo.")

        jogador["sanidade"] -= 15
        jogador["viu_corpo"] = True
        escrever("Você sente um aperto no peito.")
        escrever("Talvez o mundo realmente tenha acabado.")

    # CAMINHO 4 — TV
    elif escolha == "4":
        escrever("\nVocê liga a televisão.")
        escrever("Após alguns segundos de estática, uma transmissão surge.")

        escrever("\n\"ATENÇÃO.\"")
        escrever("\"As autoridades reforçam: permaneçam em casa.\"")
        escrever("\"Casos de violência, surtos e colapsos mentais aumentam.\"")
        escrever("\"Evitem contato humano.\"")
        escrever("\"Confiem apenas em comunicados oficiais.\"")

        jogador["sanidade"] -= 8
        escrever("A transmissão termina abruptamente.")

    else:
        escrever("\nVocê não consegue decidir.")
        escrever("O tempo passa mesmo assim.")
        jogador["sanidade"] -= 5

    # CONSEQUÊNCIA GLOBAL
    escrever("\nO isolamento começa a moldar quem você está se tornando.")
    escrever("Pensamentos estranhos surgem.")
    escrever("Você começa a falar sozinho sem perceber.")

    escrever("\nSanidade atual: " + str(jogador['sanidade']))

    # GANCHO PARA CAPÍTULO 5
    escrever("\nUm som quebra o silêncio.")
    escrever("Batidas na porta.")
    escrever("Três batidas.")
    escrever("Depois… silêncio.")
    
    salvar_jogo({
        "capitulo": 4,
        "jogador": jogador
    })

    escrever("\n[Jogo salvo automaticamente]")
    escrever("\n[FIM DO CAPÍTULO 4]")
    input("Pressione Enter para continuar...")
    time.sleep(1)

    #return 5

#def capitulo_5(jogador):