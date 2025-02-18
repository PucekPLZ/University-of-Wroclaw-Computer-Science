#include "tabbit.hpp"
#include <iostream>

using namespace std;

tab_bit::tab_bit(int rozm) : dl(rozm) {
    if (rozm < 0) {
            throw InvalidSizeException();
    }
    dl = rozm;
    int size_tb = (rozm + rozmiarSlowa - 1) / rozmiarSlowa;
    tab = new slowo[size_tb]{};
}

tab_bit::tab_bit(slowo tb) : dl(rozmiarSlowa), tab(new slowo[1]{tb}) {
    if (dl < 0 || dl > rozmiarSlowa) {
            throw InvalidSizeException();
    }
}

// konstruktor kopiujacy
tab_bit::tab_bit(const tab_bit& t) : dl(t.dl) {
    int size_tb = (t.dl + rozmiarSlowa - 1) / rozmiarSlowa;
    tab = new slowo[size_tb];
    for (int i = 0; i < size_tb; i++) {
        tab[i] = t.tab[i];
    }
}

//konstruktor przenoszacy
tab_bit::tab_bit(tab_bit&& t) : dl(t.dl), tab(t.tab) {
    dl = 0;
    t.tab = nullptr; // null poiter
}

tab_bit::tab_bit(int rozm, const initializer_list<bool>& values) : tab_bit(rozm) {
    int i = 0;
    for (bool value : values) {
        (*this)[i++] = value;
    }
}

tab_bit& tab_bit::operator=(const tab_bit& t) {
    if (this != &t) {
        delete[] tab;

        dl = t.dl;
        int size_tb = (t.dl + rozmiarSlowa - 1) / rozmiarSlowa;
        tab = new slowo[size_tb];
        for (int i = 0; i < size_tb; i++) {
            tab[i] = t.tab[i];
        }
    }
    return *this;
}

tab_bit& tab_bit::operator=(tab_bit&& t) {
    if (this != &t) {
        delete[] tab;

        dl = t.dl;
        tab = t.tab;
        t.tab = nullptr;
    }
    return *this;
}

tab_bit::~tab_bit() {
    delete[] tab;
    tab = nullptr;
}

bool tab_bit::czytaj(int i) const {
    if (i < 0 || i >= dl) {
            throw InvalidIndexException();
    }
    int index_tabb = i / rozmiarSlowa;
    int index_bit = i % rozmiarSlowa;
    return (tab[index_tabb] & (1ull << index_bit)) != 0;
}

bool tab_bit::pisz(int i, bool b) {
    if (i < 0 || i >= dl) {
            throw InvalidIndexException();
    }
    int index_tabb = i / rozmiarSlowa;
    int index_bit = i % rozmiarSlowa;
    if (b) {
        tab[index_tabb] |= (1ull << index_bit);
    } else {
        tab[index_tabb] &= ~(1ull << index_bit);
    }
    return b;
}

bool tab_bit::operator[](int i) const {
    return czytaj(i);
}

tab_bit::ref tab_bit::operator[](int i) {
    return ref(*this, i);
}

int tab_bit::rozmiar() const {
    return dl;
}

tab_bit::ref& tab_bit::ref::operator=(bool value) {
    tb.pisz(index, value);
    return *this;
}

tab_bit::ref::operator bool() const {
    return tb.czytaj(index);
}

istream& operator>>(istream& we, tab_bit& tb) {
    for (int i = 0; i < tb.rozmiar(); i++) {
        bool value;
        we >> value;
        tb[i] = value;
    }
    return we;
}

ostream& operator<<(ostream& wy, const tab_bit& tb) {
    for (int i = 0; i < tb.rozmiar(); i++) {
        wy << static_cast<int>(tb[i]);
    }
    
    return wy;
}

tab_bit& tab_bit::operator&=(const tab_bit& other) {
    if (dl != other.dl) {
            throw InvalidSizeException();
    }
    int size = (dl + rozmiarSlowa - 1) / rozmiarSlowa;
    for (int i = 0; i < size; ++i) {
        tab[i] &= other.tab[i];
    }
    return *this;
}

tab_bit& tab_bit::operator|=(const tab_bit& other) {
    if (dl != other.dl) {
            throw InvalidSizeException();
    }
    int size = (dl + rozmiarSlowa - 1) / rozmiarSlowa;
    for (int i = 0; i < size; ++i) {
        tab[i] |= other.tab[i];
    }
    return *this;
}

tab_bit& tab_bit::operator^=(const tab_bit& other) {
    if (dl != other.dl) {
            throw InvalidSizeException();
    }
    int size = (dl + rozmiarSlowa - 1) / rozmiarSlowa;
    for (int i = 0; i < size; ++i) {
        tab[i] ^= other.tab[i];
    }
    return *this;
}

tab_bit tab_bit::operator~() const {
    tab_bit result(dl);
    int size = (dl + rozmiarSlowa - 1) / rozmiarSlowa;
    for (int i = 0; i < size; ++i) {
        result.tab[i] = ~tab[i];
    }
    return result;
}


