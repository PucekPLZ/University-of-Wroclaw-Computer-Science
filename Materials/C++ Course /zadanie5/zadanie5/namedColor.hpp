#pragma once
#include "color.hpp"
#include <string>
#include <cstdint>

using namespace std;

class namedColor : public virtual color {
public:
    namedColor();
    namedColor(uint8_t Rh, uint8_t Gh, uint8_t Bh, string name = "");
    string getName() const;
    void setName(string new_name);
private:
    string Name;
};
