#pragma once

namespace GameState {
    class Board {
    public:
        Board();
        void display();
        bool placeMove(int row, int col, char player);
        bool isGameOver();
        bool isDraw();

    private:
        char board[3][3];
        bool checkWin(char player);
    };
}
