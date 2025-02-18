#pragma once
#include <iostream>
#include <stdexcept>
#include <cmath>
#include <string>
#include <unordered_map>

class measurable_exception : public std::logic_error {
public:
    explicit measurable_exception(const std::string& msg) : std::logic_error(msg) {}
};

class overrange_exception : public measurable_exception {
public:
    explicit overrange_exception(const std::string& msg) : measurable_exception(msg) {}
};

class divide_by_zero_exception : public measurable_exception {
public:
    explicit divide_by_zero_exception(const std::string& msg) : measurable_exception(msg) {}
};

namespace obliczenia {
    class wymierna {
    private:
        int licz, mian;
        void normalize();

    public:
        // konstruktor
        wymierna(int licz = 0, int mian = 1);

        // operatory binarne
        wymierna operator+(const wymierna& other) const;
        wymierna operator-(const wymierna& other) const;
        wymierna operator*(const wymierna& other) const;
        wymierna operator/(const wymierna& other) const;

        // operatory unarne
        wymierna operator-() const;
        wymierna operator!() const;

        // operatory rzutowania
        operator double() const;
        explicit operator int() const;

        // gettery
        int getLicznik() const;
        int getMianownik() const;

        friend std::ostream& operator<<(std::ostream& wyj, const wymierna& w);
    };
}


