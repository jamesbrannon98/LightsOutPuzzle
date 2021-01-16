import random
import copy

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.board = board

    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        self.board[row][col] = not self.board[row][col]
        if row - 1 >= 0:
            self.board[row - 1][col] = not self.board[row - 1][col]
        if row + 1 < len(self.board):
            self.board[row + 1][col] = not self.board[row + 1][col]
        if col - 1 >= 0:
            self.board[row][col - 1] = not self.board[row][col - 1]
        if col + 1 < len(self.board[0]):
            self.board[row][col + 1] = not self.board[row][col + 1]

    def scramble(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if random.random() < 0.5:
                    self.perform_move(row, col)

    def is_solved(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col]:
                    return False
        return True

    def copy(self):
        return copy.deepcopy(self)

    def successors(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                new = self.copy()
                new.perform_move(row, col)
                yield (row, col), new

    def find_solution(self):
        frontier = [self]
        solution = []
        visited = {}
        if self.is_solved():
            return solution
        while frontier:
            board = frontier.pop(0)         
            for move, new in board.successors():
                board = tuple(tuple(x) for x in new.board)
                if board in visited:
                    continue
                else:
                    visited[board] = [move]
                if new.is_solved():
                    while new.board != self.board:
                        check = tuple(tuple(x) for x in new.board)
                        solution = visited[check] + solution
                        new.perform_move(solution[0][0], solution[0][1])
                    return list(solution)
                frontier.append(new)
        return None

def create_puzzle(rows, cols):
     return LightsOutPuzzle([[False for col in range(cols)] for row in range(rows)])
