def mostrar_hud(jogador):
    sanidade = jogador.get("sanidade", 0)
    energia = jogador.get("energia", 0)
    fome = jogador.get("fome", 0)

    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🧠 Sanidade: {sanidade} | ⚡ Energia: {energia} | 🍞 Fome: {fome}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
