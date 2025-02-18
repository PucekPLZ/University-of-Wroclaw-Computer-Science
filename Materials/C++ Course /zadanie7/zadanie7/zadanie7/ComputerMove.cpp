#include "ComputerMove.hpp"
#include "GameState.hpp"
#include <ctime>
#include <cstdlib>
#include <vector>

namespace ComputerMove {
    std::pair<int, int> getNextMove(GameState::Board& board) {
        std::srand(std::time(0));
        std::vector<std::pair<int, int>> emptySpaces;
        int priority[3][3] = {
            {1, 2, 1},
            {2, 3, 2},
            {1, 2, 1}
        };
        int row, col;
        
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board.placeMove(i, j, '-')) {
                    emptySpaces.push_back(std::make_pair(i, j));
                }
            }
        }
    
        if (!emptySpaces.empty()) {
            int selected = std::rand() % emptySpaces.size();
            row = emptySpaces[selected].first;
            col = emptySpaces[selected].second;
        
            for (auto& space : emptySpaces) {
                if (priority[space.first][space.second] >
                    priority[row][col]) {
                    row = space.first;
                    col = space.second;
                }
            }
        }
    
        return std::make_pair(row, col);
    }
}
