#pragma once
#include <iostream>
#include <iomanip>

std::istream& clearline(std::istream& is);

class ignore_manip {
    int x;
public:
    explicit ignore_manip(int x);

    friend std::istream& operator>>(std::istream& is, const ignore_manip& im);
};

ignore_manip ignore(int x);

std::ostream& comma(std::ostream& os);

std::ostream& colon(std::ostream& os);

class index_manip {
    int x, w;
public:
    explicit index_manip(int x, int w);

    friend std::ostream& operator<<(std::ostream& os, const index_manip& im);
};

index_manip index(int x, int w);
