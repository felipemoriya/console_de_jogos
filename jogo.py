def jogo_perguntas():
print("Bem-vindo ao jogo de perguntas e respostas!")
print("Responda corretamente para ganhar pontos.")
print("-----------------------------------------\n")
perguntas = [
"Qual é a capital da França?",
"Quanto é 5 + 3?",
"Quem escreveu 'Dom Quixote'?",
"Qual é o planeta mais próximo do Sol?"
]
respostas = [
"Paris",
"8",
"Miguel de Cervantes",
"Mercúrio"
]
pontos = 0
max_tentativas = 3
pergunta_atual = 0
while pergunta_atual < len(perguntas):
tentativas = 0
print(f"Pergunta {pergunta_atual + 1}: {perguntas[pergunta_atual]}")
while tentativas < max_tentativas:
resposta_jogador = input(f"Tentativa {tentativas + 1}/{max_tentativas} - Sua resposta: ").strip()
if resposta_jogador.lower() == respostas[pergunta_atual].lower():
print("Resposta correta!\n")
pontos += 1
break
else:
tentativas += 1
if tentativas < max_tentativas:
print("Resposta errada! Tente novamente.\n")
else:
print(f"Resposta errada! A resposta correta era: {respostas[pergunta_atual]}\n")
if tentativas == max_tentativas:
resposta_errada = input("Você quer tentar de novo a pergunta anterior? (s/n): ").strip().lower()
if resposta_errada == 's' and pergunta_atual > 0:
pergunta_atual -= 1
print("Você voltou para a pergunta anterior.")
else:
pergunta_atual += 1
else:
pergunta_atual += 1
print("-----------------------------------------")
print(f"Fim do jogo! Você acertou {pontos} de {len(perguntas)} perguntas.")
if pontos == len(perguntas):
print("Parabéns! Você acertou todas as perguntas!")
elif pontos > len(perguntas) / 2:
print("Bom trabalho! Você foi bem.")
else:
print("Continue praticando e tente novamente!")


def adivinhe_o_numero():
print("Você escolheu Adivinhe o Número!")
import random
numero = random.randint(1, 10)
while True:
palpite = int(input("Tente adivinhar o número (entre 1 e 10): "))
if palpite == numero:
print("Parabéns! Você acertou!")
break
elif palpite < numero:
print("Tente um número maior.")
else:
print("Tente um número menor.")

import random
def jogar_jokenpo():
opcoes = ["pedra", "papel", "tesoura"]
while True:
jogada_jogador = input("Faça sua jogada (pedra, papel ou tesoura): ").lower()
while jogada_jogador not in opcoes:
jogada_jogador = input("Jogada inválida! Tente novamente (pedra, papel ou tesoura): ").lower()
jogada_computador = random.choice(opcoes)
print(f"Computador jogou: {jogada_computador}")
if jogada_jogador == jogada_computador:
print("Empate!")
elif (jogada_jogador == "pedra" and jogada_computador == "tesoura") or \
(jogada_jogador == "papel" and jogada_computador == "pedra") or \
(jogada_jogador == "tesoura" and jogada_computador == "papel"):
print("Você venceu!")
else:
print("Você perdeu!")
if input("Deseja jogar novamente? (sim/nao): ").lower() != 'sim':
break

iniciar = True

def console_de_jogos():
while inciar:
print('''
Bem-vindo ao Console de Jogos!
1 - jogo de perguntas
2 - Pedra, Papel e Tesoura
3 - Adivinhe o Número
0 - Sair
''')
escolha = input("Escolha um jogo (1, 2 ou 3, ou 0 para sair): ")
if escolha == "1":
jogo_perguntas()
elif escolha == "2":
jogar_jokenpo()
elif escolha == "3":
adivinhe_o_numero()
elif escolha == "0":
print("Obrigado por jogar. Até a próxima!")
iniciar = False
else:
print("Opção inválida! Tente novamente.")

console_de_jogos()
