import pyxel
import random

class App:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.balance = 100000
        pyxel.init(255, 255, caption="Wallstreetbets The Game", fps=10)
        pyxel.image(0).load(0, 0, "resources/logo.png")

        #background music
        a = "c3e2g2c3 e2g2c3e2"
        b = "c3d2g2c3 d2g2c3d2"
        pyxel.sound(0).set(a * 3 + b * 1, "t", "2", "f", 30)
        pyxel.play(0, 0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.x = (self.x + 1) % pyxel.width
        self.y = (self.y + random.randint(1, 2))
        self.updatebalance()

    def updatebalance(self):
        self.balance -= 1000

    def draw(self):
        pyxel.cls(0)
        pyxel.line(0, 0, self.x + 1, self.y + 5, 8)
        pyxel.text(80, 41, "Wallstreetbets The Game", pyxel.frame_count % 16)
        pyxel.text(180, 41, "$" + str(self.balance), pyxel.frame_count % 16)
        pyxel.blt(50, 50, 0, 0, 0, 150, 150)
App()
