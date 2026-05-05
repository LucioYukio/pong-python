import constants as con
import mod as m

m.reposicionamento()
# --- Game Loop ---
while True:
    con.janela.set_background_color(0)

    m.desenha()

    m.play()
    if not con.pause:
        m.pong()
        m.pads()
        m.placar()
    con.janela.update()