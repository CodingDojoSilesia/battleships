from game import Game
from base import Drawer

from unittest.mock import Mock, call


def get_game(*args, **kwargs):
    game = Game(*args, **kwargs)
    game.draw = Mock(spec=Drawer)
    return game


def test_tick():
    game = get_game()
    game.tick(is_clicked=True)

    assert game.clicks == 1


def test_draw():
    game = get_game()
    game.draw_game(mouse_x=5, mouse_y=5)

    # more info about mocks:
    # https://docs.python.org/3/library/unittest.mock.html
    game.draw.grid.assert_called_once_with()
    assert game.draw.text.call_args_list == [
        call('CODING DOJO', 2, 2),
        call('SILESIA', 2, 3, color=8),
    ]

    assert game.draw.image.call_args_list == [
        call('ship', 5, 10),
        call('selected_ship', 6, 10),
        call('miss', 7, 10),
        call('hit', 8, 10),
        call('cursor', 5, 5),
    ]
