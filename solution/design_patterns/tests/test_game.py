
import pytest

from dungeon_explorer.game import DungeonGame


@pytest.fixture
def dungeon_game():
    """create test data with a small level for testing"""
    yield DungeonGame(x=3, y=1, level=[
        "######",
        "#....#",
        "#....#",
        "#....#",
        "#....#",
        "######",
    ])

def test_move(dungeon_game):
    """pytest finds fixture by name"""
    dungeon_game.move_player("right")
    assert dungeon_game.x == 4
    assert dungeon_game.status == "running"

@pytest.mark.slow
def test_move_twice(dungeon_game):
    """
    call with pytest -m slow
    place marks in pytest.ini or pyproject.toml to disable warnings
    """
    dungeon_game.move_player("left")
    dungeon_game.move_player("left")
    assert dungeon_game.x == 1

def test_error(dungeon_game):
    with pytest.raises(ValueError):
        dungeon_game.status = "invalid"
