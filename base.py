import pyxel


class Drawer:
    TILE_SIZE = 10
    IMAGES = {
        'ship': 0,
        'selected_ship': 1,
        'hit': 2,
        'miss': 3,
        'cursor': 4,
        'grid': 5,
    }

    def image(self, name, tile_x, tile_y):
        tile = self.TILE_SIZE
        index = self.IMAGES[name]
        x = tile_x * tile
        y = tile_y * tile
        sx = index * tile
        sy = 0
        img_bank = 0

        pyxel.blt(x, y, img_bank, sx, sy, tile, tile, 12)

    def text(self, string, tile_x, tile_y, color=7):
        tile = self.TILE_SIZE
        x = int(tile_x * tile)
        y = int(tile_y * tile)
        pyxel.text(x, y, string, color)

    def grid(self):
        for board in range(2):
            for y in range(10):
                shift = board * 12
                self.text(str(y + 1), shift + 0.25, y + 5.25)
                for x in range(10):
                    xx = x + shift
                    self.image('grid', xx + 1, y + 5)

            for x in range(10):
                xx = x + board * 12
                self.text(chr(x + 65), xx + 1.5, 4.25)

class BaseGame:
    TILE_SIZE = Drawer.TILE_SIZE
    WIDTH = 24
    HEIGHT = 18

    def __init__(self):
        self.draw = Drawer()

    def run(self):
        width_px = self.TILE_SIZE * self.WIDTH
        height_px = self.TILE_SIZE * self.HEIGHT
        pyxel.init(width_px, height_px)
        pyxel.image(0).load(0, 0, 'tile.png')
        pyxel.run(self._tick, self._draw)

    def setup(self):
        pass

    def draw_game(self, mouse_x=0, mouse_y=0):
        pass

    def tick(self, mouse_x=0, mouse_y=0, is_clicked=False):
        pass

    def _get_mouse_args(self):
        tile = self.TILE_SIZE

        return {
            'mouse_x': pyxel.mouse_x // tile,
            'mouse_y': pyxel.mouse_y // tile,
        }

    def _tick(self):
        is_clicked = pyxel.btnp(pyxel.KEY_LEFT_BUTTON)
        self.tick(is_clicked=is_clicked, **self._get_mouse_args())
        pass

    def _draw(self):
        pyxel.cls(12)
        self.draw_game(**self._get_mouse_args())
