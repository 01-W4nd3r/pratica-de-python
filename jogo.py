print(' ')
print('=====|jogo|=====')
'''
fassa um jogo que crie um alimento
e pinte esse alimento de uma cor unica que o usuário
escolher.

crie tambem uma função que ramdomize essa escolha
'''
print(' ')  
from time import sleep
import random

# cores a ser escolhidas.  

cor = {'yellow':"\033[7;33m",'blue':"\033[7;34m",'green':"\033[7;32m",'red':"\033[7;31m",'purple':"\033[7;35m",'cyan':"\033[7;36m",'white':"\033[7;37m"}
cor2 = ["\033[7;33m","\033[7;34m","\033[7;32m","\033[7;31m","\033[7;35m","\033[7;36m","\033[7;37m"]

# alimentos a ser escolhidas. 

frut ={'melancia':"MELANCIA",'uva':"UVA",'cenoura':"CENOURA",'abobora':"ABÓBORA",'batata':"BATATA",'abacate':"ABACATE",'jaca':"JACÁ",'pepino':"PEPINO"}
frut2 =["MELANCIA","UVA","CENOURA","ABÓBORA","BATATA","ABACATE","JACÁ","PEPINO"]

# menu de cores e alimentos 

null = '\033[0m'

print('=====|CORES|=====')
print(f"{cor2[0]}YELLOW{cor2[1]}BLUE\n{cor2[2]}GREEN{cor2[3]}RED\n{cor2[4]}PURPLE{cor2[5]}CYAN\n{cor2[6]}WHITE{null}")
print('=====|CORES|=====')
print(f' MELANCIA UVA\n CENOURA ABÓBORA\n ABACATE JACA\n PEPINO')
print('=================')

# pega uma cor aleatória e um alimento aleatório e mistura os dois e cria um alimento unico

def mistura():
    mistu_cor = random.choice(cor2)
    mistu_frut = random.choice(frut2)
    print("resultado")
    sleep(1.0)
    print(' ')
    null = '\033[0m'
    print(f'{mistu_cor}{mistu_frut}{null}')
    
# pega a cor e pega o alimento e misturam os dois pra formar um alimento unico

def mesclar():        
    pega_cor = input("digite a cor: ")
    pega_frut = input("digite a fruta: ")
    null = '\033[0m'
    print ("resultado")
    sleep(1.0)
    print(' ')
    print(f"{cor[pega_cor]}{frut[pega_frut]}{null}")

print(' ')
null = '\033[0m'


# executa as funções mistura e mesclar

while True:
    print(' ')
    choose = input('escholha entre criação \naleatória [A]\nmanual    [m]\nou sair   [s]!: ')
    if choose == 'a': # requisito para executar a função mistura
       while True: 
          print(' ')       
          mistura()
          next = input('quer continuar [s/n]?: ')
          if next == 'n':
              break
          while True: # friuta a resposta do usuário para receber somente valor 's' ou 'n'                                  
              if next != 's':                           
                  print('\033[0;33mVALUE_ERROR... unidentified value  \n[N][S]!\033[0m')
                  next = input('quer continuar [s/n]?: ')
              elif next == 's':
                  break
    elif choose == 'm': # requisito para executar a função mesclar      
       while True:     
          print(' ')       
          mesclar()
          next = input('quer continuar [s/n]?: ')
          if next == 'n':
              break 
          while True: # friuta a resposta do usuário para receber valor 's' ou 'n'
              if next != 's':
                  print('\033[0;33mVALUE_ERROR... unidentified value  \n[N][S]!\033[0m')
                  next = input('quer continuar [s/n]?: ')
              elif next == 's':
                  break
    elif choose == 's': # requisito para sair do programa 
       break     
    else: # mensagem de erro
        print(' ')
        print('\033[0;31mVALUE_ERROR... unidentified value  \n[A][M][S]!\033[0m')
print(' ')
