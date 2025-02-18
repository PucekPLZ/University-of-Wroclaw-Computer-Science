#include "UserInterface.hpp"
#include "GameState.hpp"
#include "ComputerMove.hpp"
#include <iostream>
#include <stdexcept>

namespace UserInterface {
    void playGame() {
        GameState::Board board;
        std::string input;
        int row, col;
        bool gameOver = false;
        bool validMove = false;
        board.display();
    
        while (!gameOver) {
            // ruch gracza
            do {
                std::cout << "Enter your move (for example: 1A): ";
                std::cin >> input;
            
                row = input[0] - '1';
                col = std::toupper(input[1]) - 'A';
            
                validMove = board.placeMove(row, col, 'X');
                if (!validMove) {
                    std::cout << "Invalid move. Try again." << std::endl;
                }
            } while (!validMove);
        
            board.display();
        
            if (board.isGameOver()) {
                std::cout << "GGWP" << std::endl;
                break;
            }

            if (board.isDraw()) {
                std::cout << "It's a draw!" << std::endl;
                break;
            }
        
            // ruch komputera
            std::pair<int, int> computerMove = ComputerMove::getNextMove(board);
            board.placeMove(computerMove.first, computerMove.second, 'O');
            std::cout << "Computer played: " << (computerMove.first + 1) << static_cast<char>('A' + computerMove.second) << std::endl;
        
            board.display();
        
            if (board.isGameOver()) {
                std::cout << "Computer won!" << std::endl;
                break;
            }

            if (board.isDraw()) {
                std::cout << "It's a draw!" << std::endl;
                break;
            }
        }
    }
}
