from random import randint

while True:
    print('Escolha: \n 1-Pedra \n 2-Papel \n 3-Tesoura \n 0- Sair')
    pergunta = int(input('Escolha um numero: '))
    pc = randint(1,3)

    if pergunta == 0:
        print('Você escolheu sair, Encerrando...')    
        break

    elif pc == pergunta:

      if pc == 1:
        pc = '1-Pedra' 
        pergunta = '1-Pedra'
        print('Empate: \n pc: escolheu {}\n Você: escolheu {}'.format(pc, pergunta)) 

      elif pc == 2:
        pc = '2-Papel'       
        pergunta = '2-Papel' 
        print('Empate: \n pc: escolheu {}\n Você: escolheu {}'.format(pc, pergunta)) 

      elif pc == 3:
        pc = '3-Tesoura'       
        pergunta = '3-Tesoura'                         
        print('Empate: \n pc: escolheu {}\n Você: escolheu {}'.format(pc, pergunta))

    elif pc == 1 and pergunta == 2:
            pc = '1-Pedra'
            pergunta = '2-Papel'

            print('Vitoria: \n pc: escolheu {} \n Você: escolheu {}'.format(pc, pergunta)) 

    elif pc == 1 and pergunta == 3:
            pc = '1-Pedra'
            pergunta = '3-Tesoura'

            print('Derrota: \n pc: escolheu {} \n Você: escolheu {}'.format(pc, pergunta))

    elif pc == 2 and pergunta == 3:
            pc = '2-Papel'
            pergunta = '3-Tesoura'
            print('Vitoria: \n pc: escolheu {} \n Você: escolheu {}'.format(pc, pergunta))

    elif pc == 2 and pergunta == 1:
            pc = '1-Pedra'
            pergunta = '3-Tesoura'
            print('Derrota: \n pc: escolheu {} \n Você: escolheu {}'.format(pc, pergunta))
        
    elif pc == 3 and pergunta == 1:
            pc = '3-Tesoura'
            pergunta = '1-Pedra'
            print('Vitoria: \n pc: escolheu {} \n Você: escolheu {}'.format(pc, pergunta))

    elif pc == 3 and pergunta == 2:
            pc = '3-Tesoura'
            pergunta = '2-Papel'
            print('Derrota: \n pc: escolheu {} \n Você: escolheu {}'.format(pc, pergunta))        

  
        

