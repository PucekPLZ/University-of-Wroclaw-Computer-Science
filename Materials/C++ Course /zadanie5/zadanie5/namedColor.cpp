#include "namedColor.hpp"
#include <stdexcept>

namedColor::namedColor(): color() {}
namedColor::namedColor(uint8_t R, uint8_t G, uint8_t B, string name) : color(R, G, B) {
    for (int i = 0; i < name.length(); i++){
        
        if (name[i] >= 'a' && name[i] <= 'z'){
        }
        else {
            throw invalid_argument("Incorrect data type");
        }
    }
    Name = name;
}

string namedColor::getName() const{
    return Name;
}

void namedColor::setName(string new_name) {
    for (int i = 0; i < new_name.length(); i++){
        
        if (new_name[i] >= 'a' && new_name[i] <= 'z'){
        }
        else {
            throw invalid_argument("Incorrect data type");
        }
    }
    Name = new_name;
}
