import time
def escrever(texto, velocidade=0.03):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(velocidade)
    print()
