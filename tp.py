# 1
    # A Crie uma lista vazia;
lista_vazia = []

    # B Adicione os elementos: 1, 2, 3, 4 e 5,  usando append();
lista_vazia.append(1)
lista_vazia.append(2)
lista_vazia.append(3)
lista_vazia.append(4)
lista_vazia.append(5)

    # C Imprima a lista;
print(lista_vazia)

    # D Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);

for indice in range(len(lista_vazia) -1 ):
    if lista_vazia[indice] == 3 or lista_vazia[indice] == 6:
        del(lista_vazia[indice])

    # E Imprima a lista modificada
print(lista_vazia)

    # F Imprima também o tamanho da lista usando a função len()
print('tamanho da lista:', len(lista_vazia))

    # G Altere o valor do último elemento para 6 e imprima a lista modificada.

def get_indice_ultimo_elemento():
    return len(lista_vazia) - 1

lista_vazia[get_indice_ultimo_elemento()] = 6
print(lista_vazia)

#8 Escreva um programa em Python que leia um vetor de 5 números inteiros e mostre-os. (código)
vetor = []
total_de_numeros = 5

for n in range(0, 5):
    print()
    #numero_informado = int(input('Informe um número: '))
    #vetor.append(numero_informado)

#print(vetor)

# 9 Escreva um programa em Python que leia um vetor de 10 palavras e mostre-as na ordem inversa de leitura. (código)
palavras = ['porro', 'quisquam', 'est', 'qui', 'dolorem', 'ipsum', 'quia', 'dolor', 'sit', 'amet']

palavras.reverse()

print(palavras)

# 10 Escreva um programa em Python que leia um vetor de números de tamanho t.
# Leia t previamente. 
# Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele. (código)
numeros = []

for n in range(1, 11):
    print()
    #numero = int(input('Informe um númeor: '))
    #numeros.append(numero)

zeros_digitados = 0

for numero in numeros:
    if numero == 0:
        zeros_digitados = zeros_digitados + 1

print('total de zeros digitados: ', zeros_digitados)


# 11 Escreva um programa em Python que leia nomes de alunos e
# suas alturas em metros até que um nome de aluno seja o código de saída “Sair”.
# O programa deve possuir uma função que indica todos os alunos que tenham
# altura acima da média (a média aritmética das alturas de todos os alunos lidos). (código)

alunos = []

class Aluno:
    def __init__(self, nome, altura):
        print('Construindo Aluno')
        self._nome = nome
        self._altura = altura

    @property
    def get_nome(self):
        return self._nome

    @property
    def get_altura(self):
        return self._altura

sair = False

while not sair:
    nome = input('Informe um nome, ou digite "Sair": ').lower()

    if (nome == 'sair'):
        sair = True
        break

    altura = int(input('Informe a altura: '))

    aluno = Aluno(nome, altura)
    alunos.append(aluno)

quantidade_alunos = len(alunos)
somatorio = 0

for aluno in alunos:
    somatorio = somatorio + aluno.get_altura

media = somatorio / quantidade_alunos

def get_alunos_acima_da_media(alunos_cadastrados, media):
    alunos_acima_da_media = []

    for aluno in alunos_cadastrados:
        if aluno.get_altura > media:
            alunos_acima_da_media.append(aluno)

    return alunos_acima_da_media


alunos_acima_media = get_alunos_acima_da_media(alunos, media)

for aluno in alunos_acima_media:
    print(aluno.get_nome)


# 10 Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado vermelho de 100 px de lado no centro da tela.
# O quadrado deve ser capaz de se movimentar vertical e horizontalmente através de teclas do computador. 
# Pode ser ‘a’,’s’,’d’,’w’ ou as setas do teclado. (código e printscreen)


# 11 Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de diâmetro no centro da tela que se move da esquerda para a direita. 
# Sempre que chegar na extremidade direita, o círculo deve voltar à extremidade esquerda, retomando o movimento da esquerda para a direita. (código e printscreen)

# 12 Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo amarelo de 100 px de diâmetro no centro da tela 
# que se move sempre em velocidade permanente na direção que o usuário indicar através das teclas. 
# Similar ao item anterior, sempre que chegar em uma extremidade, 
# o círculo deve voltar à extremidade oposta e continuar o com a última direção que o usuário indicou. (código e printscreen)


#13 Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo verde de 100 px de diâmetro no centro da tela
#  que se inicie o movimento da esquerda para a direita. Sempre que chegar em alguma extremidade, o círculo deve trocar a direção e aumentar a velocidade em 1. (código e printscreen)

#14 Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado de tamanho 50 no centro da tela. 
# Quando o usuário clicar em alguma área da janela, o quadrado deve se mover para a posição clicada. (código e printscreen)


#15 Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha na tela um estrela de 5 pontas no tamanho que preferir. (código e printscreen)


#16 Usando a biblioteca Pygame, escreva um programa que desenha na tela estrelas de 5 pontas de tamanhos aleatórios
# a cada vez que o usuário clicar na tela. A ponta superior da estrela deve estar situada onde o usuário clicou. (código e printscreen)

#17 Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” (visto no curso), com uma modificação. 
# Tal modificação consiste em incluir o aumento da velocidade da bola. 
# O aumento será feito de maneira gradual, isto é, cada 10 vezes que a bola bater na paleta do jogador1 a velocidade aumenta em 1. (código e printscreen)


#18 Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” alterado na questão anterior e que adicione uma nova modificação. 
# Tal modificação consiste em aumentar o ganho de pontos para cada vez que a bola encostar na paleta do jogador1. 
# O aumento da pontuação será também realizada de maneira gradual, porém somente a cada 2 aumentos da velocidade da bola, 
# isto é 1 ponto será atribuído ao total de pontos que o jogador ganha a cada vez que a bola bate na paleta. (código e printscreen)

#19 Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” alterado na questão anterior e que adicione uma nova modificação. 
# Tal modificação consiste em inserir um som quando a bola bate nas paletas dos jogadores. (código)

#20 Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” alterado na questão anterior e que adicione uma nova modificação.
# Tal modificação consiste em inserir um som (vitória) quando a bola bate na borda atrás da paleta do computador. (código)

#21 Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” alterado na questão anterior e que adicione uma nova modificação. 
# Tal modificação consiste em inserir um som (derrota) quando a bola bate na borda atrás da paleta do jogador1. (código)


#22 Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” alterado na questão anterior e que adicione uma nova modificação. 
# Tal modificação consiste em inserir um som a cada 10 pontos feitos pelo jogador. (código)


#23 (Desafio) Usando a biblioteca Pygame, escreva um programa que implemente o jogo da velha para dois jogadores (ambos usuários). (código e printscreen)

