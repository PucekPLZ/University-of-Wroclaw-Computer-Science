#include "wymierna.hpp"

namespace obliczenia {
    int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    void wymierna::normalize() {
        if (mian < 0) {
            licz = -licz;
            mian = -mian;
        }
        int g = gcd(abs(licz), mian);
        licz /= g;
        mian /= g;
    }

    // konstruktor
    wymierna::wymierna(int licz, int mian) : licz(licz), mian(mian) {
        if (mian == 0) {
            throw std::invalid_argument("mian cannot be 0");
        }
        normalize();
    }

    // operatory binarne
    wymierna wymierna::operator+(const wymierna& other) const {
        if (static_cast<long long>(licz) * other.mian + static_cast<long long>(other.licz) * mian > INT_MAX ||
            static_cast<long long>(licz) * other.mian + static_cast<long long>(other.licz) * mian < INT_MIN) {
            throw overrange_exception("Addition result is out of range");
        }
        return wymierna(licz * other.mian + other.licz * mian, mian * other.mian);
    }

    wymierna wymierna::operator-(const wymierna& other) const {
        if (static_cast<long long>(licz) * other.mian - static_cast<long long>(other.licz) * mian > INT_MAX ||
            static_cast<long long>(licz) * other.mian - static_cast<long long>(other.licz) * mian < INT_MIN) {
            throw overrange_exception("Subtraction result is out of range");
        }
        return wymierna(licz * other.mian - other.licz * mian, mian * other.mian);
    }

    wymierna wymierna::operator*(const wymierna& other) const {
        if (static_cast<long long>(licz) * other.licz > INT_MAX ||
            static_cast<long long>(licz) * other.licz < INT_MIN ||
            static_cast<long long>(mian) * other.mian > INT_MAX ||
            static_cast<long long>(mian) * other.mian < INT_MIN) {
            throw overrange_exception("Multiplication result is out of range");
        }
        return wymierna(licz * other.licz, mian * other.mian);
    }

    wymierna wymierna::operator/(const wymierna& other) const {
        if (other.licz == 0) {
            throw divide_by_zero_exception("Cannot divide by zero");
        }
        if (static_cast<long long>(licz) * other.mian > INT_MAX ||
            static_cast<long long>(licz) * other.mian < INT_MIN ||
            static_cast<long long>(mian) * other.licz > INT_MAX ||
            static_cast<long long>(mian) * other.licz < INT_MIN) {
            throw overrange_exception("Division result is out of range");
        }
        return wymierna(licz * other.mian, mian * other.licz);
    }

    // operatory unarne
    wymierna wymierna::operator-() const {
        return wymierna(-licz, mian);
    }

    wymierna wymierna::operator!() const {
        if (licz == 0) {
            throw std::domain_error("Cannot invert zero");
        }
        return wymierna((licz > 0) ? mian : -mian, abs(licz));
    }

    // operatory rzutowania
    wymierna::operator double() const {
        return static_cast<double>(licz) / static_cast<double>(mian);
    }

    wymierna::operator int() const {
        return static_cast<int>(round(static_cast<double>(licz) / static_cast<double>(mian)));
    }

    // gettery
    int wymierna::getLicznik() const {
        return licz;
    }

    int wymierna::getMianownik() const {
        return mian;
    }

    std::ostream& operator<<(std::ostream& wyj, const wymierna& w) {
        int integer_part = w.licz / w.mian;
        int remainder = abs(w.licz % w.mian);
        wyj << integer_part;

        if (remainder != 0) {
            wyj << '.';
            std::unordered_map<int, int> seen_remainders;
            std::string fraction_part;

            while (remainder != 0 && seen_remainders.find(remainder) == seen_remainders.end()) {
                seen_remainders[remainder] = fraction_part.length();
                remainder *= 10;
                fraction_part += std::to_string(remainder / w.mian);
                remainder %= w.mian;
            }

            if (remainder != 0) {
                int idx = seen_remainders[remainder];
                wyj << fraction_part.substr(0, idx) << '(' << fraction_part.substr(idx) << ')';
            } else {
                wyj << fraction_part;
            }
        }
        return wyj;
    }
}

