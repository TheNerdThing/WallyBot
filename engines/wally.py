import sys
import os
sys.path.append(os.path.join(sys.path[0],'../'))
import chess
from chess.engine import PlayResult
from engine_wrapper import MinimalEngine
import runSavedBot


class Wally(MinimalEngine):
    DEPTH = 3
    def search(self, board: chess.Board, *args: any) -> PlayResult:
        whiteToMove = chess.Board.turn == chess.WHITE
        runSavedBot.find_best_move(board, DEPTH,whiteToMove,)