#pragma once
#include <iostream>


using namespace std;

class pixel {
public:
    pixel();
    pixel(int xh, int yh);
    int getX() const;
    int getY() const;
    void setX(int new_x);
    void setY(int new_y);
    int disLeft() const;
    int disRight() const;
    int disTop() const;
    int disBottom() const;
protected:
    static const int height = 1080;
    static const int width = 1920;
    int x;
    int y;
};

int distance(const pixel &p, const pixel &q);
int distance(const pixel *p, const pixel *q);
