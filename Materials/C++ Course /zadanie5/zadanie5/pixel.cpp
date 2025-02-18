#include "pixel.hpp"
#include <cmath>
#include <stdexcept>

using namespace std;

pixel::pixel() : x(0), y(0) {}

pixel::pixel(int xh, int yh) {
    if(xh > 0 && xh < width) {
        x = xh;
    }
    else {
        throw invalid_argument("Incorrect data type");
    }
    
    if(yh > 0 && yh < height) {
        y = yh;
    }
    else {
        throw invalid_argument("Incorrect data type");
    }
}

int pixel::getX() const {
    return x;
}

int pixel::getY() const {
    return y;
}

void pixel::setX(int new_x) {
    if(new_x > 0 && new_x < width) {
        x = new_x;
    }
    else {
        throw invalid_argument("Incorrect data type");
    }
}

void pixel::setY(int new_y) {
    if(new_y > 0 && new_y < height) {
        y = new_y;
    }
    else {
        throw invalid_argument("Incorrect data type");
    }
}

int pixel::disLeft() const {
    return x;
}

int pixel::disRight() const {
    return width - x;
}

int pixel::disTop() const {
    return y;
}

int pixel::disBottom() const {
    return height - y;
}

int distance(const pixel &p, const pixel &q){
    int dis_x = p.getX() - q.getX();
    int dis_y = p.getY() - q.getY();
    return int(sqrt(dis_x*dis_x + dis_y*dis_y));
}

int distance(const pixel *p, const pixel *q) {
    return distance(*p, *q);
}











