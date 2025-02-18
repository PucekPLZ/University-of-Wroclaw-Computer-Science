#include "manipulatory.hpp"

std::istream& clearline(std::istream& is) {
    char c;
    while(is.get(c) && c != '\n');
    return is;
}

ignore_manip::ignore_manip(int x): x(x) {}

std::istream& operator>>(std::istream& is, const ignore_manip& im) {
    for(int i=0; i < im.x && is; ++i) {
        char c;
        if(is.get(c) && c == '\n')
            break;
    }
    return is;
}

ignore_manip ignore(int x) {
    return ignore_manip(x);
}

std::ostream& comma(std::ostream& os) {
    return os << ", ";
}

std::ostream& colon(std::ostream& os) {
    return os << ": ";
}

index_manip::index_manip(int x, int w): x(x), w(w) {}

std::ostream& operator<<(std::ostream& os, const index_manip& im) {
    os << "[" << std::setw(im.w) << im.x << "]";
    return os;
}

index_manip index(int x, int w) {
    return index_manip(x, w);
}
