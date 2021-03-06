"""
example2_1

例題2-1（基礎）

Copyright (c) 2018-2019 Shogo MURAMATSU, All rights reserved
"""
from board import Board
#from gui_board import GuiBoard
from board_out_of_range_exception import BoardOutOfRangeException

def main():
    try:
        # Board型のインスタンスboardを生成
        board = Board() # GuiBoard()
        # 盤(board)の状態を表示（初期状態）
        board.display_state()
        # 盤(board)の3列4行目に手番の石(Black)を置いてみる
        print('(x,y) = (3,4)')
        board.try_place_stone(3,4)
        # 盤(board)の状態を表示
        board.display_state()
        
        # 盤(board)の5列3行目に手番の石(White)を置いてみる
        print('(x,y) = (5,3)')
        board.try_place_stone(5,3)
        # 盤(board)の状態を表示
        board.display_state()
        
        # パスする
        print('パス')
        board.change()
        # 盤(board)の状態を表示
        board.display_state()
        
        print()
        
    except BoardOutOfRangeException as boore:
        print()
        print(boore)
        
    
if __name__ == '__main__':
    main()
