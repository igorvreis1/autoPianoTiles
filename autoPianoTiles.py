import time

from PIL import ImageGrab
import pyautogui



#tecla = (1, 1, 1)
#teclaStart = (54, 159, 198)
#teclaArrastada = (0, 2, 3)
#teclaAmarela = (255, 183, 9)

def printScrean():
    imagem = ImageGrab.grab()
    #color = screen.getpixel((680, 527))

    #print(color, time.process_time())
    return (imagem)

def procuraTecla(imagem):
    #coordenados de onde estão localizadas cada tecla, isso pode mudar conforme a resolução do seu monitor

    #rangeD = (650,508)
    #rangeF = (735,508)
    #rangeJ = (815,508)
    #rengeK = (895,508)
    cont = 0
    
    #            D          F         J         K
    ranges = ((650,508),(735,508),(815,508),(895,508))
    for i in ranges:
        color = imagem.getpixel(i)
        if color == (1, 1, 1) or color == (54, 159, 198) or color == (0, 2, 3) or color == (255, 183, 9):
            return cont
        cont+=1
    return -1

def aperta(tecla):
    if tecla == 0:
        pyautogui.press("d")
    elif tecla == 1:
        pyautogui.press("f")
    elif tecla == 2:
        pyautogui.press("j")
    else:
        pyautogui.press("k")


print("Começa em 3 segundos, vá para a tela do jogo.")
time.sleep(3)

while True:
    imagem = printScrean()
    tecla = procuraTecla(imagem)
    if tecla != -1:
        aperta(tecla)