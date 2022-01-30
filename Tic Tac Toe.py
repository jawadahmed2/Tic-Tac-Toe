#.....................................................................................................................................................#
#Modified by jawad ahmed 
#bscs201959


import numpy as np
class tictactoe:
    def __init__(self):
        self.board=np.zeros((3,3),'int64')
        
    def displayBoard(self):
        print(self.board)
        
    def takeInput(self,player):
        r= int(input("Enter Row"))
        c= int(input("Enter col"))
        isLegal= self.isLegalMove(r,c)
        
        if(isLegal==1):
            self.board[r,c]=player
        
    def turnChange(self,player):
        if(player==1):
            player=2
        else:
            player=1
        return player
    def isLegalMove(self,r,c):
        if(r>-1 and r<3 and c>=0 and c<=2):
            if (self.board[r,c]==0):
                return 1
            else:
                return 0
        else:
            return 0
        
    def isDrawn(self):
        for i in range(3):
            for j in range(3):
                if(self.board[i,j]==0):
                    return 0
        return 10
                
    def isWin(self, player):
        if self.board[0,0]==player and self.board[0,1]==player and self.board[0,2]==player:
            return player
        if self.board[0,0]==player and self.board[1,0]==player and self.board[2,0]==player:
            return player 
        if self.board[0,0]==player and self.board[1,1]==player and self.board[2,2]==player:
            return player
        if self.board[0,1]==player and self.board[1,1]==player and self.board[2,1]==player:
            return player
        if self.board[0,2]==player and self.board[1,2]==player and self.board[2,2]==player:
            return player
        if self.board[1,0]==player and self.board[1,1]==player and self.board[1,2]==player:
            return player
        if self.board[2,0]==player and self.board[2,1]==player and self.board[2,2]==player:
            return player
        if self.board[0,2]==player and self.board[1,1]==player and self.board[2,0]==player:
            return player
                   
        else:
            return 0     
player=1
finish=0
game=tictactoe()
game.displayBoard()
while finish==0:
    
    game.takeInput(player)
    game.displayBoard()
    player=game.turnChange(player)
    finish=game.isDrawn()
    finish=game.isWin(player)
    if finish>0:
        print(player,"IS WIN")
        break
    if finish==10:
        print("GAME IS DRAW")
        break

    #........................................................................................................................................................#