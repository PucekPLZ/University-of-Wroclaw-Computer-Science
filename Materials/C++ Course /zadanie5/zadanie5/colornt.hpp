#pragma once
#include "color.hpp"
#include "transparentColor.hpp"
#include "namedColor.hpp"
#include <cstdint>


using namespace std;

class colornt : public namedColor, public transparentColor {
public:
    colornt(uint8_t Rh, uint8_t Gh, uint8_t Bh, const string& name, uint8_t alpha);
};



