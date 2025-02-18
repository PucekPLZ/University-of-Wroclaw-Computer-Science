#pragma once
#include "pixel.hpp"
#include "transparentColor.hpp"


class coloredPixel : public pixel, public transparentColor {
public:
    coloredPixel();
    coloredPixel(int xh, int yh, transparentColor  kolor);
    transparentColor getColor() const;
    void setColor(transparentColor kolor);
    void movePixel(int xp,int yp);
private:
    transparentColor color;
};


