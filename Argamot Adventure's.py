from time import sleep

def load():
    sleep(1.5)

def aguarde():
    contagemRegressiva = 5
    for n in range (0,6):
        print(contagemRegressiva)
        contagemRegressiva -= 1
        load()


# Sistema
fadaGuia=("Luxanna")
apFadaGuia=("Lux")
danoFada=(1000)
# HP MOBS
hpMobTuto = 5

# Skills Mago
while 'mago' or 'Mago':
    mago = ("2força + 10pdh + 5dfs + 5vida + 0arm + 20mana")
    skill0 = ('Você utilizou Tempestade de Areia e deu 5 de dano.')
    skill1 = ('Você utilizou Raio Magnetico e deu 5 de dano.')
    skills = [skill0, skill1]
    forca=2
    pdh=10
    defesa=5
    vida=5
    armadura=0
    mana=20
    danoSkill1 = 5
    break

# Skills Guerreiro
while 'guerreiro' or 'Guerreiro':
    guerreiro = ("15força + 0pdh + 8dfs + 10vida + 20arm + 0mana")
    skill0 = ("Você utilizou Corta-Vento e deu 5 de dano.")
    skill1 = ('Você utilizou Corte Certeiro e deu 5 de dano.')
    skills = [skill0, skill1]
    forca=15
    pdh=0
    defesa=8
    vida=10
    armadura=20
    mana=0
    danoSkill1 = 5
    break


# Skills Arqueiro
while 'arqueiro' or 'Arqueiro':
    arqueiro = ("10força + 5pdh + 5dfs + 8vida + 10arm + 5mana")
    skill0 = ('Você utilizou Ponta de Agulha e deu 5 de dano.')
    skill1 = ('Você utilizou Precisão Perfeita e deu 5 de dano.')
    skills = [skill0,skill1]
    forca=10
    pdh=5
    defesa=5
    vida=8
    armadura=10
    mana=5
    danoSkill1 = 5
    break


while True:

    nome=input("Olá, Guerreiro! Antes de me apresentar, me diga seu nome: ")
    print(f'Seja bem vindo, {nome}, eu me chamo {fadaGuia}, mas pode me chamar de {apFadaGuia}. Por favor escolha sua classe: ')
    from time import sleep
    load()

    while True:
        print("Você pode escolher entre mago, guerreiro e arqueiro! Lembre-se, cada um contem uma habilidade e atributos únicos.")
        load()

        escolha = input("E então qual vai ser?: ")
        if escolha == "mago" or escolha == "Mago":
            print("Você escolheu a classe Mago! Estes são seus atributos: ", mago)
        elif escolha == "guerreiro" or escolha == "Guerreiro":
            print("Você escolheu a classe Guerreiro! Estes são seus atributos: ", guerreiro)
        elif escolha == "arqueiro" or escolha == "Arqueiro":
            print("Você escolheu a classe Arqueiro! Estes são seus atributos:", arqueiro)
        else:
            print("Vamos com calma, essa classe ainda não está disponível!")
            sleep(1)
            continue
        load()

        confirmacao = input("Você confirma a classe escolhida?: ")
        if confirmacao == "sim" or confirmacao == "Sim":
            print("Que legal! Agora, pegue seus equipamentos e vamos adentrar um mundo repleto de magias!")
            print("CARREGANDO... AGUARDEE!")
        elif confirmacao == "nao" or confirmacao == "Não" or confirmacao == "não" or confirmacao == "Nao":
            print("Ops! Vamos retornar para escolha.")
            continue
        else:
            print(f'Ops! Essa classe ainda não está disponivel.')
            continue
            
        
        
        aguarde()
        break
    
    load()

    print("Olá, {}, seja bem vindo à Argomort.".format(nome))
    confirmarTutorial=input("Você deseja passar por nosso tutorial? ")
    if confirmarTutorial == "sim" or confirmarTutorial == "Sim":
        print("Muito bem! Vamos aos campos de treinamento.")
        print("CARREGANDO... AGUARDE!")
        aguarde()
        
        if escolha == 'mago' or escolha == 'Mago':
            print(f'Olá {nome}, chegamos ao campo de treinamento. Vamos lá!')
            load()
            print(f'Veja, um monstro ali na frente. Use sua primeira habilidade para dar dano nele.')
            load()
            print("Sistema: Veja bravo guerreiro, este mob contém 5 de vida, é hora de critar nele!")
            load()
            usarSkill1=input("Vamos escolha uma skill que deseja utilizar 0-Tempestade de Areia ou 1-Raio Magnetico: ")
            if usarSkill1 == '0':
                print(skills[0])
                resultadoDano = danoSkill1 - hpMobTuto
                load()
                print(f'Ual, você acertou o mob e causou {danoSkill1} de dano, levando seu HP à {resultadoDano}.')
                load()
                print(f'SISTEMA: Voltando para o Argomot!')
                aguarde()
            elif usarSkill1 == '1':
                print(skills[1])
                resultadoDano = danoSkill1 - hpMobTuto
                load()
                print(f'Ual, você acertou o mob e causou {danoSkill1} de dano, levando seu HP à {resultadoDano}.')
                load()
                print(f'SISTEMA: Voltando para o Argomot!')
                aguarde()

        elif escolha == 'guerreiro' or escolha == 'Guerreiro':
            print(f'Olá {nome}, chegamos ao campo de treinamento. Vamos lá!')
            load()
            print(f'Veja, um monstro ali na frente. Use sua primeira habilidade para dar dano nele.')
            print("Sistema: Veja bravo guerreiro, este mob contém 5 de vida, é hora de critar nele!")
            load()
            usarSkill1=input("Vamos escolha uma skill que deseja utilizar 0-Corta-Vento ou 1-Corte Certeiro: ")
            if usarSkill1 == '0':
                print(skills[0])
                resultadoDano = danoSkill1 - hpMobTuto
                load()
                print(f'Ual, você acertou o mob e causou {danoSkill1} de dano, levando seu HP à {resultadoDano}.')
                load()
                print(f'SISTEMA: Voltando para o Argomot!')
                aguarde()
            elif usarSkill1 == '1':
                print(skills[1])
                resultadoDano = danoSkill1 - hpMobTuto
                load()
                print(f'Ual, você acertou o mob e causou {danoSkill1} de dano, levando seu HP à {resultadoDano}.')
                load()
                print(f'SISTEMA: Voltando para o Argomot!')
                aguarde()
            

        elif escolha == 'arqueiro' or escolha == 'Arqueiro':
                print(f'Olá {nome}, chegamos ao campo de treinamento. Vamos lá!')
                load()
                print(f'Veja, um monstro ali na frente. Use sua primeira habilidade para dar dano nele.')
                print("Sistema: Veja bravo guerreiro, este mob contém 5 de vida, é hora de critar nele!")
                load()
                usarSkill1=input("Vamos escolha uma skill que deseja utilizar 0-Ponta de Agulha ou 1-Precisão Perfeita: ")
                if usarSkill1 == '0':
                    print(skills[0])
                    resultadoDano = danoSkill1 - hpMobTuto
                    load()
                    print(f'Ual, você acertou o mob e causou {danoSkill1} de dano, levando seu HP à {resultadoDano}.')
                    load()
                    print(f'SISTEMA: Voltando para o Argomot!')
                    aguarde()
                elif usarSkill1 == '1':
                    print(skills[1])
                    resultadoDano = danoSkill1 - hpMobTuto
                    load()
                    print(f'Ual, você acertou o mob e causou {danoSkill1} de dano, levando seu HP à {resultadoDano}.')
                    load()
                    print(f'SISTEMA: Voltando para o Argomot!')
                    aguarde()        

                elif usarSkill1 % '1' or '0':
                    print(f'Vamos com calma {nome}. Ainda não aprendemos essa técnica.')
    elif confirmarTutorial == "não" or confirmarTutorial == "nao" or confirmarTutorial == "Não" or confirmarTutorial == "Nao":
        print("Certo, você irá lutar por sua conta e risco!")
        print(f'SISTEMA: Entrando no mundo...')
        aguarde()

    print(f'{fadaGuia}: Olá novamente, {nome}. Seja Bem-Vindo(a) à Argomot!')
    load()

    print(f'Argomot é um Mundo repleto de Magia e de muita calma, onde todos os reinos vivem em harmonia, mas...')
    load()

    print(f'{nome}: Mas, o quê?')
    load()

    print(f'{fadaGuia}: Ultimamente uma força maligna está nos aterrorizando, e precisamos de sua ajuda!')
    load()
    
    ajuda = input(f'SISTEMA: Você deseja ajudar {fadaGuia}? Confirme com "Sim" ou "Não": ')
    load()

    if ajuda == 'Sim' or ajuda == 'sim':
        print(f'{nome}: Não se preocupe, {fadaGuia}. Juntos iremos acabar com todos eles!')
        load()
        print(f'{fadaGuia}: Que maravilha, sabia que poderia contar com você.')
        load()
        print(f'{fadaGuia}: Juntos seremos uma ótima dupla!')
        load()
        print('SISTEMA: CONTINUA NA PRÓXIMA ATUALIZAÇÃO.')
        load()
        print('Muito Obrigado por jogar nosso protótipo!')
        load()
        print('Por favor, entre em contato para seu feedback: programmerantunes@gmail.com')
        load()
        print('SAINDO...')
        aguarde()
        break

    elif ajuda == 'Não' or ajuda == 'nao' or ajuda == 'não':
        print(f'Eu não irei me envolver. Quem disse que isso é problema meu?')
        load()

        if escolha == 'mago' or escolha == 'Mago':
            print(f'{fadaGuia}: Não! Não! Impossível, eles me disseram que você era o escolhido!\nVocê deve retornar de onde veio, por favor não resista {nome}')
            load()
            escolhaSit = input(f'SISTEMA: {fadaGuia} está a lhe expulsar de Argomot.\nO que você irá fazer: "Resistir" ou "Deixar"?: ')
            if escolhaSit == 'resistir' or escolhaSit == 'Resistir':
                load()
                print(f'SISTEMA: {fadaGuia} DISFERE HABILIDADE FEIXO DE LUZ CONTRA VOCÊ')
                load()
                resultDano = (vida) - (danoFada)
                print(f'{fadaGuia} Acerta Feixo de Luz: Dano Recebido: {danoFada} - Vida Restante: {vida} = {resultDano} ')
                load()
                print('SISTEMA: Você morreu!')
                load()
                print('Muito Obrigado por jogar nosso protótipo!')
                load()
                print('Por favor, entre em contato para seu feedback: programmerantunes@gmail.com')
                aguarde()
                break
        elif escolha == 'guerreiro' or escolha == 'Guerreiro':
            print(f'{fadaGuia}: Não! Não! Impossível, eles me disseram que você era o escolhido!\nVocê deve retornar de onde veio, por favor não resista {nome}')
            load()
            escolhaSit = input(f'SISTEMA: {fadaGuia} está a lhe expulsar de Argomot.\nO que você irá fazer: "Resistir" ou "Deixar"?: ')
            if escolhaSit == 'resistir' or escolhaSit == 'Resistir':
                load()
                print(f'SISTEMA: {fadaGuia} DISFERE HABILIDADE FEIXO DE LUZ CONTRA VOCÊ')
                load()
                resultDano = (vida) - (danoFada)
                print(f'{fadaGuia} Acerta Feixo de Luz: Dano Recebido: {danoFada} - Vida Restante: {vida} = {resultDano} ')
                load()
                print('SISTEMA: Você morreu!')
                load()
                print('Muito Obrigado por jogar nosso protótipo!')
                load()
                print('Por favor, entre em contato para seu feedback: programmerantunes@gmail.com')
                load()
                print('SAINDO...')
                aguarde()
                break

        elif escolha == 'arqueiro' or escolha == 'Arqueiro':
            print(f'{fadaGuia}: Não! Não! Impossível, eles me disseram que você era o escolhido!\nVocê deve retornar de onde veio, por favor não resista {nome}')
            load()
            escolhaSit = input(f'SISTEMA: {fadaGuia} está a lhe expulsar de Argomot.\nO que você irá fazer: "Resistir" ou "Deixar"?: ')
            if escolhaSit == 'resistir' or escolhaSit == 'Resistir':
                load()
                print(f'SISTEMA: {fadaGuia} DISFERE HABILIDADE FEIXO DE LUZ CONTRA VOCÊ')
                load()
                resultDano = (vida) - (danoFada)
                print(f'{fadaGuia} Acerta Feixo de Luz: Dano Recebido: {danoFada} - Vida Restante: {vida} = {resultDano} ')
                load()
                print('SISTEMA: Você morreu!')
                load()
                print('Muito Obrigado por jogar nosso protótipo!')
                load()
                print('Por favor, entre em contato para seu feedback: programmerantunes@gmail.com')
                load()
                print('SAINDO...')
                aguarde()
                break
            elif escolhaSit == 'deixar' or escolhaSit == 'Deixar':
                print(f'SISTEMA: {nome} acorda de seu sonho.')
                print(f'{nome}: Mas que sonho esquisito, parecia tão real...')
                load()
                print('Muito Obrigado por jogar nosso protótipo!')
                load()
                print('Por favor, entre em contato para seu feedback: programmerantunes@gmail.com')
                load()
                print('SAINDO...')
                aguarde()
                break
