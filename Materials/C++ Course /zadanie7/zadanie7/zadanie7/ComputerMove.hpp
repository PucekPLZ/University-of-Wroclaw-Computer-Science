#pragma once
#include "GameState.hpp"
#include <utility>

namespace ComputerMove {
    std::pair<int, int> getNextMove(GameState::Board& board);
}
