#include "coloredPixel.hpp"
#include <utility>
#include <stdexcept>

coloredPixel::coloredPixel() : pixel(0, 0), transparentColor() {}

coloredPixel::coloredPixel(int xh, int yh, transparentColor  kolor) : pixel(xh, yh), color(std::move(kolor)) {}

transparentColor coloredPixel::getColor() const {
    return color;
}

void coloredPixel::setColor(transparentColor kolor) {
    color = kolor;
}

void coloredPixel::movePixel(int xp, int yp) {
    
    if(xp + x > 0 && xp + x < width) {
        x += xp;
    }
    else {
        throw invalid_argument("Incorrect data type");
    }
    
    if(yp + y > 0 && yp + y < height) {
        y += yp;
    }
    else {
        throw invalid_argument("Incorrect data type");
    }
}
