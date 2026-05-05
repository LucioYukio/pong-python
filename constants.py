from PPlay.sprite import *
from PPlay.window import *
from PPlay import keyboard
# Configurações Iniciais
janela = Window(1200, 600)
janela.set_title('Pong Evolution')
janela.set_background_color(0)

teclado = keyboard.Keyboard()

#  Sprites
bola = Sprite('assets/bola1.png')
# Pads Principais (Iniciais)
retang1 = Sprite("assets/ret1.png")
retang2 = Sprite("assets/ret1.png")

# Pads Menores
retan_menor1 = Sprite("assets/ret_menor.png")  # Jogador Topo
retan_menor2 = Sprite("assets/ret_menor.png")  # Jogador Baixo
retan_menor3 = Sprite("assets/ret_menor.png")  # IA Topo
retan_menor4 = Sprite("assets/ret_menor.png")  # IA Baixo

# Variáveis de Controle
placarA = 0
placarB = 0
velocidade_bolax = 400
velocidade_bolay = 400
velocidade_retangulo_y = 450
contador = 0
pause = True
desenha_grande = True
