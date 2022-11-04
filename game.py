import sys
import argparse
from player import Player


class Game:
    def __init__(self, max_score,  playername):
        self.max_score = int(max_score)
        self.playernames = playername
        self.run = True
        self.started = False
        self.resetgame = False 
        self.rounds = 0
        self.player1 = Player()
        self.player2 = Player()

    def game_start(self):
        if len(self.playernames) == 0:
            self.get_player_name(self.player1)
            self.get_game_mode()

        elif len(self.playernames) == 1:
            self.player1.name = self.playernames[0]
            self.get_game_mode()

        elif len(self.playernames) == 2:
            self.player1.name,self.player2.name = self.playernames

        with open("playername.txt",'w') as f:
            f.write(self.player1.name)

        self.resetgame = False
        self.game_loop()


    def get_player_name(self, player, player2=False):
        if not player.name:
            player.name = input("What is your name?: ")

        if not player.name:
            if player2: 
                player.name = "Guest"
            else:
                with open("playername.txt",'r') as f:
                    player.name = f.readline()
                    if player.name == "":
                        print("Name not chosen, using 'Player1'")
                        player.name = "Player1"          


    def get_game_mode(self):
        choice = (input("Choose a game mode: (1) - vs CPU   (2) - vs Player 2   Exit   Instructions: "))
        if choice == "1":
            self.player2.name = "BOT"
            self.player2.playertype = False

        elif choice == "2":
            self.get_player_name(self.player2, player2=True)

        elif choice == "exit":
            self.run = False

        elif choice == "instructions":
            print("This is a Rock Paper scizors game:")
            print("You can play against CPU or another player locally")
            print("When you are in the game you must choose your move as following")
            print("0=Rock 1=Paper 2=Scizors")
            print("The player can either type the numbers or the name of the move")
            print("Type exit/quit to close the game or instructions to read this again")
            self.get_game_mode()

        else:
            self.get_game_mode()



    def player_move(self, player):
        player.get_move()

        while player.move == -1:
            player.get_move()

        if player.move == 3:
            print("Exiting Game")
            self.run = False

        if player.move == 5:
            print("Quiting to Menu")
            self.started = False
            self.player1.reset_score()
            self.player2.reset_score()
            self.rounds = 0
            self.run = False
            self.resetgame = True

        if player.move == 4:
            print("Possible Inputs: Rock-0, Paper-1, Scizor-2, Exit/Quit, Instructions")
            self.player_move(player)


    def round(self):
        self.started = True
        self.rounds += 1

        movenames = ['Rock','Paper','Scizor','Exit','Instructions']
        self.player_move(self.player1)
        if self.run:
            self.player_move(self.player2)

        if self.run:
            if self.player1.move == self.player2.move:
                round_result_str = 'TIE'
            else:
                moveset = [self.player1.move,self.player2.move]
                winningmoves = [[0,2],[2,1],[1,0]]
                if moveset in winningmoves:
                    self.player1.score += 1
                    round_result_str = f'{self.player1.name} Wins the Round'
                else:
                    self.player2.score += 1
                    round_result_str = f'{self.player2.name} Wins the Round'
        
            print(f'Round Nº{self.rounds}:  {movenames[self.player1.move]} vs {movenames[self.player2.move]} -- {round_result_str}  ({self.player1.score}-{self.player2.score})')
        

    def game_loop(self):
        while self.run:
            self.round()
            if self.max_score != -1:
                if self.player1.score == self.max_score or self.player2.score == self.max_score:
                    self.run = False
        if self.started:
            print(f'Game Over\nFinal Score: {self.player1.name}:{self.player1.score}  {self.player2.name}:{self.player2.score}')
        elif self.resetgame:
            self.run = True
            self.game_start()
        else:
            print("Game Exiting")
            


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxscore', type=int, default=-1 , help='Maximum score to Win')
    parser.add_argument('--playername', nargs='+', type=str, default="", help='Name of Player 1 and of Player 2 (Optional)')
    args = parser.parse_args()

    if len(args.playername) > 2:
        raise ValueError("Invalid Number of player names")

    game1 = Game(args.maxscore, args.playername)
    
    game1.game_start()
