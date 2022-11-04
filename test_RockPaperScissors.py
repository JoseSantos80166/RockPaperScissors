import pytest
from player import Player
from game import Game

## Various players to test

@pytest.fixture
def Player1():
    return Player("Jose")

@pytest.fixture
def CPU1():
    return Player("BOT",False)

@pytest.fixture
def GAME1():
    return game(3,"Jose")

@pytest.fixture
def GAME2():
    return game(5,"")



##-------------Tests for Player class-------------##

#Check if attributes are correctly placed
def test_attributes(Player1,CPU1):
    assert Player1.name != ""
    assert Player1.playertype == True

    assert CPU1.name != ""
    assert CPU1.playertype == False

#Check if given a string of any portion of the move (P,Pa,pap,PaPe,PaPEr)
@pytest.mark.parametrize("text,move", [("Pap", 1), ("paPeR", 1),("P",1),("rO",0),("2",2),("bananas",-1),("Per",-1)])
def test_get_move(Player1,text,move):
    assert Player1.translate_move(text) == move


##-------------Tests for Game class-------------##

def test_attributes_game(GAME1,GAME2):
    GAME1.maxscore == 3
    GAME1.name == "Jose"
    GAME2.maxscore == 5
    GAME2.name == ""

def test_game_start(GAME1,GAME2):
    GAME1.game_start(GAME1.name,1)
