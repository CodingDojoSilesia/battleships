from base import BaseGame


class Game(BaseGame):

    def __init__(self):
        super().__init__()
        self.clicks = 0

    def setup(self):
        pass

    def tick(self, mouse_x=0, mouse_y=0, is_clicked=False):
        # X is from 0 to 23
        # Y is from 0 to 17
        if is_clicked:
            self.clicks += 1
            print(self.clicks, mouse_x, mouse_y)

    def draw_game(self, mouse_x=0, mouse_y=0):
        # X is from 0 to 23
        # Y is from 0 to 17
        self.draw.grid()

        # colors are descripted on https://github.com/kitao/pyxel#color-palette
        # self.draw.text(str, x, y, [color])
        self.draw.text('CODING DOJO', 2, 2)  # default white
        self.draw.text('SILESIA', 2, 3, color=8)

        # self.draw.image(name, x, y)
        # name = ship | selected_ship | miss | hit | cursor
        self.draw.image('ship', 5, 10)
        self.draw.image('selected_ship', 6, 10)
        self.draw.image('miss', 7, 10)
        self.draw.image('hit', 8, 10)
        self.draw.image('cursor', mouse_x, mouse_y)


if __name__ == "__main__":
    game = Game()
    game.setup()
    game.run()

