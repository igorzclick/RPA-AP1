import time
import pyautogui

#Oi professor, tudo bem?
#este arquivo, esta aqui apenas pois esta nos requisitos do projeto,
#porem não estamos ultilizando as posições na tela, pois elas mudam de resolução pra resolução,
#algo que roda na minha maquina, poderia não rodar na sua, então mantivemos aqui, mas não estamos usando.

def get_mouse_position():
   
    time.sleep(5)
    
    
    x, y = pyautogui.position()
    
  
    print(f"Mouse position: ({x}, {y})")


get_mouse_position()    
    
 