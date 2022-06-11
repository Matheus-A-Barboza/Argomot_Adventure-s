from cgi import print_arguments
import sys
import os
from time import sleep
# Sistema
fadaGuia=("Luxanna")
apFadaGuia=("Lux")
# HP MOBS
hpMobTuto = 5

# Skills Mago
mago = ("2força + 10pdh + 5dfs + 5vida + 0arm + 20mana")
skillMago1 = ("Você usou Tempeste de Areia e deu 5 de dano")
danoSkill1 = 5 

# Skills Guerreiro
guerreiro = ("15força + 0pdh + 8dfs + 10vida + 20arm + 0mana")

# Skills Arqueiro
arqueiro = ("10força + 5pdh + 5dfs + 8vida + 10arm + 5mana")

while True:

    nome=input("Olá, Guerreiro! Antes de me apresentar, me diga seu nome: ")
    print(f'Seja bem vindo, {nome}, eu me chamo {fadaGuia}, mas pode me chamar de {apFadaGuia}. Por favor escolha sua classe: ')
    from time import sleep
    sleep(1)

    print("Você pode escolher entre mago, guerreiro e arqueiro! Lembre-se, cada um contem uma habilidade e atributos únicos.")
    from time import sleep
    sleep(1)

    escolha = input("E então qual vai ser?: ")
    if escolha == "mago" or escolha == "Mago":
        print("Você escolheu a classe Mago! Estes são seus atributos: ", mago)
    elif escolha == "guerreiro" or escolha == "Guerreiro":
        print("Você escolheu a classe Guerreiro! Estes são seus atributos: ", mago)
    elif escolha == "arqueiro" or escolha == "Arqueiro":
        print("Você escolheu a classe Arqueiro! Estes são seus atributos:", arqueiro)
    else:
        print("Vamos com calma, essa classe ainda não está disponível!")
    from time import sleep
    sleep(1)

    confirmacao = input("Você confirma a classe escolhida?: ")
    if confirmacao == "sim" or confirmacao == "Sim":
        print("Que legal! Agora, pegue seus equipamentos e vamos adentrar um mundo repleto de magias!")
    print("CARREGANDO... AGUARDEE!")
    if confirmacao == "nao" or confirmacao == "Não" or confirmacao == "não" or confirmacao == "Nao":
        print("Ops! Vamos retornar para escolha.")
        continue
    from time import sleep
    contagemRegressiva = 5
    for n in range (0,6):
        print(contagemRegressiva)
        contagemRegressiva -= 1
        sleep(1)
    
    from time import sleep
    sleep(1)

    print("Olá, {}, seja bem vindo à Argomort.".format(nome))
    confirmarTutorial=input("Você deseja passar por nosso tutorial? ")
    if confirmarTutorial == "sim" or confirmarTutorial == "Sim":
        print("Muito bem! Vamos aos campos de treinamento.")
        print("CARREGANDO... AGUARDE!")
        from time import sleep

        contagemRegressiva = 5
        for n in range (0,6):
            print(contagemRegressiva)
            contagemRegressiva -= 1
            sleep(1)
        print(f'Olá {nome}, chegamos ao campo de treinamento. Vamos lá!')
        print(f'Veja, um monstro ali na frente. Use sua primeira habilidade para dar dano nele.')
        print("Sistema: Veja bravo guerreiro, este mob contém 5 de vida, é hora de critar nele!")
        usarSkill1=input("Vamos utilize sua Primeira Skill Tempestade de Areia apertando a tecla 1: ")
        if usarSkill1 == "1":
            resultadoDano = danoSkill1 - hpMobTuto
            print(f'Ual, você acertou e o mob e causou {danoSkill1} de dano, levando seu HP à {resultadoDano}.')
    elif confirmarTutorial == "não" or confirmarTutorial == "nao" or confirmarTutorial == "Não" or confirmarTutorial == "Nao":
        print("Certo, você irá lutar por sua conta e risco!")

