"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.
Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

Example 1:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
"""


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[0] * 3 for _ in range(3)]
        for i in range(len(moves)):
            x, y = moves[i]
            if i % 2 == 0:
                grid[x][y] = "A"
            else:
                grid[x][y] = "B"

        def winner(ch):
            if grid[0][0] == grid[0][1] == grid[0][2] == ch or grid[1][0] == grid[1][1] == grid[1][2] == ch \
                    or grid[2][0] == grid[2][1] == grid[2][2] == ch:
                return True
            if grid[0][0] == grid[1][1] == grid[2][2] == ch or grid[0][2] == grid[1][1] == grid[2][0] == ch:
                return True
            if grid[0][0] == grid[1][0] == grid[2][0] == ch or grid[0][1] == grid[1][1] == grid[2][1] == ch \
                    or grid[0][2] == grid[1][2] == grid[2][2] == ch:
                return True
            return False

        if winner("A"):
            return "A"
        if winner("B"):
            return "B"
        if len(moves) >= 9:
            return "Draw"
        return "Pending"

