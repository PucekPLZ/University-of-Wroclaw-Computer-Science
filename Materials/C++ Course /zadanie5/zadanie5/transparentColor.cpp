#include "transparentColor.hpp"
#include <iostream>
#include <cstdint>

using namespace std;

transparentColor::transparentColor(): color(), Alpha(255) {}
transparentColor::transparentColor(uint8_t R, uint8_t G, uint8_t B, uint8_t alpha) : color(R, G, B) {
    Alpha = alpha;
}

uint8_t transparentColor::getAlpha() const {
    return Alpha;
}

int transparentColor::getAlpha_int() const {
    return static_cast<int>(Alpha);
}

void transparentColor::setAlpha(uint8_t new_alpha) {
    Alpha = new_alpha;
}



