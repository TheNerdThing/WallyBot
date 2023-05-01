import sys
import os
sys.path.append(os.path.join(sys.path[0],'../'))
import chess
from chess.engine import PlayResult
from engine_wrapper import MinimalEngine


class Wally(MinimalEngine):
    
    def search(self, board: chess.Board, *args: any) -> PlayResult:
        print('hello world')