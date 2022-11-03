import random


class Player:
    def __init__(self, name, playertype=True):
        self.name = name
        self.playertype = playertype
        self.move = None

    def translate_move(self, move):
        if isinstance(move, str):
            possiblemoves_str = {'rock':0,'paper':1,'scizor':2,'exit':3,'quit':3,'instructions':4,'0':0,'1':1,'2':2}
            for k,v in possiblemoves_str.items():
                if k.startswith(move.lower()):
                    return v
    
        return -1

    def get_move(self):
        if not self.playertype:
            self.move = random.randint(0,2)
        else:
            userinp = input("What is your move?: ")
            self.move =  self.translate_move(userinp)
