from PPlay.sprite import *
from PPlay.window import *
from PPlay import keyboard

# Configurações Iniciais
janela = Window(1200, 600)
janela.set_title('Pong Evolution')
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


def reposicionamento():
    global velocidade_bolax, velocidade_bolay, pause, contador, desenha_grande
    bola.set_position(janela.width / 2 - bola.width / 2, janela.height / 2 - bola.height / 2)
    velocidade_bolax = 400 if velocidade_bolax > 0 else -400
    velocidade_bolay = 400

    contador = 0
    desenha_grande = True

    # Posição inicial dos pads grandes
    retang1.set_position(10, janela.height / 2 - retang1.height / 2)
    retang2.set_position(janela.width - 10 - retang2.width, janela.height / 2 - retang2.height / 2)
    pause = True


def atualizar_pads_menores():
    """Faz os pads menores seguirem o movimento do pad 'pai' com o espaçamento"""
    # Lado do Jogador (Esquerda)
    retan_menor1.set_position( retang1.x, retang1.y)
    retan_menor2.set_position( retang1.x,  retang1.y + retan_menor1.height + 150)# Espaçamento de 150px
    # Lado da IA (Direita)
    retan_menor3.x = retang2.x
    retan_menor3.y = retang2.y
    retan_menor4.x = retang2.x
    retan_menor4.y = retang2.y + retan_menor3.height + 150


reposicionamento()

# --- Game Loop ---
while True:
    janela.set_background_color(0)

    if pause:
        if teclado.key_pressed("space"):
            pause = False
    else:
        # Movimentação da bola
        bola.x += velocidade_bolax * janela.delta_time()
        bola.y += velocidade_bolay * janela.delta_time()

        # Colisão com teto e chão
        if (bola.y <= 0 and velocidade_bolay < 0) or (bola.y + bola.height >= janela.height and velocidade_bolay > 0):
            velocidade_bolay *= -1

        # Lógica de Evolução (Divisão dos Pads)
        if contador >= 3:
            desenha_grande = False

        atualizar_pads_menores()

        # --- Lógica de Colisão ---
        if desenha_grande:
            # Colisão com pads grandes
            if (bola.collided(retang1) and velocidade_bolax < 0) or (bola.collided(retang2) and velocidade_bolax > 0):
                velocidade_bolax *= -1.1
                contador += 1
        else:
            # Colisão com os 4 pads menores simultaneamente
            # Lado Esquerdo (1 e 2)
            if (bola.collided(retan_menor1) or bola.collided(retan_menor2)) and velocidade_bolax < 0:
                velocidade_bolax *= -1.1
                contador += 1
            # Lado Direito (3 e 4)
            if (bola.collided(retan_menor3) or bola.collided(retan_menor4)) and velocidade_bolax > 0:
                velocidade_bolax *= -1.1
                contador += 1

        # --- Movimentação dos Pads ---
        # Jogador
        if (teclado.key_pressed("up") or teclado.key_pressed("w")) and retang1.y > 0:
            retang1.y -= velocidade_retangulo_y * janela.delta_time()
        if (teclado.key_pressed("down") or teclado.key_pressed("s")):
            # Limite inferior considera o pad menor de baixo se estiver dividido
            limite = retan_menor2.y + retan_menor2.height if not desenha_grande else retang1.y + retang1.height
            if limite < janela.height:
                retang1.y += velocidade_retangulo_y * janela.delta_time()

        # IA (segue o centro da bola)
        meio_ia = retang2.y + (retang2.height / 4)
        if meio_ia > bola.y and retang2.y > 0:
            retang2.y -= velocidade_retangulo_y * janela.delta_time()
        elif meio_ia < bola.y:
            limite_ia = retan_menor4.y + retan_menor4.height if not desenha_grande else retang2.y + retang2.height
            if limite_ia < janela.height:
                retang2.y += velocidade_retangulo_y * janela.delta_time()

        # Placar
        if bola.x < 0:
            placarB += 1
            reposicionamento()
        elif bola.x > janela.width:
            placarA += 1
            reposicionamento()

    # --- Desenho ---
    bola.draw()
    if desenha_grande:
        retang1.draw()
        retang2.draw()
    else:
        retan_menor1.draw()
        retan_menor2.draw()
        retan_menor3.draw()
        retan_menor4.draw()

    janela.draw_text(f"{placarA} x {placarB}", janela.width / 2 - 40, 20, size=30, color=(255, 255, 255))
    janela.update()