import pyautogui as pg #automatizção de cliques e teclas
import numpy as np #randomizar numero do pixel

#para o codigo
pg.FAILSAFE = True #Ao levar rapidamente o mouse para o canto esquerdo encerra o código
pg.useImageNotFoundException(False) #Tratamento de erro de excessão

#biblioteca imagens de track (prints exatos dos items a sua escolha)
icones = {
   'images/loot_cacth/1.png':0.7,
   'images/loot_cacth/2.png':0.7,
   'images/loot_cacth/5.png':0.7,
   'images/loot_cacth/4.png':0.7,
}
#funação de click aleatório pós tela azul 
def click_aleatorio():
     x =  np.random.randint(300, 1600)
     y = np.random.randint (200, 800)
     pg.click(x, y)

#biblioteca track tela_azul
icon = {'images/loot_cacth/3.png':0.5}

#função de clique na tela azul
def tela_azul():
        print('Procurando tela azul')
        for tela, tempo_click in icon.items():
            posi = pg.locateCenterOnScreen(tela, confidence=0.90) #serve para comprar a imagem mostrada com a da biblioteca
            if posi:                                              #sendo 0.90 (90%) de proximidade minima para a ação
                print('tela dectada')
                pg.moveTo(posi)
                pg.click(posi)
                pg.sleep(tempo_click)
                click_aleatorio()

            return True
        
        return False

tela_azul()

#funação de interação com a imagem
def acao():
        for imagem, segundos in icones.items():
            print("Porcurando a imagem:", imagem)
            posicao = pg.locateCenterOnScreen(imagem, confidence=0.60)
            if posicao:
                print('localizei o icone')
                pg.moveTo(posicao)
                pg.press('2') #Pode usar qualquer tecla como hotkey
                pg.click(posicao)
                pg.sleep(segundos)
                
                return True
#para questões de escalabilidade ao poder fazer que uma função dependa da outra para ocorrer caso necessáio
        return False 
                
acao()
# Looping princial da automção (aperte Ctrl + C no terminal ou
#  arraste o mouse para o canto esquerdo da tela para encerrar)
def bot():
    while True:
        tela_azul()
        acao()
bot()