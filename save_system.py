import json
import os

SAVE_FILE = "save.json"

def salvar_jogo(dados):
    with open(SAVE_FILE, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def carregar_jogo():
    if not os.path.exists(SAVE_FILE):
        return None

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return None  # save vazio

            return json.loads(conteudo)

    except json.JSONDecodeError:
        return None
