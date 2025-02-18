#include <iostream>
#include <initializer_list>
#include <stdexcept>
#ifndef tab_bit_hpp
#define tab_bit_hpp

using namespace std;

class InvalidSizeException : public std::runtime_error {
public:
    InvalidSizeException() : std::runtime_error("Invalid size") {}
};

class InvalidIndexException : public std::runtime_error {
public:
    InvalidIndexException() : std::runtime_error("Invalid index") {}
};

class tab_bit {
private:
    typedef uint64_t slowo; // komorka w tablicy
    static const int rozmiarSlowa = sizeof(slowo)*8; // rozmiar slowa w bitach
    int dl; // liczba bitów
    slowo* tab; // tablica bitów

public:
    friend istream& operator>>(istream& we, tab_bit& tb);
    friend ostream& operator<<(ostream& wy, const tab_bit& tb);

    class ref;

protected:
    bool czytaj(int i) const; // metoda pomocnicza do odczytu bitu
    bool pisz(int i, bool b); // metoda pomocnicza do zapisu bitu

public:
    explicit tab_bit(int rozm); // wyzerowana tablica bitow [0...rozm]
    explicit tab_bit(slowo tb); // tablica bitów [0...rozmiarSlowa] zainicjalizowana wzorcem
    tab_bit(const tab_bit &tb); // konstruktor kopiujący
    tab_bit(tab_bit &&tb); // konstruktor przenoszący
    tab_bit& operator=(const tab_bit &tb); // przypisanie kopiujące
    tab_bit& operator=(tab_bit &&tb); // przypisanie przenoszące
    ~tab_bit(); // destruktor

    tab_bit(int rozm, const initializer_list<bool>& values); // constructor with initializer_list

    bool operator[](int i) const; // indeksowanie dla stałych tablic bitowych
    ref operator[](int i); // indeksowanie dla zwykłych tablic bitowych
    inline int rozmiar() const; // rozmiar tablicy w bitach
    
    tab_bit& operator&=(const tab_bit& rhs); // koniunkcja
    tab_bit& operator|=(const tab_bit& rhs); // alternatywa
    tab_bit& operator^=(const tab_bit& rhs); // roznica symetryczna
    tab_bit operator~() const; // negacja 
    
    class ref {
        friend class tab_bit;

    private:
        tab_bit& tb;
        int index;

        ref(tab_bit& tb, int index) : tb(tb), index(index) {}

    public:
        ref& operator=(bool value);
        operator bool() const;

        template <typename T>
        ref& operator=(const T& value) {
            bool b = static_cast<bool>(value);
            tb.pisz(index, b);
            return *this;
        }

        ref& operator=(const ref& other) {
            bool b = static_cast<bool>(other);
            tb.pisz(index, b);
            return *this;
        }
    };
};



#endif /* tab_bit_hpp */
