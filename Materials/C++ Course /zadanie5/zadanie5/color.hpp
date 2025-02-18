#pragma once
#include <cstdint>


class color {
public:
    color(uint8_t Rh, uint8_t Gh, uint8_t Bh);
    color();
    
    uint8_t getR() const;
    uint8_t getG() const;
    uint8_t getB() const;
    int getR_int() const;
    int getG_int() const;
    int getB_int() const;
    
    void setR(uint8_t new_r);
    void setG(uint8_t new_g);
    void setB(uint8_t new_b);
    void darken_color(int val);
    void brighten_color(int val);
    static color mix_colors(color color1, color color2);

protected:
    uint8_t R;
    uint8_t G;
    uint8_t B;
};
