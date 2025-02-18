#pragma once
#include "color.hpp"
#include <cstdint>

class transparentColor : public virtual color {
public:
    transparentColor();
    transparentColor(uint8_t Rh, uint8_t Gh, uint8_t Bh, uint8_t alpha);
    uint8_t getAlpha() const;
    int getAlpha_int() const;
    void setAlpha(uint8_t new_alpha);

protected:
    uint8_t Alpha;
};

