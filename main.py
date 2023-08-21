import turtle # permite usar as funções e objetos do módulo turtle
import random # para determinar os passos em cada ciclo
# criar os competidores
alex = turtle.Turtle()
blex = turtle.Turtle()
clex = turtle.Turtle()
# define a quantidade de passos da corrida
passos = 200 # corrida de 200 passos
# criar o juiz, traçar a linha de chegada e se posicionar
juiz = turtle.Turtle()
juiz.penup()
juiz.setpos(200, 100)
juiz.right(90)
juiz.pendown()
juiz.forward(200)
juiz.right(180)
# contadores
n_venc = 0 # número de vencedores da corrida
alex_passos = 0 # número de passos de alex
blex_passos = 0 # número de passos de blex
clex_passos = 0 # número de passos de clex
# posiciona alex e clex. blex já está posicionado
alex.penup()
alex.setpos(0, 50)
alex.pendown()
clex.penup()
clex.setpos(0, -50)
clex.pendown()
# cores
alex.color("blue")
blex.color("green")
clex.color("red")
# aparência
alex.shape("turtle")
blex.shape("turtle")
clex.shape("turtle")
# largura da linha
alex.pensize(5)
blex.pensize(5)
clex.pensize(5)
# inicia a corrida
# vamos usar 1000 ciclos - suficiente para terminar uma corrida
# random.seed()
for i in range(1000):
    # movimenta alex
    k = random.randrange(5)
    alex.forward(k)
    alex_passos += k
    if alex_passos >= passos:
        print("alex venceu a corrida")
        n_venc += 1
    # movimenta blex
    k = random.randrange(5)
    blex.forward(k)
    blex_passos += k
    if blex_passos >= passos:
        print("blex venceu a corrida")
        n_venc += 1

    # movimenta clex
    k = random.randrange(5)
    clex.forward(k)
    clex_passos += k
    if clex_passos >= passos:
        print("clex venceu a corrida")
        n_venc += 1
    if (n_venc > 0): break
#temos um ou mais vencedores
if (n_venc == 1): print("temos um vencedor")
else: print("houve empate")  