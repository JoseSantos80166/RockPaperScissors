import sys
import argparse
from player import Player


class Game:
    def __init__(self, max_score,  playername):
        self.max_score = int(max_score)
        self.playernames = playername
        self.run = True
        self.player1 = Player()
        self.player2 = Player()


    def get_player_name(self, player, player2=False):
        if not player.name:
            player.name = input("What is your name?: ")

        if not player.name:
            if player2: 
                player.name = "Guest"
            else:
                with open("playername.txt",'r') as f:
                    player.name = f.readline()          


    def get_game_mode(self):
        choice = int(input("Choose a game mode: (1) - vs CPU   (2) - vs Player 2: "))
        if choice == 1:
            self.player2.name = "BOT"
            self.player2.playertype = False

        elif choice == 2:
            self.get_player_name(self.player2, player2=True)


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

        self.game_loop()


    def player_move(self, player):
        player.get_move()

        if player.move == -1:
            print("Invalid Input")
            self.player_move(player)

        if player.move == 3:
            print("Exiting Game")
            self.run = False

        if player.move == 4:
            print("Possible Inputs: Rock-0, Paper-1, Scizor-2, Exit/Quit, Instructions")
            self.player_move(player)


    def round(self):
        self.player_move(self.player1)
        self.player_move(self.player2)

        movenames = ['Rock','Paper','Scizor','Exit','Instructions']

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
        
        print(f'{movenames[self.player1.move]} vs {movenames[self.player2.move]} -- {round_result_str}')
        

    def game_loop(self):
        self.run = True
        while self.run:
            self.round()
            if self.max_score != -1:
                if self.player1.score == self.max_score or self.player2.score == self.max_score:
                    self.run = False

        print(f'Game Over\nFinal Score: {self.player1.name}:{self.player1.score}  {self.player2.name}:{self.player2.score}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxscore', type=int, default=-1 , help='Maximum score to Win')
    parser.add_argument('--playername', nargs='+', type=str, default="", help='Name of Player 1 and of Player 2 (Optional)')
    args = parser.parse_args()

    if len(args.playername) > 2:
        raise ValueError("Invalid Number of player names")

    game1 = Game(args.maxscore, args.playername)
    
    game1.game_start()
