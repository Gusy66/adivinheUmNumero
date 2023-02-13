import random

def main():
    print("Bem-vindo ao jogo de adivinhação de número!")
    print("Tente adivinhar o número escolhido pelo computador entre 1 e 100.")
    number = random.randint(1, 100)
    guess = int(input("Digite sua primeira tentativa: "))
    tries = 1
    while guess != number:
        if guess < number:
            print("O número é mais alto.")
        else:
            print("O número é mais baixo.")
        guess = int(input("Digite sua próxima tentativa: "))
        tries += 1
    print(f"Parabéns, você adivinhou o número em {tries} tentativas!")

if __name__ == "__main__":
    main()
