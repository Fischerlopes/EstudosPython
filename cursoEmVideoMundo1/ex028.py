#jogo de advinhação
import random
a = random.randint(1,4)

b = int(input('Tente adivinhar o número: '))

print('Você acertou' if a == b else 'Você errou')