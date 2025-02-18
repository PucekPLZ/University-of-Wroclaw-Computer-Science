#include "color.hpp"
#include <iostream>
#include <cstdint>

using namespace std;

color::color(uint8_t Rh, uint8_t Gh, uint8_t Bh) {
    R = Rh;
    G = Gh;
    B = Bh;
}

color::color() {
    R = 0;
    G = 0;
    B = 0;
}

uint8_t color::getR() const {
    return R;
}

uint8_t color::getG() const {
    return G;
}

uint8_t color::getB() const {
    return B;
}

void color::setR(uint8_t new_r) {
    R = new_r;
}

void color::setG(uint8_t new_g) {
    G = new_g;
}

void color::setB(uint8_t new_b) {
    B = new_b;
}

void color::brighten_color(int val) {
    int r = R + val;
    int g = G + val;
    int b = B + val;

    R = (r > 255) ? 255 : static_cast<uint8_t>(r);
    G = (g > 255) ? 255 : static_cast<uint8_t>(g);
    B = (b > 255) ? 255 : static_cast<uint8_t>(b);
}

void color::darken_color(int val) {
    int r = R - val;
    int g = G - val;
    int b = B - val;

    R = (r < 0) ? 0 : static_cast<uint8_t>(r);
    G = (g < 0) ? 0 : static_cast<uint8_t>(g);
    B = (b < 0) ? 0 : static_cast<uint8_t>(b);
}

color color::mix_colors(color color1, color color2) {
    uint8_t red;
    uint8_t green;
    uint8_t blue;
    red = (color1.getR() + color2.getR()) / 2;
    green = (color1.getG() + color2.getG()) / 2;
    blue = (color1.getB() + color2.getB()) / 2;
    return {red, green, blue};
}

int color::getR_int() const {
    return static_cast<int>(R);
}

int color::getG_int() const {
    return static_cast<int>(G);
}

int color::getB_int() const {
    return static_cast<int>(B);
}
