from PPlay.sprite import *
from PPlay.window import *
from PPlay import keyboard
import constants as con






def reposicionamento():
    con.bola.set_position(con.janela.width / 2 - con.bola.width / 2, con.janela.height / 2 - con.bola.height / 2)
    con.velocidade_bolax = 400 if con.velocidade_bolax > 0 else -400
    con.velocidade_bolay = 400

    con.contador = 0
    con.desenha_grande = True

    # Posição inicial dos pads grandes
    con.retang1.set_position(10, con.janela.height / 2 - con.retang1.height / 2)
    con.retang2.set_position(con.janela.width - 10 - con.retang2.width, con.janela.height / 2 - con.retang2.height / 2)
    con.pause = True


def play():
    # Apertar espaço pra começar o jogo
    if con.pause:
        if con.teclado.key_pressed("space"):
            con.pause = False

def pong():
        # Movimentação da bola
        con.bola.x += con.velocidade_bolax * con.janela.delta_time()
        con.bola.y += con.velocidade_bolay * con.janela.delta_time()


        # Colisão com teto e chão
        if (con.bola.y <= 0 and con.velocidade_bolay < 0) or (con.bola.y + con.bola.height >= con.janela.height and con.velocidade_bolay > 0):
            con.velocidade_bolay *= -1

        # Lógica de Evolução (Divisão dos Pads)
        if con.contador >= 3:
            con.desenha_grande = False


        # Lógica de Colisão
        if con.desenha_grande:
            # Colisão com pads grandes
            if (con.bola.collided(con.retang1) and con.velocidade_bolax < 0) or (con.bola.collided(con.retang2) and con.velocidade_bolax > 0):
                con.velocidade_bolax *= -1.1
                con.contador += 1
        else:
            # Colisão com os 4 pads menores simultaneamente
            # Lado Esquerdo (1 e 2)
            if (con.bola.collided(con.retan_menor1) or con.bola.collided(con.retan_menor2)) and con.velocidade_bolax < 0:
                con.velocidade_bolax *= -1.1
                con.contador += 1
            # Lado Direito (3 e 4)
            if (con.bola.collided(con.retan_menor3) or con.bola.collided(con.retan_menor4)) and con.velocidade_bolax > 0:
                con.velocidade_bolax *= -1.1
                con.contador += 1

def pads():
     # Movimentação dos Pads
        # Jogador
        if (con.teclado.key_pressed("up") or con.teclado.key_pressed("w")) and con.retang1.y > 0:
            con.retang1.y -= con.velocidade_retangulo_y * con.janela.delta_time()
        if (con.teclado.key_pressed("down") or con.teclado.key_pressed("s")):
            # Limite inferior considera o pad menor de baixo se estiver dividido
            limite = con.retan_menor2.y + con.retan_menor2.height if not con.desenha_grande else con.retang1.y + con.retang1.height
            if limite < con.janela.height:
                con.retang1.y += con.velocidade_retangulo_y * con.janela.delta_time()

    # IA (segue o centro da bola)
        meio_ia = con.retang2.y + (con.retang2.height / 4)
        if meio_ia > con.bola.y and con.retang2.y > 0:
            con.retang2.y -= con.velocidade_retangulo_y * con.janela.delta_time()
        elif meio_ia < con.bola.y:
            limite_ia = con.retan_menor4.y +con. retan_menor4.height if not con.desenha_grande else con.retang2.y + con.retang2.height
            if limite_ia < con.janela.height:
                con.retang2.y += con.velocidade_retangulo_y * con.janela.delta_time()

        """Faz os pads menores seguirem o movimento do pad 'pai' com o espaçamento"""
    # Lado do Jogador (Esquerda)
        con.retan_menor1.set_position( con.retang1.x, con.retang1.y)
        con.retan_menor2.set_position( con.retang1.x,  con.retang1.y + con.retan_menor1.height + 150)# Espaçamento de 150px
    # Lado da IA (Direita)
        con.retan_menor3.set_position( con.retang2.x, con.retang2.y)
        con.retan_menor4.set_position( con.retang2.x,  con.retang2.y + con.retan_menor3.height + 150)


def placar():
        # Placar
        if con.bola.x < 0:
            con.placarB += 1
            reposicionamento()
        elif con.bola.x > con.janela.width:
            con.placarA += 1
            reposicionamento()

def desenha():
    con.bola.draw()
    if con.desenha_grande:
        con.retang1.draw()
        con.retang2.draw()
    else:
        con.retan_menor1.draw()
        con.retan_menor2.draw()
        con.retan_menor3.draw()
        con.retan_menor4.draw()

    con.janela.draw_text(f"{con.placarA} x {con.placarB}", con.janela.width / 2 - 40, 20, size=30, color=(255, 255, 255))
