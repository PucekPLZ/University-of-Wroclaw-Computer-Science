#include "colornt.hpp"


colornt::colornt(uint8_t R, uint8_t G, uint8_t B, const string& name, uint8_t alpha) : color(R, G, B), transparentColor(R, G, B, alpha), namedColor(R, G, B, name) {

}



